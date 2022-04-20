#!/usr/bin/python3


import rospy
from std_msgs.msg import String

#subscribes to the topic /Team_abhiyaan
def printer():
    rospy.init_node('receiver', anonymous=True)
    rospy.Subscriber('/Team_abhiyaan',String,reverse)
    rospy.spin()
    
#function that reverses incoming data
def reverse(data):
  data1=str(data)
  starter = ""
  for i in data1:
    starter = i + starter
  print(starter)
#the faxer that publishes reversed data to the topic /naayihba_maeT
def faxer(data):
    rospy.init_node('faxer',anonymous=True)
    pub=rospy.Publisher('/naayihba_maeT',String,queue_size=10)
    message=reverse(data)
    pub.publish(message)
#printer that subscribes to the published reversed output
def printer1():
    rospy.init_node('reverse', anonymous=True)
    rospy.Subscriber('/naayihba_maeT',String,fax_handler)
    rospy.spin()
    
def fax_handler(data):
    print(data.data)

if __name__ == '__main__':
    printer()