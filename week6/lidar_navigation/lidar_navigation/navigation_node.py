import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np

class LidarNavigator(Node):

    def __init__(self):
        super().__init__('lidar_navigator')

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)

        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        # Thresholds
        self.front_threshold = 0.5
        self.side_threshold = 0.4

    def scan_callback(self, msg):

        ranges = np.array(msg.ranges)

        # -----------------------------
        # Clean data
        # -----------------------------
        ranges[np.isinf(ranges)] = 10
        ranges[np.isnan(ranges)] = 10

        # -----------------------------
        # Define regions
        # -----------------------------
        front = np.concatenate((ranges[:20], ranges[-20:]))
        left = ranges[60:120]
        right = ranges[240:300]

        # Minimum distance
        front_dist = np.min(front)
        left_dist = np.min(left)
        right_dist = np.min(right)

        twist = Twist()

        # -----------------------------
        # Obstacle logic
        # -----------------------------
        if front_dist < self.front_threshold:

            # Turn direction
            if left_dist > right_dist:
                twist.angular.z = 0.5   # turn left
            else:
                twist.angular.z = -0.5  # turn right

            twist.linear.x = 0.0

        else:
            # Move forward
            twist.linear.x = 0.15
            twist.angular.z = 0.0

        # Debug print
        self.get_logger().info(
            f"Front: {front_dist:.2f}, Left: {left_dist:.2f}, Right: {right_dist:.2f}"
        )

        self.publisher.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = LidarNavigator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
