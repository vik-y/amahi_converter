docker kill $(docker ps -q)
docker rm $(docker ps -a -q)
docker rmi vikasy/amahi_owncloud
