#!/bin/env python3
import openrazer.client as razer
import time
# from colours import linear_gradient

device_manager = razer.DeviceManager()

device_manager.sync_effects = False

# steps = 100

# gradient = linear_gradient('#FF0000', '#00FF00', steps)

gradient = {'r': [255, 252, 249, 247, 244, 242, 239, 236, 234, 231, 229, 226, 224, 221, 218, 216, 213, 211, 208, 206, 203, 200, 198, 195, 193, 190, 188, 185, 182, 180, 177, 175, 172, 170, 167, 164, 162, 159, 157, 154, 151, 149, 146, 144, 141, 139, 136, 133, 131, 128, 126, 123, 121, 118, 115, 113, 110, 108, 105, 103, 100, 97, 95, 92, 90, 87, 85, 82, 79, 77, 74, 72, 69, 66, 64, 61, 59, 56, 54, 51, 48, 46, 43, 41, 38, 36, 33, 30, 28, 25, 23, 20, 18, 15, 12, 10, 7, 5, 2, 0], 'g': [
    0, 2, 5, 7, 10, 12, 15, 18, 20, 23, 25, 28, 30, 33, 36, 38, 41, 43, 46, 48, 51, 54, 56, 59, 61, 64, 66, 69, 72, 74, 77, 79, 82, 85, 87, 90, 92, 95, 97, 100, 103, 105, 108, 110, 113, 115, 118, 121, 123, 126, 128, 131, 133, 136, 139, 141, 144, 146, 149, 151, 154, 157, 159, 162, 164, 167, 170, 172, 175, 177, 180, 182, 185, 188, 190, 193, 195, 198, 200, 203, 206, 208, 211, 213, 216, 218, 221, 224, 226, 229, 231, 234, 236, 239, 242, 244, 247, 249, 252, 255]}

while True:
    viper = None
    for device in device_manager.devices:
        if "Razer Viper Ultimate (Wireless)" == device.name:
            viper = device
        elif "Razer Mouse Dock" == device.name:
            dock = device

    if viper == None:
        exit

    battery = viper.battery_level

    # battery = 99

    if battery >= 99:
        dock.fx.static(0, 255, 0)
        print("Batttery is at {}%, setting dock to r:0 g:255 b:0".format(battery))
    else:
        dock.fx.static(gradient['r'][battery], gradient['g'][battery], 0)
        print("Batttery is at {}%, setting dock to r:{} g:{} b:{}".format(
            battery, gradient['r'][battery], gradient['g'][battery], 0))

    time.sleep(5)
