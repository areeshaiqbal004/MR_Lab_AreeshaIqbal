import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CmdVelPublisher(Node):

    def __init__(self):
        super().__init__('cmd_vel_publisher')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.toggle = True

    def timer_callback(self):
        msg = Twist()
        if self.toggle:
            msg.linear.x = 0.2
            self.get_logger().info('Moving Forward')
        else:
            msg.linear.x = 0.0
            self.get_logger().info('Stopping')

        self.publisher_.publish(msg)
        self.toggle = not self.toggle

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
