from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
  # package_path = FindPackageShare('basic_rover_description')
  default_model = PathJoinSubstitution(['urdf', 'basic-rover.urdf'])

  launch_description = LaunchDescription()

  launch_description.add_action(DeclareLaunchArgument(
    name='model',
    default_value=default_model,
    description='Path to urdf file relative to basic_rover_description package',
  ))

  launch_description.add_action(IncludeLaunchDescription(
    PathJoinSubstitution([FindPackageShare('urdf_launch'), 'launch', 'display.launch.py']),
    launch_arguments={
      'urdf_package': 'basic_rover_description',
      'urdf_package_path': LaunchConfiguration('model'),
    }.items(),
  ))

  return launch_description
