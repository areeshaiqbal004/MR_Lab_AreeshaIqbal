import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TrianglePublisher(Node):
    def __init__(self):
        super().__init__('triangle_publisher')

        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.step = 0
        self.counter = 0

        # Timer (loop)
        self.timer = self.create_timer(0.5, self.move_triangle)

    def move_triangle(self):
        msg = Twist()

        # Move forward
        if self.step == 0:
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.counter += 1

            if self.counter >= 4:
                self.step = 1
                self.counter = 0

        # Turn
        elif self.step == 1:
            msg.linear.x = 0.0
            msg.angular.z = 2.09
            self.counter += 1

            if self.counter >= 2:
                self.step = 0
                self.counter = 0

        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = TrianglePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
