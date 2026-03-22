import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('velocity_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.move_square()

    def move_square(self):
        for _ in range(4):
            msg = Twist()

            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            time.sleep(2)

            msg.linear.x = 0.0
            msg.angular.z = 1.57
            self.publisher_.publish(msg)
            time.sleep(1)

        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = VelocityPublisher()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
