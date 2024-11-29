# import ros packages
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

# extend node to subscriber class
# create a subscriber to get a callback
# make a callback function for the subscriber to print onto logger

class SimpleSubscriber(Node):
    def __init__(self):
        super.__init__('SimpleSubscriber')
        _ = self.create_subscription(String, topic='hello', qos_profile=10, callback=self.subscriber_)

    def subscriber_(self, msg_):
        self.get_logger().info('Recieved: %s' % msg_)

# init rcl, get instance of node, spin node
# explictly destroy node and shutdown client

def main(args=None):
    rclpy.init(args)
    simple_subscriber = SimpleSubscriber()
    rclpy.spin(simple_subscriber)

    simple_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()