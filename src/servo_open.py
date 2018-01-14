#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

import time
import wiringpi

class ROS_Servo():
    def callback(self,data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
    def __init__(self):

        self.servo_state = 0 #0=open, 1=closed
        

        self.result_sub = rospy.Subscriber("/result", Int16, self.callback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

    def main(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('servo_open', anonymous=True)
    servo = ROS_Servo()
    servo.main()
