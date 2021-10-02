#!/bin/env python3
from openrazer.client import DeviceManager
from colours import linear_gradient

device_manager = DeviceManager()

device_manager.sync_effects = False

steps = 100

gradient = linear_gradient('#FF0000', '#00FF00', steps)

viper = None
for device in device_manager.devices:
    if "Razer Viper Ultimate (Wireless)" == device.name:
        viper = device
    elif "Razer Mouse Dock" == device.name:
        dock = device

if None == viper:
    exit

dock.fx.static(gradient['r'][viper.battery_level], gradient['g']
               [viper.battery_level], gradient['b'][viper.battery_level])

print("Batttery is at {}%, setting dock to r:{} g:{} b:{}".format(viper.battery_level,
      gradient['r'][viper.battery_level], gradient['g'][viper.battery_level], gradient['b'][viper.battery_level]))
