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
import bashlex

def identify_stack():
    # This will aid in writing build scripts for the app.
    dbs = ['mysql']
    webserver = ['apache']
    return []


def validate_commands():
    # Parse all the commands and run them inside a base fedora container.
    # Get a list of commands which are available inside the fedora image
    # Those not available will have to be installed
    # and list of commands which are not.
    return []


f = open('owncloud.sh','r')
lines = f.readlines()
for line in lines:
    #print line
    try:
        parts = bashlex.parse(line)
        for ast in parts:
            print ast.parts[0].parts[0].word
    except Exception as e:
        pass

    #print "\n\n"
#print lines
