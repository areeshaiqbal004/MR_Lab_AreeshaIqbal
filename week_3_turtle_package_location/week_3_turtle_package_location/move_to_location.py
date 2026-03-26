import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute


class MoveToLocationClient(Node):
    def __init__(self):
        super().__init__('move_to_location_client')

        self.client = self.create_client(
            TeleportAbsolute,
            '/turtle1/teleport_absolute'
        )

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for teleport service...')

        self.send_request()

    def send_request(self):
        request = TeleportAbsolute.Request()
        request.x = 7.0
        request.y = 3.0
        request.theta = 0.0

        future = self.client.call_async(request)
        future.add_done_callback(self.response_callback)

    def response_callback(self, future):
        try:
            future.result()
            self.get_logger().info('Turtle moved to location (7.0, 3.0)')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')
        finally:
            rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = MoveToLocationClient()
    rclpy.spin(node)
    node.destroy_node()


if __name__ == '__main__':
    main()
