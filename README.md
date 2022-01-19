# Robot_Prog_Tasks 
LCAS Robot programming task from the workshop UoL <br />
## Basic stuff you should know 
1. Rostopic: Some nodes provide information for other nodes, as a camera feed would do, for example. Such a node is said to publish information that can be received by other nodes. The information in ROS is called a topic. Simply, A topic defines the types of messages that will be sent concerning that topic.
2. ROS Node: Basically, nodes are processes that perform some computation or task. The nodes themselves are really software processes but with the capability to register with the ROS Master node and communicate with other nodes in the system. The ROS design idea is that each node is independent and interacts with other nodes using the ROS communication capability. The Master node is described in the ROS Master section to follow.The nodes that transmit data publish the topic name and the type of message to be sent.
3. ROS message: ROS messages are defined by the type of message and the data format. The ROS package named std_msgs, for example, has messages of type String which consist of a string of characters. Other message packages for ROS have messages used for robot navigation or robotic sensors.
4. seeing the topic and nodes: <br />
  - $ roscore : to start the Master and allow nodes to communicate (doesng need to be done if your already done roslaunch.

  - $ rosnode list : to list the active nodes

  - $ rostopic list : to list the topics associated with active ROS nodes
  
5. ROS frame: simply means a frame of reference on which you base your odometry or robot parts

## how to start my ROS 
$ sudo apt-get update && sudo apt-get upgrade  <br />
$ sudo apt-get install ros-melodic-uol-cmp9767m-base ros-melodic-desktop  <br />
$ source /opt/ros/melodic/setup.bash  <br />
$ roslaunch bacchus_gazebo vineyard_demo.launch world_name:=vineyard_small
 <br />
if thats fails try <br />
$ sudo apt-get purge "*gazebo*" then step 3 again   <br />

for ease just name your workspace catkin_ws but up to you i dont care.

make a work space for a package  <br />
$ mkdir -p ~/<my_ws>/src  <br />
$ cd ~/<my_ws>/  <br />
$ catkin_make  <br />

## Workshop 2
go to your newly made work space (ws)  <br />

check the first order dependencies of the package tutorials  <br />
$ rospack depends1 beginner_tutorials  <br />
this can be used on any package using  <br />
$ rospack depends1 <package_name>  <br />
this can also be used on the 1st order dependencies to see the indirect dependencies  <br />

to see the package.xml file where the dependencies are stored follow  <br />
$ roscd <package_name>  <br />
$ cat package.xml  <br />

### Customizing the package.xml

The generated package.xml should be in your new package. Now lets go through the new package.xml and touch up any elements that need your attention.

#### First update the description tag:

![image](https://user-images.githubusercontent.com/92380630/148955445-6ae5d488-f177-4ba4-9853-ba0855aa87a2.png)


Change the description to anything you like, but by convention the first sentence should be short while covering the scope of the package. If it is hard to describe the package in a single sentence then it might need to be broken up.

#### Next comes the maintainer tag:

![image](https://user-images.githubusercontent.com/92380630/148955669-7a176a08-e059-4f70-992f-d9a91341760a.png)

This is a required and important tag for the package.xml because it lets others know who to contact about the package. At least one maintainer is required, but you can have many if you like. The name of the maintainer goes into the body of the tag, but there is also an email attribute that should be filled out:


![image](https://user-images.githubusercontent.com/92380630/148955781-8f821cb7-7109-42dc-a632-c517f2beeb68.png)

#### license tags

Next is the license tag, which is also required:

![image](https://user-images.githubusercontent.com/92380630/148955958-d652fb1a-393e-4fda-8267-053141c2d6b1.png)

You should choose a license and fill it in here. Some common open source licenses are BSD, MIT, Boost Software License, GPLv2, GPLv3, LGPLv2.1, and LGPLv3. You can read about several of these at the Open Source Initiative. For this tutorial we'll use the BSD license because the rest of the core ROS components use it already:

![image](https://user-images.githubusercontent.com/92380630/148956177-d06b3f55-5485-4f9d-8e93-82cbd598ebe9.png)

#### dependencies tags

The next set of tags describe the dependencies of your package. The dependencies are split into build_depend, buildtool_depend, exec_depend, test_depend. For a more detailed explanation of these tags see the documentation about Catkin Dependencies. Since we passed std_msgs, roscpp, and rospy as arguments to catkin_create_pkg, the dependencies will look like this:

![image](https://user-images.githubusercontent.com/92380630/148956375-49a1d42e-4ba0-4854-b692-3b4a0fa2e725.png)


All of our listed dependencies have been added as a build_depend for us, in addition to the default buildtool_depend on catkin. In this case we want all of our specified dependencies to be available at build and run time, so we'll add a exec_depend tag for each of them as well:

![image](https://user-images.githubusercontent.com/92380630/148956592-f9a9b89b-76ca-4103-8e5c-82850a10bdd7.png)


#### Final package.xml

As you can see the final package.xml, without comments and unused tags, is much more concise:

![image](https://user-images.githubusercontent.com/92380630/148956694-e4b0ff97-7541-4224-a671-5277a7e7b8df.png)

#### writing a publisher node 
$ roscd beginner_tutorials <br />
$ mkdir scripts <br />
$ cd scripts <br />
$ wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/talker.py <br />
$ chmod +x talker.py <br />

this goes into the beginner_tutorials and makes a folder called scripts which then has the talker.py file download into it

to see the new talker.py file use: <br />
$ rosed beginner_tutorials talker.py <br />
use :x to exit the rosed <br />
add this to end of cmakelists.txt file in the beginner tutorials folder <br />
catkin_install_python(PROGRAMS scripts/talker.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

To get the listener.py put the following:<br />
$ roscd beginner_tutorials/scripts/ <br />
$ wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/listener.py <br />
$ chmod +x listener.py <br />

Now add the follwing to the previous adjustment you made to cmakelists.txt so it looks like this at the end of the file 

catkin_install_python(PROGRAMS scripts/talker.py scripts/listener.py<br />
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}<br />
)

to build your new publisher and subscriber nodes do the following: <br />
$ cd ~/catkin_ws <br />
$ catkin_make <br />

to examine the previous nodes we just made do: <br />
$ roscore <br />

to start the talker (publisher) in a new terminal: <br />

$ cd ~/catkin_ws <br />
$ source ./devel/setup.bash <br />
$ rosrun beginner_tutorials talker.py <br />

next the listener (subscriber) in a new terminal  <br />

$ cd ~/catkin_ws <br />
$ source ./devel/setup.bash <br />
$ rosrun beginner_tutorials listener.py <br />

### finding the topic to make Thorvald move and publishing to it
to more the thorvald robot using publisher on rostopic: <br />
$ rostopic pub -r 10  thorvald_001/twist_mux/cmd_vel geometry_msgs/Twist <br />
using -r 10 is the rate which is required by ros <br />

### simple python controller for Thorvald

for this we are going to make a new package in the workspace we have used before (mines called catkin_ws).
follow this code like to before to setup your package 

$ cd ~/catkin_ws/src  <br />
i called mine catkin_ws remember dumby! but yours could be different 
$ catkin_create_pkg workshops std_msgs rospy roscpp  <br />
i called mine workshops just to remember where i made it  <br />
$ source ~/catkin_ws/devel/setup.bash <br />
$ roscd workshops  <br />
$ mkdir scripts <br />
$ cd scripts <br />

then either put: <br />
$ code ThorvaldMover.py <br />
if your have visual studio code downloaded and write your own/ base it off mine <br />
or <br />
download it with github with: <br />
$ wget https://github.com/James-ben-tombling/Robot_Prog_Tasks/blob/main/ThorvaldMover.py <br />
$ chmod +x ThorvaldMover.py <br />
Now add the follwing to the previous adjustment you made to cmakelists.txt so it looks like this at the end of the file 

catkin_install_python(PROGRAMS scripts/ThorvaldMover.py <br />
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}<br />
)

to build your new moving scripts do the following: <br />
$ cd ~/catkin_ws <br />
$ catkin_make <br />

in a new terminal launch the thorvald simulation  <br />
$ source /opt/ros/melodic/setup.bash  <br />
$ roslaunch bacchus_gazebo vineyard_demo.launch world_name:=vineyard_small  <br />

then go back to your terminal catking_ws  <br />
$ cd ~/catkin_ws  <br />
$ source ./devel/setup.bash  <br />
$ rosrun workshops ThorvaldMover.py  <br />
## Workshop 3 

### first update the system 

$ sudo apt-get update && sudo apt-get upgrade <br />
$ sudo apt-get install \ <br />
    ros-melodic-opencv-apps \ <br />
    ros-melodic-rqt-image-view \ <br />
    ros-melodic-uol-cmp9767m-base \ <br />
    ros-melodic-find-object-2d \ <br />
    ros-melodic-video-stream-opencv \ <br />
    ros-melodic-topic-tools \ <br />
    ros-melodic-rqt-tf-tree <br />

to see the different outputs of a rostopic type: <br />

$ rosmsg show message_type/node

for example:

$ rosmsg show sensor_msgs/LaserScan

close all terminal and start a new one <br />

$ source ~/catkin_ws/devel/setup.bash <br />
$ roscd workshops  <br />
$ cd scripts <br />

then use:
$ code tflistener.py <br />
or < br />
$ wget https://github.com/James-ben-tombling/Robot_Prog_Tasks/blob/main/tflistener.py

follow this with <br />
$ chmod +x tflistener.py

then edit your cmakelists.txt in the workshops folder <br />
catkin_install_python(PROGRAMS scripts/ThorvaldMover.py scripts/tflistener.py <br />
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION} <br />
)

to build your new tf listner scripts do the following: <br />
$ cd ~/catkin_ws <br />
$ catkin_make <br />
### lets add our new tf listener 

start it up in a new terminal baby 

$ source /opt/ros/melodic/setup.bash <br />
$ roslaunch bacchus_gazebo vineyard_demo.launch world_name:=vineyard_small  <br />

then again in a new terminal 

$ cd ~/catkin_ws  <br />
$ source ./devel/setup.bash  <br />
$ rosrun workshops tflistener.py  <br />

### roaming robot that shows the nearest point 

$ source ~/catkin_ws/devel/setup.bash <br />
$ roscd workshops  <br />
$ cd scripts <br />

then use:
$ code NearestObstacle.py <br />
or < br />
$ wget ***to be filled*** <br />

follow this with <br />
$ chmod +x NearestObstacle.py

then edit your cmakelists.txt in the workshops folder <br />
catkin_install_python(PROGRAMS scripts/ThorvaldMover.py scripts/tflistener.py scripts/NearestObstacle.py <br />
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION} <br />
)

to build your new tf listner scripts do the following: <br />
$ cd ~/catkin_ws <br />
$ catkin_make <br />
### lets add our new Nearest Obstacle 

start it up in a new terminal baby! 

$ source /opt/ros/melodic/setup.bash <br />
$ roslaunch bacchus_gazebo vineyard_demo.launch world_name:=vineyard_small  <br />

then again in a new terminal 

$ cd ~/catkin_ws  <br />
$ source ./devel/setup.bash  <br />
$ rosrun workshopsNearest Obstacle.py  <br />

Note (this is the same method for adding and running the files at the previous files)

after this go to RViz that should be running at click add
![image](https://user-images.githubusercontent.com/92380630/149778957-ac9c85b6-f2f2-4a95-b0c8-3d920d700092.png)

then add a Pose component 

go to the part of pose that says topic and specify /Nearest_Obstacle 

do this while the scripts NearestObstacle.py is running (it wont show if not running)

## Workshop 4 OpenCV

Update: sudo apt-get update && sudo apt-get upgrade
Install today's packages:
```

sudo apt-get install \
    ros-melodic-opencv-apps \
    ros-melodic-rqt-image-view \
    ros-melodic-image-geometry \
    ros-melodic-uol-cmp9767m-base \
    ros-melodic-uol-cmp9767m-tutorial \
    ros-melodic-find-object-2d \
    ros-melodic-video-stream-opencv \
    ros-melodic-image-view
```
run this to see all the nodes of a specific .launch file 

$ `roslaunch --nodes bacchus_gazebo vineyard_demo.launch`

run this to see the following files included in a .launch file 

$ `roslaunch --files bacchus_gazebo vineyard_demo.launch`

### lets build a package for testing out open CV that depends on rospy and cv_bridge 

follow this 


for making a package my_opencv_test use   <br />
$ `catkin_create_pkg my_opencv_test rospy cv_bridge`  <br />
in every new terminal you want to use your package you must source as follows  <br />
$ `source ~/<my_ws>/devel/setup.bash`  <br />

$ `roscd my_opencv_test` <br />
$ `mkdir scripts` <br />
$ `cd scripts` <br />
$ `wget https://github.com/James-ben-tombling/Robot_Prog_Tasks/blob/main/opencv_test.py`  <br />
$ `chmod +x opencv_test.py` <br />

then go to the new cmakelist.txt in the my_opencv_test package and add the folloeing to the very bootm of the file and save it 

catkin_install_python(PROGRAMS scripts/opencv_test.py <br />
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}<br />
)


to build your new opencv_test.py scripts do the following: <br />
$ `cd ~/catkin_ws` <br />
$ `catkin_make` <br />

in a new terminal wite the following to start the opencv_test.py

$ `cd ~/catkin_ws` <br />
$ `source ./devel/setup.bash` <br />
$ `rosrun my_opencv_test opencv_test.py `

## Workhop 5 geometry and 3D
first go into catkin_ws and download the turturial package and build with the following:

download this package https://github.com/LCAS/CMP9767M.git <br />
move uol_cmp9767m_tutorial to ~/catkin/src 

$ `cd ~/catkin_ws/src`  <br />

check it in there then:

$ `cd ~/catkin_ws` <br />
$ `catkin_make` <br />

in a fresh terminal launch vinyard with:
$` roslaunch bacchus_gazebo vineyard_demo.launch world_name:=vineyard_small`

in another terminal 
$ `cd ~/catkin_ws` <br />
$ `source ./devel/setup.bash` <br />
$ `rosrun uol_cmp9767m_tutorial image_projection_1.py 

then try 

$ `rosrun uol_cmp9767m_tutorial image_projection_2.py`

should get a blue dot about 5 metres on the floor infront of thorvald

in gazebo place a sphere from the top bar infront of the thorvald then 
go too:

![image](https://user-images.githubusercontent.com/92380630/149982801-7e1fc075-4624-4135-9c41-652253f9b34f.png)


$ `code image_projection_2.py `

and add the coordinate pose of the sphere to the scripts pose and change the frame_id from thorval_001/base_link to /map so it looks something like this: 

![image](https://user-images.githubusercontent.com/92380630/149982623-37937b55-dd76-45be-a7c9-3fbc9a047c41.png)

then go back to the terminal and rerun 

$ `rosrun uol_cmp9767m_tutorial image_projection_2.py`

you should get something that looks like this now 
![image](https://user-images.githubusercontent.com/92380630/149983266-c73e6535-d1ae-42a2-90c6-9399582494d4.png)

###

## Workshop 8 Topological Navigation 

* Update: `sudo apt-get update && sudo apt-get upgrade`

* Install today's packages: 
    ```
    sudo apt-get install \
        ros-melodic-topological-utils \
        ros-melodic-topological-navigation \
        ros-melodic-topological-navigation-msgs \
        ros-melodic-strands-navigation
    ```
* First, make sure that you have a working copy (fork and clone into your catkin workspace) of the course's repository as described [here](https://github.com/LCAS/CMP9767M/wiki/Workshop-2---ROS-workspaces-and-actual-coding#task-5-code-on-github-or-where-you-want). The tutorial code is included in the `uol_cmp9767m_tutorial` folder. If you have your workspace set up already in the previous workshops, please pull the recent update from the repository as some of the workshop files have been updated recently.

###  Map Demo

In this task, we will run the topological navigation demonstrated in the lecture. You will learn how a topological map is defined, how it is loaded to the database (i.e. MongoDB), and how to make the robot move to different waypoints (nodes) using RVIZ.

1. The topological map for the demo is available in `uol_cmp9767m_tutorial/maps/test.yaml`. Look at this file first, and try to understand how a topological map is specified.
2. Create a folder (named `mongodb`) in your user home directory. MongoDB will store all database files required to run our topological map. This step is required only once.
3. Launch the simulation setup
    - `roslaunch bacchus_gazebo vineyard_demo.launch`
    - `roslaunch uol_cmp9767m_tutorial topo_nav.launch`, if you work with a dockerised distribution (e.g. at home or using a remote access) please use the following line instead which will help to address some issues with the MongoDB database: `HOSTNAME=0.0.0.0 roslaunch uol_cmp9767m_tutorial topo_nav.launch`.
    - You will see some warnings in the terminal where you launched `topo_nav.launch` saying the pointset is not found in the `message_store`. This is because we haven't loaded the topological map to the mongodb yet. Once you do the next step, that warning should stop.
    - `rosrun topological_utils load_yaml_map.py $(rospack find uol_cmp9767m_tutorial)/maps/test.yaml`. This step is required only once.
    - open the topological map visualisation config for RVIZ in `uol_cmp9767m_tutorial/config/topo_nav.rviz`.
    - click the green arrows at the nodes seen in RVIZ to send `topological_navigation` goals to the robot.

Navigate between different nodes and note the robot's behaviour on edges with a different directionality. 

Note: you can also use your own `move_base` setup from the previous workshop. Topological navigation is currently configured to run with the DWA planner, so remember to switch your `base_local_planner` to `dwa_local_planner/DWAPlannerROS` in the `uol_cmp9767m_tutorial/config/planners.yaml`.

### Map Modifications

We have already seen some service calls in the lecture about creating a new topological map directly into MongoDB, rather than loading a map file. In this task, we will use the same service calls to modify the existing topological map we used in Task 1. Please note that to see any new changes made to the map in RVIZ, you have to manually update the map by issuing `rostopic pub /update_map std_msgs/Time "data:
  secs: 0
  nsecs: 0"`.

1. In a terminal, add a node to the map
```
rosservice call /topological_map_manager/add_topological_node "
name: WayPoint6
pose:
  position:
    x: -2.0
    y: -2.0
    z: 0.0
  orientation:
    x: 0.0
    y: 0.0
    z: 0.0
    w: 1.0
add_close_nodes: false"
```
2. Add a uni-directional edge to the new node (`WayPoint6`) from an existing node (`WayPoint0`)
```
rosservice call /topological_map_manager/add_edges_between_nodes "
origin: WayPoint0
destination: WayPoint6
action: move_base
edge_id: WayPoint0_WayPoint6"
```
3. Add a bi-directional edge between the new node (`WayPoint6`) and an existing node (`WayPoint3`)
```
rosservice call /topological_map_manager/add_edges_between_nodes "
origin: WayPoint6
destination: WayPoint3
action: move_base
edge_id: WayPoint6_WayPoint3"
```
```
rosservice call /topological_map_manager/add_edges_between_nodes "
origin: WayPoint3
destination: WayPoint6
action: move_base
edge_id: WayPoint3_WayPoint6"
```
3. Visualise the map in `rviz`. Navigate the robot to the new node.
4. *Optional*: Save the modified map as a yaml file.
```
rosrun topological_utils map_to_yaml.py test $(rospack find uol_cmp9767m_tutorial)/maps/test_mod.yaml
```

### Action Client

In this task, you will create an action client that can send goals to the robot's topological navigation action. 

1. Follow the steps in Task 1 to launch the topological_navigation stack.
2. In another terminal run `rosrun uol_cmp9767m_tutorial set_topo_nav_goal.py` and see what is happening. 
3. Look at the script (uol_cmp9767m_tutorial/scritps/set_topo_nav_goal.py) to see how the goals are sent. 
4. Modify the script to send the robot to the new node added in Task 2.
