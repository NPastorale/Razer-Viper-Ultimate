from openrazer.client import DeviceManager

device_manager = DeviceManager()

device_manager.sync_effects = False

for device in device_manager.devices:

    if "Razer Mouse Dock" == device.name:
        device.fx.static(255, 255, 255)
