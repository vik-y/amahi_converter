FROM fedora_python
MAINTAINER Vikas Yadav

RUN mkdir /home/test

ADD convert.py /home/test/convert.py
ADD owncloud.sh /home/test/owncloud.sh

RUN cd /home/test
CMD ["python", "/home/test/convert.py"]
