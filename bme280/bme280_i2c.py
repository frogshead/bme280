# -*- coding: utf-8 -*-

import smbus

default_i2c_address = None
default_bus = None


def set_default_i2c_address(i2c_address):
    global default_i2c_address
    default_i2c_address = i2c_address


def set_default_bus(bus_number):
    global default_bus
    default_bus = smbus.SMBus(bus_number)


def read_byte_data(cmd, bus=None, i2c_address=None):
    if bus is None:
        bus = default_bus
    if i2c_address is None:
        i2c_address = default_i2c_address
    return bus.read_byte_data(i2c_address, cmd)


def write_byte_data(cmd, value, bus=None, i2c_address=None):
    if bus is None:
        bus = default_bus
    if i2c_address is None:
        i2c_address = default_i2c_address
    return bus.write_byte_data(i2c_address, cmd, value)
