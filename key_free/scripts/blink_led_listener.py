#!/usr/bin/env python
# -*- coding: utf-8 -*-
# rotate_servo_listener.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>
import rospy
from std_msgs.msg import Bool

from blink_led import BlinkLed

PIN_CTRL = 13


def callback(msg):
    bl = BlinkLed(PIN_CTRL)
    if msg.data is True:
        bl.on()
    else:
        bl.off()
    bl.cleanup()


def listener():
    rospy.init_node('blink_led_listener')
    rospy.Subscriber('/jishu_pro/blink_led', Bool, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
