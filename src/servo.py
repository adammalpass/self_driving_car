#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16

from rrb3 import *

import time
import pigpio

CLOSE_PW = 1480
OPEN_PW = 2200
SERVO=10

class ROS_Servo():
    def callback(self,data):
        #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        distance = self.rr.get_distance()       
        print distance
        if distance < 20:
            if not data.data:
                rospy.loginfo("It's the dog - keep shut!")
                action = "CLOSE"
                #self.pi.set_servo_pulsewidth(SERVO, CLOSE_PW)
            else:
                rospy.loginfo("It`s you - enjoy your treats!")
                action = "OPEN"
                #self.pi.set_servo_pulsewidth(SERVO, OPEN_PW)
            
        else:
            rospy.loginfo("Noone here - keep shut!")
            action = "CLOSE"
            #self.pi.set_servo_pulsewidth(SERVO, CLOSE_PW)
       
        self.last_decision.append(action)
        self.last_decision = self.last_decision[1:]



        if self.last_decision == ["OPEN", "OPEN", "OPEN", "OPEN"] and self.servo_state == "CLOSE":
            self.pi.set_servo_pulsewidth(SERVO, OPEN_PW)
            self.servo_state = "OPEN"
            print "OPENING"
        elif self.last_decision == ["CLOSE", "CLOSE", "CLOSE", "CLOSE"] and self.servo_state == "OPEN":
            self.pi.set_servo_pulsewidth(SERVO, CLOSE_PW)
            self.servo_state = "CLOSE"
            print "CLOSING"

    def __init__(self):
        
        self.pi = pigpio.pi()
        self.servo_state = "CLOSE" #0=open, 1=closed
        self.last_decision = ["CLOSE", "CLOSE", "CLOSE", "CLOSE"]
        self.pi.set_servo_pulsewidth(SERVO, CLOSE_PW)
        self.count = 0        

        self.rr = RRB3()

        self.result_sub = rospy.Subscriber("/result", Int16, self.callback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

    def main(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('servo_open', anonymous=True)
    servo = ROS_Servo()
    servo.main()
