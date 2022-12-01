import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16 #使う型を変更

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10) #変更
n = 0
def cb():
    global n
    msg = Int16()         #受信するデータの型を変更
    msg.data = n
    pub.publish(msg)
    n += 1

node.create_timer(0.5, cb)
rclpy.spin(node)
