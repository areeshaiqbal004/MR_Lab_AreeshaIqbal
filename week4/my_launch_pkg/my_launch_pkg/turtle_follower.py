import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TurtleFollower(Node):
    def __init__(self):
        super().__init__('follower_node')
        # Publisher for the second turtle's velocity
        self.publisher_ = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        
        # Subscribers for both turtle positions
        self.create_subscription(Pose, '/turtle1/pose', self.leader_cb, 10)
        self.create_subscription(Pose, '/turtle2/pose', self.follower_cb, 10)
        
        self.leader_pose = None
        self.follower_pose = None

    def leader_cb(self, msg):
        self.leader_pose = msg
        self.track_leader()

    def follower_cb(self, msg):
        self.follower_pose = msg

    def track_leader(self):
        if self.leader_pose is None or self.follower_pose is None:
            return

        msg = Twist()
        dx = self.leader_pose.x - self.follower_pose.x
        dy = self.leader_pose.y - self.follower_pose.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance > 1.0:
            msg.linear.x = 1.0 * distance
            goal_theta = math.atan2(dy, dx)
            msg.angular.z = 4.0 * (goal_theta - self.follower_pose.theta)
        
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleFollower()
    rclpy.spin(node)
    rclpy.shutdown()
