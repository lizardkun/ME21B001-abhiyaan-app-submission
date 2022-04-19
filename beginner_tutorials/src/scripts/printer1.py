#!/usr/bin/python3


import rospy
from std_msgs.msg import String
def fax_handler(data):
    print(data.data)
def printer():
    rospy.init_node('printer', anonymous=True)
    rospy.Subscriber('/Team_abhiyaan',String,fax_handler)
    rospy.spin()
    

if __name__ == '__main__':
    printer()