# Idea

What this installer is trying to achieve?

* Build a base image on fedora image which has required dependences like httpd, php installed.
* Directly execute the install scripts in these containers instead of executing them in host machine.
* The copy on write feature of docker will make sure that even if 100 containers are running use the same base image, the data replication doesn't take place.

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
