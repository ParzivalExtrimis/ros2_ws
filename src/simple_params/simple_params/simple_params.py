# import node modulr for rclpy, 
import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rcl_interfaces.msg import ParameterDescriptor

# extend node for simple_params_node,
# make a timer with duration 1 and callback. Also set param on node
# get param on callback and display on logger
# ensure param is set back to default value

class SimpleParams(Node):
    def __init__(self):
        super().__init__('simple_params')
        desc_ = ParameterDescriptor(description = 'Parameter selects the greeting to be used with test output')
        self.declare_parameter('greeting', 'Hello', desc_)

        self.create_timer(1, self.callback_)

    def callback_(self):
        param_val_ = self.get_parameter('greeting').get_parameter_value().string_value
        
        # display
        self.get_logger().info('%s, world!' % param_val_)

        new_param_ = Parameter(
            'greeting',
            Parameter.Type.STRING,
            'Hello'     
        )

        self.set_parameters([new_param_])

# instantiate rclpy, node. spin node
def main():
    rclpy.init()
    node_ = SimpleParams()
    rclpy.spin(node_)

if __name__ == '__main__':
    main()