FROM vikasy/amahi_base
MAINTAINER Vikas Yadav

RUN mkdir /home/test

ADD convert.py /home/test/convert.py
ADD owncloud.sh /home/test/owncloud.sh
RUN chmod a+x
RUN cd /home/test
WORKDIR "/home/test"
CMD ["python", "convert.py"]
