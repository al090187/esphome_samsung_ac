import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor, sensor, climate, uart, select, button
from esphome.const import (
    CONF_ID,
    CONF_BUTTON,
    DEVICE_CLASS_BUTTON,
    DEVICE_CLASS_DURATION,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_TEMPERATURE,
    ENTITY_CATEGORY_CONFIG,
    ENTITY_CATEGORY_DIAGNOSTIC,
    ICON_POWER,
    ICON_TIMER,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    UNIT_CELSIUS,
    UNIT_HOUR,
    UNIT_KILOWATT_HOURS,
)

DEPENDENCIES = ["uart"]
AUTO_LOAD = ["sensor", "select"]
