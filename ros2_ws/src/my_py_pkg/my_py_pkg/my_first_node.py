#!/usr/bin/env python3
# Crate Node Template 

import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello ROS2")
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("Hello" + "::" + str(self.counter_))

def main(args=None):
    rclpy.init(args=args)  # first line every ros2 node

    node = MyNode()

    rclpy.spin(node) # Node callbacks
    rclpy.shutdown() # Last line every ros2 node

if __name__ == "__main__":
    main()
