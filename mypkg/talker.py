import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16 #使う型を変更

class Talker():
    def __init__(self, node_ref):  # オブジェクトを作ると呼ばれる関数
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0
        node_ref.create_timer(0.5, self, cb)

    def cb(self):
        msg = Int16()         #受信するデータの型を変更
        msg.data = self.n
        talker.pub.publish(msg)
        talker.n += 1

rclpy.init()
node = Node("talker")
talker = Talker(node)
rclpy.spin(node)
