# imports required: rclpy and addtwoInt type
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

# extend node for server, make server with type addtwoint and callback
class SimpleServer(Node):
    def __init__(self):
        super().__init__('simple_server')
        _ = self.create_service(AddTwoInts, 'adder', self.adder_service_callback)

# callback (req, res) -> return response set to added result, log request as recieved
    def adder_service_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Request received: ( %d , %d )' % (request.a, request.b ))

        return response

# initialize rcl client and node obj and spin rclpy on obj. delete node and shutdown rcl client

def main():
    rclpy.init()
    simple_serv = SimpleServer()
    rclpy.spin(simple_serv)
    rclpy.shutdown()


if __name__ == '__main__':
    main()




