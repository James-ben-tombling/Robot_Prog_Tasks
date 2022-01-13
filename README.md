# Robot_Prog_Tasks 
LCAS Robot programming task from the workshop UoL <br />
## how to start my ROS 
$ sudo apt-get update && sudo apt-get upgrade  <br />
$ sudo apt-get install ros-melodic-uol-cmp9767m-base ros-melodic-desktop  <br />
$ source /opt/ros/melodic/setup.bash  <br />
$ roslaunch bacchus_gazebo vineyard_demo.launch world_name:=vineyard_small  <br />
$ if thats fails try sudo apt-get purge "*gazebo*" then step 3 again   <br />

for ease just name your workspace catkin_ws but up to you i dont care.

make a work space for a package  <br />
$ mkdir -p ~/<my_ws>/src  <br />
$ cd ~/<my_ws>/  <br />
$ catkin_make  <br />

## Workshop 2
go to your newly made work space (ws)  <br />
$ cd ~/<my_ws>/src  <br />
for making a package turtorial use   <br />
$ catkin_create_pkg beginner_tutorials std_msgs rospy roscpp  <br />
this can be anything just fill in the zones of below (dont copy)  <br />
$ catkin_create_pkg <package_name> [depend1] [depend2] [depend3]  <br />
in every new terminal you want to use your package you must source as follows  <br />
$ source ~/<my_ws>/devel/setup.bash  <br />
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
    
close all terminal and start a new one 

$ source ~/catkin_ws/devel/setup.bash <br />
$ roscd workshops  <br />
$ cd scripts <br />

then use:
$ code ThorvaldMover.py <br />
or < br />


### lets add our new tf listener 

start her baby 

$ source /opt/ros/melodic/setup.bash <br />
$ roslaunch bacchus_gazebo vineyard_demo.launch world_name:=vineyard_small  <br />

then again ina new terminal 
