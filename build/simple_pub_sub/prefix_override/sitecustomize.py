import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/hegde-aryan/dev/robo/ros2_ws/install/simple_pub_sub'
