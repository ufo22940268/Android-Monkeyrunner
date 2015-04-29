#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 ccheng <ccheng@cchengs-Mac-Pro.local>
#
# Distributed under terms of the MIT license.

"""

"""


import os
import random
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

height = 480
width = 800

class Apk:
    def __init__(self, path, package):
        self.path = "apks/" + path
        self.package = package

apks = [
        Apk("a.apk", "com.ushaqi.zhuishushenqi")
]

def key(code): 
    device.press(code, MonkeyDevice.DOWN_AND_UP)

def drag(f, t):
    device.drag(f, t, 100, 1)

device = MonkeyRunner.waitForConnection()

def testApk():
    #Test install uninstall apks.
    for apk in apks:
        device.removePackage(apk.package)
        device.installPackage(apk.path)
        device.removePackage(apk.package)

    showDialog()


def testSwitchSpace():
    key('KEYCODE_HOME')
    #Switch in workspace
    for _ in range(5):
        device.drag((0, height/2), (width*(1 if random.random() > 0.5 else -1), height/2))

    showDialog()

def showDialog():
    result = MonkeyRunner.choice(u"选择你要测试的项目", ["Apk install and uninstall", "swap workspace"], u"测试")
    if result == 0:
        testApk()
    else:
        testSwitchSpace()

showDialog()
