#!/usr/bin/env python3

import rclpy 
from edragorn_brain.core.states import BrainState
from rclpy.node import Node
from std_msgs.msg import String

class BrainNode(Node):

    def __init__(self):

        super().__init__("brain_node")

        self.get_logger().info('BRAIN NODE HAS BEEN STARTED.')

        self.state = BrainState.idle
        self.target_visible = False
        self.last_perception = None
    
        self.timer = self.create_timer(2.0, self.think)

        self.subscription = self.create_subscription(
            String,
            'camera_data',
            self.camera_callback,
            10
        )

        self.command_publisher = self.create_publisher(
            String,
            'brain_commands',
            10
        )


    def camera_callback(self, msg):
        self.last_perception = msg.data
        self.target_visible = (msg.data == "target_detected")
        self.get_logger().info(f'Received from perception: {msg.data}')
        self.get_logger().info(f'target_visible={self.target_visible}')

    def publish_command(self, command):
        msg = String()
        msg.data = command

        self.get_logger().info(f'Publishing command:{command}')
        self.command_publisher.publish(msg)



    def think(self):
        self.get_logger().info("I AM THINKING...")

        if self.state == BrainState.idle:
            self.get_logger().info("STATUS: IDLE -> SEARCHING")
            self.state = BrainState.searching

        elif self.state == BrainState.searching:
            self.get_logger().info("STATUS: SEARCHING...")

            if self.target_visible:
                self.get_logger().info("TARGET DETECTED BY PERCEPTION")
                self.state = BrainState.target_found

        elif self.state == BrainState.target_found:
            self.get_logger().info("STATUS: TARGET FOUND -> TRACKING")
            self.state = BrainState.tracking

        elif self.state == BrainState.tracking:
            self.get_logger().info("STATUS: TRACKING...")

            self.publish_command("follow_target")

            if not self.target_visible:
                self.get_logger().info("TARGET LOST -> SEARCHING")
                self.publish_command("search_target")
                self.state = BrainState.searching
                

        
def main(args=None):

    rclpy.init(args=args)

    node = BrainNode()

    rclpy.spin(node)

    node.destroy_node()


    rclpy.shutdown()                


if __name__ == '__main__':
            main()


