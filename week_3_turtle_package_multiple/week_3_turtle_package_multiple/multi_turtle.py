import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class MultiTurtlePublisher(Node):
    def __init__(self):
        super().__init__('multi_turtle_publisher')

        self.pub1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pub2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.pub3 = self.create_publisher(Twist, '/turtle3/cmd_vel', 10)

        self.triangle_step = 0
        self.triangle_count = 0

        self.square_step = 0
        self.square_count = 0

        self.timer = self.create_timer(0.5, self.move_turtles)

    def move_turtles(self):
        # turtle1 -> circle
        msg1 = Twist()
        msg1.linear.x = 2.0
        msg1.angular.z = 1.0
        self.pub1.publish(msg1)

        # turtle2 -> triangle
        msg2 = Twist()
        if self.triangle_step == 0:
            msg2.linear.x = 2.0
            msg2.angular.z = 0.0
            self.triangle_count += 1
            if self.triangle_count >= 4:
                self.triangle_step = 1
                self.triangle_count = 0
        else:
            msg2.linear.x = 0.0
            msg2.angular.z = 2.09
            self.triangle_count += 1
            if self.triangle_count >= 2:
                self.triangle_step = 0
                self.triangle_count = 0
        self.pub2.publish(msg2)

        # turtle3 -> square
        msg3 = Twist()
        if self.square_step == 0:
            msg3.linear.x = 2.0
            msg3.angular.z = 0.0
            self.square_count += 1
            if self.square_count >= 4:
                self.square_step = 1
                self.square_count = 0
        else:
            msg3.linear.x = 0.0
            msg3.angular.z = 1.57
            self.square_count += 1
            if self.square_count >= 2:
                self.square_step = 0
                self.square_count = 0
        self.pub3.publish(msg3)


def main(args=None):
    rclpy.init(args=args)
    node = MultiTurtlePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
