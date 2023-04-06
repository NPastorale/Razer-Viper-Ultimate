import os
import pyudev


def device_connected(device):
    print("Device connected:", device.device_node)


def device_disconnected(device):
    print("Device disconnected:", device.device_node)


# Get the vendor and product IDs of the USB device
lsusb_output = os.popen("lsusb").read().strip()
lsusb_lines = lsusb_output.split("\n")
for line in lsusb_lines:
    if "Razer USA, Ltd" in line:
        vendor_id, product_id = line.split()[5].split(":")

# Get the input device name of the mouse
evtest_output = os.popen("evtest").read().strip()
evtest_lines = evtest_output.split("\n")
for line in evtest_lines:
    if "Razer USA, Ltd" in line:
        device_path = line.split("/")[-1]

# Create a context object for Pyudev
context = pyudev.Context()

# Monitor the input device for changes
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('input', device_path=device_path)

# Add callbacks for device connection and disconnection events
observer = pyudev.MonitorObserver(monitor, callback=lambda action, device: device_connected(
    device) if action == 'add' else device_disconnected(device))
observer.start()
