#!/bin/env python3
from openrazer.client import DeviceManager

device_manager = DeviceManager()

viper = None
for device in device_manager.devices:

    if "Razer Viper Ultimate (Wireless)" == device.name:
        viper = device

if None == viper:
    print("n/a")
    exit

print("{}%".format(viper.battery_level))
