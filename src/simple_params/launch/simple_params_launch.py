# import launch descriptions class, which is the type returned by generate launch descriptions
# import Node from launch_ros.actions which will be wrapped in launch desc

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='simple_params',
            executable='talker',
            name='cutom_simple_params_node',
            output='screen',
            emulate_tty=True,
            parameters=[
                {'greeting': 'Bonjour'}
            ]
        )
    ])