import rclpy
from rclpy.node import Node
import os


class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')

        # File to store counter
        file_path = os.path.join(os.path.dirname(__file__), 'counter.txt')

        # Read current count
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                count = int(f.read())
        else:
            count = 0

        count += 1

        # Save updated count
        with open(file_path, 'w') as f:
            f.write(str(count))

        self.get_logger().info(f'Run count: {count}')


def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    rclpy.spin_once(node, timeout_sec=0.1)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
