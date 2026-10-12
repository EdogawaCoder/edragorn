#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class ActionNode(Node):

    def __init__(self):

        super().__init__('action_node')

        self.get_logger().info('ACTION NODE HAS BEEN STARTED.')

        self.subscription = self.create_subscription(
            String,
            'brain_commands',
            self.command_callback,
            10
        )

    def command_callback(self,msg):

        self.get_logger().info(f'Received command from brain: {msg.data}')

        if msg.data == 'follow_target':
            self.get_logger().info('ACTION: FOLLOWING TARGET')

        elif msg.data == 'search_target':
            self.get_logger().info('ACTION: SEARCHING TARGET')

        
        elif msg.data == 'data':
            self.get_logger().info('ACTION: STOP')

        else:
            self.get_logger().warn(f'UNKNOW COMMAND: {msg.data}')


def main(args=None):

        rclpy.init(args=args)

        node = ActionNode()

        rclpy.spin(node)

        node.destroy_node()

        rclpy.shutdown()

        if __name__ == '__main__':
            main()
        






