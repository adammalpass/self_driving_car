#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from rrb3 import *
import sys

rr = RRB3(9.0, 6.0) # battery, motor

def move_callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)

    speed = data.linear.x
    rot = data.angular.z

    #print speed, rot

    if rot == 0:
	if speed >= 0:
            #drive forward at set speed
            print "Driving forward at speed", speed
            rr.forward(seconds = 0.0, speed = speed)
	else:
            #drive backwards at set speed
            print "Driving backwards at speed", -speed
            rr.reverse(seconds = 0.0, speed = -speed)
	
    elif rot > 0:
        #drive left
        print "Driving left at speed", rot
        rr.left(seconds = 0.0, speed = rot)
    elif rot < 0:
        #drive right
        print "Driving right at speed", -rot
        rr.right(seconds = 0.0, speed = -rot)

    
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/cmd_vel_mux/input/teleop", Twist, move_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
