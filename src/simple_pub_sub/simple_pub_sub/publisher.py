# ros imports
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

# publisher class from node
# create a publisher
# for an interval add a timer on node 
# increment a counter to be displayed on timer
# write a timer callback to publish message onto publisher
# display published message on logger

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('SimplePublisher')
        self.publisher_ = self.create_publisher(String, topic='hello', qos_profile=10)
        interval_ = 0.5
        self.timer_ = self.create_timer(interval_, self.publish_)
        self.counter_ = 0

    def publish_(self):
        msg_ = String()
        msg_.data = 'Hello: %d' % self.counter_

        self.publisher_.publish(msg_)
        self.get_logger().info('Publishing: %s' % msg_.data)

        self.counter_ += 1

# main func -> init rcl, get instance of publisher node, spin (run) publisher
# externally terminate node and shutdown client after exec

def main(args = None):
    rclpy.init(args = args)
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)

    simple_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()