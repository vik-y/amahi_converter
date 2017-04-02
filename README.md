# Idea

What this installer is trying to achieve?

* Build a base image on fedora image which has required dependences like httpd, php installed.
* Directly execute the install scripts in these containers instead of executing them in host machine.
* The copy on write feature of docker will make sure that even if 100 containers are running use the same base image, the data replication doesn't take place.

How it works?

The fedora image available on docker hub is the skimmed out version of original fedora from which has bare minimum softwares installed in it. The motivation here is to build our own image from that fedora image which has all dependencies relevant to us pre-installed. 

Dockerfile0 tries to generate a base image with all those dependencies. (and is not compmlete at all..just an idea).
In future this can also ask for specific versions of each software that you want (e.g Php 7, Mysql 5.6, etc), that way application specific base images can be made if the need be. 

Once the base image is ready we run a python script (convert.py) to parse the install script of the application and run inside the base image. The script will run inside the base container and try to identify the commands which might create an issue for the user. Most install scripts will execute without much issues (as per my assumption), and many might fail. This python script can be hardened enough to identify failures so that the install scripts can be modified manually as needed. 


That was part 1 of the idea. 

Part 2 is to take a new approach and not use install scripts at all. 
The idea here is to take as input the application specific requirements from the admin along with the source code of the application to be installed and generate a docker-compose.yml file for it. 

## Dockerfile0

This is the file using which the base image will be build. This is not complete in any way.


## Dockerfile

This is the file which will is used to test compatibility of install scripts.

## convert.py
Idea is that this file will parse the config file, and test if the commands mentioned in the script are available in the base container. If not what are the missing commands.
Developing it a little further can help in understanding which if running the install scripts will require any change in the environment.

## Moving forward.

Each install script can be packaged with information like:
* What stack do they use? e.g. apache+php+mysql along with their versions.
* A base image with those stacks in place can be provisioned and then install scripts can be run on those base image to install the apps.
* This will require testing with multiple install scripts. Right now I have tested only with owncloud.



PLEASE NOTE THAT THIS IS AN IDEA OF THE PROTOTYPE AND IS NOT COMPLETE IN ANY WAY.
