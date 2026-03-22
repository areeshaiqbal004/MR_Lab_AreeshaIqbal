import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class CirclePublisher(Node):
    def __init__(self):
        super().__init__('circle_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.move_circle()

    def move_circle(self):
        msg = Twist()

        # Set circular motion
        msg.linear.x = 2.0
        msg.angular.z = 1.0

        # Publish continuously for some time
        for _ in range(20):
            self.publisher_.publish(msg)
            time.sleep(0.5)

        # Stop the turtle
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CirclePublisher()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
