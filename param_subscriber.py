#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

# BEGIN CALLBACK
def callback(msg):
    print ">>> Time span driving forward (s)=", msg.data
# END CALLBACK


rospy.init_node('Internal parameters')

# BEGIN SUBSCRIBER
sub = rospy.Subscriber('fw_time', Int32, callback)
# END SUBSCRIBER

rospy.spin()
# END ALL
