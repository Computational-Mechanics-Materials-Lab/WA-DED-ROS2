## example.launch.py

import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.actions import GroupAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import TextSubstitution
from launch_ros.actions import Node
from launch_ros.actions import PushRosNamespace
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
print(get_package_share_directory('abb_irb4600_support'))

def generate_launch_description():
    #ld= LaunchDescription()

    #optris_dir=get_package_share_directory('optris_drivers2')
    optris_dir='/var/tmp/ROS/ros_ws_folder/ros2_ws_optris_abb/src/optris_drivers2/config/19102025.xml'
    print(optris_dir)
    #optris_config_dir=optris_dir+'/config/19102025.xml'

    Robot_launch_file= IncludeLaunchDescription(
	 PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('abb_irb4600_support'),'launch'),
	'/view_robot.launch.py'])
         )
    rviz = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        arguments=[
            "-d",
            PathJoinSubstitution(
                [
                    FindPackageShare("abb_irb4600_support"),
                    "rviz",
                    "urdf_description.rviz",
                ]
            ),
        ],
        output="screen",
    )

    return LaunchDescription([
	Robot_launch_file,
    DeclareLaunchArgument(
            'camera_calibration_file',
            default_value=get_package_share_directory('optris_drivers2') + '/config/19102025.xml'),
    Node(package = 'optris_drivers2',
            	     namespace ='optris_imager_node',
            	     executable = 'optris_imager_node', 
                     name = 'image',
                     #parameters =  [{"camera_calibration_file": LaunchConfiguration('camera_calibration_file')}]
                     arguments = [PathJoinSubstitution([FindPackageShare("optris_drivers2"),"config","19102025.xml",])], ),
                                  #str(optris_dir)], ),
                                  
    Node(package = 'optris_drivers2',
		    namespace = 'optris_colorconvert_node',
                    executable = 'optris_colorconvert_node',
                    name = 'convert', ),
    rviz
])
