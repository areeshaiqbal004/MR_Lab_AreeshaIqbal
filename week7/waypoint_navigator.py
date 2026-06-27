import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped
import sys
import time

class WaypointNavigator(Node):
    def __init__(self):
        super().__init__('waypoint_navigator')
        self._client = ActionClient(self, FollowWaypoints, 'follow_waypoints')

    def send_waypoints(self, waypoints):
        self.get_logger().info('Waiting for FollowWaypoints server...')
        self._client.wait_for_server()

        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = waypoints

        self.get_logger().info(f'Sending {len(waypoints)} waypoints')

        send_goal_future = self._client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)

        goal_handle = send_goal_future.result()

        if not goal_handle.accepted:
            self.get_logger().error('Goal rejected!')
            return

        self.get_logger().info('Goal accepted, navigating...')
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)

        self.get_logger().info('All waypoints completed!')

def make_pose(x, y, w):
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = rclpy.clock.Clock().now().to_msg()

    pose.pose.position.x = float(x)
    pose.pose.position.y = float(y)
    pose.pose.position.z = 0.0

    pose.pose.orientation.x = 0.0
    pose.pose.orientation.y = 0.0
    pose.pose.orientation.z = 0.0
    pose.pose.orientation.w = float(w)

    return pose

def main():
    rclpy.init()
    node = WaypointNavigator()

    # Wait for Nav2 to fully start
    time.sleep(10)

    args = sys.argv[1:]

    if len(args) % 3 != 0 or len(args) == 0:
        print("Usage: python3 waypoint_navigator.py x1 y1 w1 x2 y2 w2 ...")
        return

    waypoints = []

    for i in range(0, len(args), 3):
        x = args[i]
        y = args[i+1]
        w = args[i+2]
        waypoints.append(make_pose(x, y, w))

    node.send_waypoints(waypoints)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
