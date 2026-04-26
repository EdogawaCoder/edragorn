import rclpy
from rclpy.node import Node
from std_msgs.msg import String




class PerceptionNode(Node):  

    def __init__(self):
        super().__init__('perception_node')
    
        self.publisher_ = self.create_publisher(String, 'camera_data', 10)

        self.timer = self.create_timer(3.0, self.capture)

    def capture(self):
        msg = String()
        msg.data = "target_detected"

        self.get_logger().info(f'Publishing: {msg.data}')
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = PerceptionNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

