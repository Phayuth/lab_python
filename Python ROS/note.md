# ROS-Python
# ROS In 5 Minute Note
### by The Construct
1. ROS Catkin Workspace

create catkin_ws on home directory
```
$ mkdir catkin_ws/src -p
$ cd catkin_ws
$ catkin_make
$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
```
Now roscd can be use to navigate to catkin_ws

2. Create ROS Package

Using catkin_create_pkg with -h flag for help
```
$ catkin_create_pkg -k
```
Example
```
$ cd catkin_ws
$ cd src
$ catkin_create_pkg tutorial rospy std_msgs
$ cd ..
$ catkin_make
```
rospy and std_msgs is the dependencies of package

3. Create ROS Publisher

In Package folder
```
$ cd src
$ touch publisher.py
$ gedit publisher.py
```
In editor
```
# Code_ros_py_publisher_tutorial.py
#! /usr/bin/env python

WRITE PYTHON CODE HERO

```
Run the code
```
rosrun tutorial publisher.py
```
4. ROSCORE
Run roscore the initiate ros master server for ROS
```
roscore
```
5. ROS Node
ROS node contains a code for Publication, Subscription and Services
```
$ rosnode list
$ rosnode info /scan
```
6. ROS run
```
$ rosrun [name of the package] [executable code.py]
```
Use rosrun -h flag for help

7. ROS run vs ROS launch

- ROS run can run without knowing the exact location of the package
- ROS laucn can run multiple node at once
Create launch file
```
$ touch exe.launch
```
In launch file:
```
<launch>
  <node name="arbitrary_name1" pkg="name_of_the_package1" type"name_of_the_executable1"/>
  <node name="arbitrary_name2" pkg="name_of_the_package2" type"name_of_the_executable2"/>
  <node name="arbitrary_name3" pkg="name_of_the_package3" type"name_of_the_executable3"/>
</launch>
```
8. ROS Master URI
```
$ echo $ROS_MASTER_URI
```
Setup ROS Server
```
$ gedit ~/.bashrc
export ROS_MASTER_URI=http://IP:11311
export ROS_IP=IP
```
9. ROS Parameter Server
```
$ rosparam list
$ rosparam get /[value_or_topic]
```
10. ROS Package

ROS Package is the folder that keep ROS organized. ROS package contains package.xml and CMakeList.txt\
More Advance Package contains : config, include, launch, msg, scripts, src, srv
```
$ tree .
```
To see all avilable package in the machine run :
```
$ rospack list
```
11. CMakeList.txt

CMakeList is for the list method for compile, build and install the package

12. Launch file Remap
```
$ touch remap.launch
$ gedit rempa.launch
```
In the editor :
```
<launch>
  <remap from="old_topic_name" to "new_topic_name" />
</launch>
```
13. Run Python and C++ code in ROS

- For python catkin_make can be use directly on catkin_ws.
- For C++, CMakeList need to be edit by adding under #######build######:
```
# Declare a C++ executable
add_executable(obiwancpp src/obiwancpp.cpp)

# Add cmake target dependencies of the executable
# same as for the library above
add_dependencies(obiwancpp ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

# Specify libraries to link a library or executable target against
target_link_libraries(obiwancpp
  ${catkin_LIBRARIES}
)
```
https://gist.github.com/bayodesegun/68bc6043c206d73dfdbb8275bd9fde8f

14. Launch file include in Launch file
```
<launch>
  <include file"path_to_launch_file.launch" />
  <include file"$(find rospy_tutorial)/src/exe.launch" />
  <include ns="namespace1" file"$(find rospy_tutorial)/src/exe.launch" />
  <include ns="namespace2" file"$(find rospy_tutorial)/src/exe.launch" />
</launch>
```
15. Compile ROS Message

Create folder msg
```
$ touch exe.msg
```
In exe.msg, define the data. For example :
```
string name
float32 price
```
#### Then in CMakeList.txt, under # Declare ROS Message, services and actions # See the intruction for compile
- In package.xml, uncomment <run_depend>message_runtime</run_depend> and <build_depend>message_generation</build_depend>
- In CMakeList.txt, under find_package  add message_generation std_msgs
- In CMakeList.txt, under add_message_files add (name of the msg we create)exe.msg
- In CMakeList.txt, uncomment generate_messages
- In CMakeList.txt, under catkin_package add DEPENDS message_runtime
```
$ catkin_make
$ rosmsg list | grep
```
To test using python
```
$ python -c 'from financial_market.msg import exe; print "OK"'
```
More on : https://www.youtube.com/watch?v=NpqRLuUj2vE

16. ROS Service

ROS Service has a request and a respond.\
ROS Service is synchronize and interactive.
```
$ rosservice list
$ rosservice info /model
$ rossrv show asdf/asdf
$ rosservice call asdf/asdf
```

17. Compile ROS Service Message

- To make the service
Example
```
$ mkdir srv
$ touch exe.srv
$ gedit exe.srv
```
In editor:
```
float32 a
float32 b
---
float32 sum
```
- To compile
DO Like ROS message compile

More on : https://www.youtube.com/watch?v=9scwWpM7jiw

18. Compile ROS Action messages
19. Create ROS Service Client
20. Create ROS Action Server
21. ROS Action
22. Create ROS Action Client
23. Rosed, use and configure
24. ROS Package Path
25. ROS IP
26. setup.bash and setup.sh
27. ROS directories , src , build, devel
28. rqt_graph
29. roswtf
30. tf view frame
31. ROS tf
32. ROS Namespace
33. ROS bag
34. rqt plot
35. rqt_console, debugging
36. Turtlesim ROS basic
37. Package.xml
38. Gazebo create and launch
39. Master ROS Subject
40. Load params on Parameter Server
41. Unit test loading ROS Param
42. Testing ROS python code
43. /tf data
44. Robot pose publish with Tfbroadcaster in python
