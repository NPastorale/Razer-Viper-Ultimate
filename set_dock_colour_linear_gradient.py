import openrazer.client as razer
import time
import logging
from colours import linear_gradient

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

steps = 100

UPPER_THRESHOLD = 95
LOWER_THRESHOLD = 15


gradient = linear_gradient(
    '#FF0000', '#00FF00', UPPER_THRESHOLD-LOWER_THRESHOLD)

mouse_battery_current = 0
mouse_battery_previous = 0
mouse_charging_state_current = False
mouse_charging_state_previous = False


device_manager = razer.DeviceManager()
device_manager.sync_effects = False


def get_dock():
    try:
        for device in device_manager.devices:
            if "Razer Mouse Dock" == device.name:
                return device
    except Exception as e:
        logging.error(f"Error while getting dock: {e}")
        return None


def get_mouse():
    try:
        for device in device_manager.devices:
            if "Razer Viper Ultimate (Wireless)" == device.name:
                return device
    except Exception as e:
        logging.error(f"Error while getting mouse: {e}")
        return None


def set_dock_colour(mouse_battery, dock):
    if mouse_battery >= UPPER_THRESHOLD:
        dock.fx.static(0, 255, 0)
        logging.info(
            "Battery is at {}%, setting dock to r:0 g:255 b:0".format(mouse_battery))
    elif mouse_battery > LOWER_THRESHOLD:
        dock.fx.static(gradient['r'][mouse_battery-LOWER_THRESHOLD],
                       gradient['g'][mouse_battery-LOWER_THRESHOLD], gradient['b'][mouse_battery-LOWER_THRESHOLD])
        logging.info("Battery is at {}%, setting dock to r:{} g:{} b:{}".format(
            mouse_battery, gradient['r'][mouse_battery-LOWER_THRESHOLD], gradient['g'][mouse_battery-LOWER_THRESHOLD], gradient['b'][mouse_battery-LOWER_THRESHOLD]))
    else:
        dock.fx.static(255, 0, 0)
        logging.info(
            "Battery is at {}%, setting dock to r:255 g:0 b:0".format(mouse_battery))


def set_brightness(mouse):
    charging_state = "charging" if mouse.is_charging else "not charging"
    logging.info(charging_state)


try:
    while True:
        mouse_battery_previous = mouse_battery_current
        try:
            mouse_battery_current = get_mouse().battery_level
        except Exception as e:
            logging.error(f"Error while getting mouse battery level: {e}")
        dock = get_dock()
        if dock is not None and mouse_battery_current is not None:
            if mouse_battery_current != mouse_battery_previous:
                set_dock_colour(mouse_battery_current, dock)
        time.sleep(1)

except KeyboardInterrupt:
    pass
