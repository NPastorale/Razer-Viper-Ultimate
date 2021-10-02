#!/bin/env python3
from openrazer.client import DeviceManager
from colour import Color

device_manager = DeviceManager()

device_manager.sync_effects = False

steps = 100

gradient = list(Color("#FF0000").range_to(Color("#00FF00"), steps))

viper = None
for device in device_manager.devices:
    if "Razer Viper Ultimate (Wireless)" == device.name:
        viper = device
    elif "Razer Mouse Dock" == device.name:
        dock = device

if None == viper:
    exit

dock.fx.static(round(gradient[viper.battery_level].get_red()*255), round(
    gradient[viper.battery_level].get_green()*255), round(gradient[viper.battery_level].get_blue()*255))

print("Batttery is at {}%, setting dock to r:{} g:{} b:{}".format(viper.battery_level, round(gradient[viper.battery_level].get_red(
)*255), round(gradient[viper.battery_level].get_green()*255), round(gradient[viper.battery_level].get_blue()*255)))
