# Idea

What this installer is trying to achieve?

* Build a base image on fedora image which has required dependences like httpd, php installed.
* Directly execute the install scripts in these containers instead of executing them in host machine.
* The copy on write feature of docker will make sure that even if 100 containers are running use the same base image, the data replication doesn't take place.

## Dockerfile0

This is the file using which the base image will be build. This is not complete in any way.


## Dockerfile

This is the file which will is used to test compatibility of install scripts. 
