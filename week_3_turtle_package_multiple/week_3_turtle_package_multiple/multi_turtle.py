import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class MultiTurtlePublisher(Node):
    def __init__(self):
        super().__init__('multi_turtle_publisher')

        self.pub1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pub2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.pub3 = self.create_publisher(Twist, '/turtle3/cmd_vel', 10)
        self.pub4 = self.create_publisher(Twist, '/turtle4/cmd_vel', 10)

        self.timer = self.create_timer(0.5, self.move_turtles)

    def move_turtles(self):
        msg1 = Twist()
        msg2 = Twist()
        msg3 = Twist()
        msg4 = Twist()

        msg1.linear.x = 2.0
        msg1.angular.z = 1.0

        msg2.linear.x = 1.5
        msg2.angular.z = 0.0

        msg3.linear.x = 1.0
        msg3.angular.z = -1.0

        msg4.linear.x = 2.0
        msg4.angular.z = 2.0

        self.pub1.publish(msg1)
        self.pub2.publish(msg2)
        self.pub3.publish(msg3)
        self.pub4.publish(msg4)


def main(args=None):
    rclpy.init(args=args)
    node = MultiTurtlePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
