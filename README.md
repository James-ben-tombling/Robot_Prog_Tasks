# Robot_Prog_Tasks
LCAS Robot programming task from the workshop UoL
## how to start my ROS
1. sudo apt-get update && sudo apt-get upgrade
2. source /opt/ros/melodic/setup.bash
3. roslaunch bacchus_gazebo vineyard_demo.launch world_name:=vineyard_small
4. if thats fails try sudo apt-get purge "*gazebo*" then step 3 again 

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



