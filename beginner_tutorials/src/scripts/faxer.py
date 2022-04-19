#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def faxer():
    rospy.init_node('faxer',anonymous=True)
    pub=rospy.Publisher('/Team_abhiyaan',String,queue_size=10)
    #loops the messages indefinitely 
    while not rospy.is_shutdown():
        message="Team Abhiyaan Rocks:"
        pub.publish(message)
        

#error handling, i have copy pasted this from the ROS wiki, i dont know how this works, but they said its important
if __name__ == '__main__':
    try:
        faxer()
    except rospy.ROSInterruptException:
        pass