#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from functools import partial
from example_interfaces.srv import AddTwoInts

class AddTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.call_add_two_ints_server(6, 7)
        self.call_add_two_ints_server(1, 2)
        self.call_add_two_ints_server(10, 13)
        self.call_add_two_ints_server(1, 10)


    def call_add_two_ints_server(self, a, b):
        client = self.create_client(AddTwoInts, "add_two_ints")   # First Create Client
        while not client.wait_for_service(1.0):  # Wait for the server 
            self.get_logger().warn("Waiting for server add two Ints...")

        # Created Request
        self.request = AddTwoInts.Request()
        self.request.a = a
        self.request.b = b

        # We need to call server
        future = client.call_async(request=self.request)
        future.add_done_callback(partial(self.callback_call_add_two_ints, a=a, b=b)) # We callback function for future complate

    def callback_call_add_two_ints(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(str(a) + " + " + str(b) + " = " + str(response.sum))

        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))



def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClientNode()
    rclpy.spin(node=node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
