#!/usr/bin/env pythong

from __future__ import print_function

class NetDevice(object):
    
    def __init__(self, ip_addr, username, password, serial_number=None, model=None, vendor=None, uptime=None, os_version=None):
        self._ip_addr = ip_addr
        self._username = username
        self._password = password

    @property
    def ip_addr(self):
        return self._ip_addr

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def serial_number(self):
        return self._serial_number

    @property
    def model(self):
        return self._model

    @property
    def vendor(self):
        return self._vendor

    @property
    def uptime(vendor):
        return self._uptime

    @property
    def os_version(self):
        return self._os_version

    @serial_number.setter
    def serial_number(self, serial_number):
        self._serial_number = serial_number

    @model.setter
    def model(self, model):
        self._model = model

    @vendor.setter
    def vendor(self, vendor):
        self._vendor = vendor

    @uptime.setter
    def uptime(self, uptime):
        self._uptime = uptime

    @os_version.setter
    def os_version(self, os_version):
        self._version = os_version


def main():

    net_dev_one = NetDevice('192.168.1.1', 'root', 'Passwd')
    net_dev_two = NetDevice('192.168.10.1', 'admin', 'Passwd')
    net_dev_three = NetDevice('172.16.32.1', 'lab', 'lab123')
    net_dev_four = NetDevice('10.0.20.1', 'console', 'Console0')
    print(net_dev_one)
    print(net_dev_one.ip_addr)
    print(net_dev_one.username)
    print(net_dev_one.password)

    print()

    net_dev_one.serial_number = 'SERIAL#'
    print(net_dev_one.serial_number)

if __name__ == '__main__':
    main()
