import time

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class TrianglePublisher(Node):
    def __init__(self):
        super().__init__('triangle_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.move_triangle()

    def move_triangle(self):
        for _ in range(3):
            msg = Twist()
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            time.sleep(2)

            msg.linear.x = 0.0
            msg.angular.z = 2.09
            self.publisher_.publish(msg)
            time.sleep(1)

        stop_msg = Twist()
        self.publisher_.publish(stop_msg)


def main(args=None):
    rclpy.init(args=args)
    node = TrianglePublisher()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
