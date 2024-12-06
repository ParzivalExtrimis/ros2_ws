import sys

from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node


class SimpleClientAsync(Node):

    def __init__(self):
        super().__init__('simple_client_async')
        self.client_ = self.create_client(AddTwoInts, 'adder')
        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        return self.client_.call_async(self.req)


def main():
    rclpy.init()

    simple_client = SimpleClientAsync()
    future = simple_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin_until_future_complete(simple_client, future)
    response = future.result()
    simple_client.get_logger().info(
        'Result ( %d , %d ): %d' %
        (int(sys.argv[1]), int(sys.argv[2]), response.sum))

    simple_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()