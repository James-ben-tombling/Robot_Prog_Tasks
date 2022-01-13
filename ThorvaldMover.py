#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class Mover:
    """
    A very simple Roamer implementation for Thorvald.
    It simply goes straight until any obstacle is within
    3 m distance and then just simply turns left.
    A purely reactive approach.
    """

    def __init__(self):
        """
        On construction of the object, create a Subscriber
        to listen to lasr scans and a Publisher to control
        the robot
        """
        self.publisher = rospy.Publisher(
            '/thorvald_001/teleop_joy/cmd_vel',
            Twist, queue_size=1)
        rospy.Subscriber("/thorvald_001/front_scan", LaserScan, self.callback)

    def callback(self, data):
        """
        Callback called any time a new laser scan becomes available
        """
        end = 390
        start = 330
        rospy.loginfo(
            rospy.get_caller_id() + "I heard %s", data.header.seq)
        min_dist = min(data.ranges[start:end])
        # min angle -2.18 rad/ -125 deg
        #  max 2.359 rad /130 deg
        # min_angle = data.angle_min
        # max_angle = data.angle_max
        # angle_increments = data.angle_increment
        # angle_range = max_angle - min_angle
        # angle_index = angle_range/angle_increments
        t = Twist()
        # print(angle_index)
        if min_dist < 4:
            t.angular.z = 1.0
            # t.linear.x = 0.8 
        else:
            t.linear.x = 0.8
        self.publisher.publish(t)

if __name__ == '__main__':
    rospy.init_node('mover')
    Mover()
    rospy.spin()

