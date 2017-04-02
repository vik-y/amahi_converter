'''
Prepare a base fedora image for testing the install scripts

docker pull fedora
docker run -it fedora /bin/bash

Install python inside the container.

dnf install python2.7

Commit the changes to this image.

Create a Dockerfile.
Copy the install_script and the test python script in container and run the tests there.

'''
import re, os, yaml
import bashlex, subprocess

# Incomplete
def identify_stack():
    # This will aid in writing build scripts for the app.
    dbs = ['mysql']
    webserver = ['apache']
    return []

# Incomplete
def validate_commands():
    # Parse all the commands and run them inside a base fedora container.
    # Get a list of commands which are available inside the fedora image
    # Those not available will have to be installed
    # and list of commands which are not.
    return []

# A helper class to store a service 
class Service:
    def __init__(self, name='', image='', cname='', volumes=[], environment=[]):
        self.name = name
        self.image = image
        self.cname = cname
        self.volumes = volumes
        self.environment = environment

    # Return a yaml of this service
    def get_dict(self):
        data ={self.name :
                {
                    'image': self.image,
                    'container_name': self.cname,
                    'volumes': self.volumes,
                    'environment' : self.environment
                }
        }
        print yaml.dump(data, default_flow_style=False)
        return data


# Extract all commands in the install script
# currently using bashlex parser
# Can be modified to handle complex scripts 
# Returns a list of commands 
def get_commands(lines):
    # Return a list of all commands in the program
    commands = []
    for line in lines:
        #print line
        try:
            parts = bashlex.parse(line)
            for ast in parts:
                c = ast.parts[0].parts[0].word
                if c not in commands:
                    commands.append(c)
        except Exception as e:
            pass
    return commands

# A helper function to test if a command is valid or not
# returns True if valid False if not valid
def test_command(command):
    global prohibited
    if command not in prohibited:
        print "Testing:", command
        try:
            subprocess.call([command])
            #print "Successful"
            return True
        except OSError as e:
            #if e.errno == os.errno.ENOENT:
            #    print "Something"
            #else:
                # Something else went wrong while trying to run `wget`
            #    raise
            return False
    return True

f = open('owncloud.sh','r')
lines = f.readlines()
commands = get_commands(lines)
prohibited = ['cd', 'export']

# for command in commands:
#     if test_command(command):
#         print command, ":::::" ,"Successful"

# Define all the services here

# Example definition of services
mysql = Service(name='mysql', image='mysql', cname='mysqldb', volumes=[{'./data':'/var/lib/mysql'}], environment=['ROOT_PASS=123'])
apache = Service(name="apache", image='fedora/apache', cname='fedora_apache', volumes=[{}], environment=[''])

mysql.get_dict()
apache.get_dict()

# TODO: Make a list of all the services.
# Read the config file and identify the services required.
# Based on that generate a docker-compose file along with a build scripts
# The build script will just run amahi installer script inside the container
# Test if that script will work without any issues or not. 
