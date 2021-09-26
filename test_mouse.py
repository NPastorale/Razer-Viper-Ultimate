from openrazer.client import DeviceManager
from pprint import pprint

device_manager = DeviceManager()

device_manager.sync_effects = False

for device in device_manager.devices:

    if "Razer Viper Ultimate (Wireless)" == device.name:

        pprint(dir(device.fx._lighting_dbus.get_dbus_method.__init__))
