# ROS-Python

### Create ROS Package
#### Create a workspace and initialize catkin workspace
```
$ mkdir -p ~/catkin_ws/src
$ cd catkin_ws/src
$ catkin_init_workspace
```
#### Catkin_make and source workspace
```
$ cd ..
$ catkin_make
$ source ~/catkin_ws/devel/setup.bash
```
#### Create Package in src folder
Using catkin_create_pkg  ===> EX: $ catkin_create_pkg beginner_tur std_msgs  rospy roscpp
```
$ cd catkin_ws/src
$ catkin_create_pkg _name_ _depend1_ _depend2_
$ cd ..
$ catkin_make
```
#### Source
```
$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```
## Some Useful Command
| Command      | Description  | Example  |
|------------- |:-------------:| -----:|
|`$ rospack find {name of the package}` | find the location of the package | Ex rospack find roscpp |
|`$ rospack depends {name of the package}` | find the package that the package depend on      | rospack depends turtlesim|
|`$ rospack help`|show description of rospack||
|`$ rosrun rqt_graph rqt_graph`|show rqt graph||
|`$ roscd roscpp`|change directory to ROS package in system||
|`$ rosls roscpp`|list content in the dir||
|`$ find . -name".py" -exec chmod +x {} \;`|Find all file ending in .py and make executable||
