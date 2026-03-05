#!/usr/bin/env python3
import rclpy 

from sre_parse import State
from states import BrainState
from rclpy.node import Node

class BrainNode(Node):


    def __init__(self):

        super().__init__("brain_node")

        self.get_logger().info('BRAIN NODE HAS BEEN STARTED.')
    
        self.timer = self.create_timer(2.0, self.think)

        self.state = BrainState.idle

    def think(self):
        self.get_logger().info('I AM THINKING...')

        if self.state == BrainState.idle:
           self.get_logger().info("STATUS: IDLE.")
           self.state = BrainState.searching
        
        elif self.state == BrainState.searching:
            self.get_logger().info("STATUS: SEARCHING...")
            self.state == BrainState.target_found

        elif self.state == BrainState.target_found:
            self.get_logger().info("STATUS: TARGET FOUND!")
            self.state = BrainState.tracking

        elif self.state == BrainState.tracking:
            self.get_logger().info("STATUS: LOST THE TARGET. TRACKING.")

    
def main(args=None):

    rclpy.init(args=args)

    node = BrainNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()



 
