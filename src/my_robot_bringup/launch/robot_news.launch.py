from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    robot_parameters = [{"robot_name":"giscard"},
                             {"robot_name":"bb8"}, 
                             {"robot_name":"daneel"},
                             {"robot_name":"jander"}, 
                             {"robot_name":"c3p0"}]
    
    remap_robot_topic = [("robot_news", "giscard_robot"),
                                 ("robot_news", "bb8_robot"),
                                 ("robot_news", "daneel_robot"),
                                 ("robot_news", "jander_robot"),
                                 ("robot_news", "c3p0_robot")]

    robot_giskard_node = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="giscard_news_station",
        remappings=[
            remap_robot_topic[0]
        ],
        parameters=[
            robot_parameters[0]
        ]
    )

    robot_bb8_node = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="bb8_news_station",
        remappings=[
            remap_robot_topic[1]
        ],
        parameters=[
            robot_parameters[1]
        ]
    )

    robot_daneel_node = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="daneel_news_station",
        remappings=[
            remap_robot_topic[2]
        ],
        parameters=[
            robot_parameters[2]
        ]
    )

    robot_jander_node = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="jander_news_station",
        remappings=[
            remap_robot_topic[3]
        ],
        parameters=[
            robot_parameters[3]
        ]
    )

    robot_c3p0_node = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="c3p0_news_station",
        remappings=[
            remap_robot_topic[4]
        ],
        parameters=[
            robot_parameters[4]
        ]
    )

    smartphone = Node(
        package="my_py_pkg",
        executable="smartphone",
        name="smartphone"

    )


    ld.add_action(robot_giskard_node)
    ld.add_action(robot_bb8_node)
    ld.add_action(robot_daneel_node)
    ld.add_action(robot_jander_node)
    ld.add_action(robot_c3p0_node)
    ld.add_action(smartphone)

    return ld
