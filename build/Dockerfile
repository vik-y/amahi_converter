FROM vikasy/amahi_base
MAINTAINER Vikas Yadav

WORKDIR /var/www/html
COPY v9.0.8.tar.gz /var/www/html/v9.0.8.tar.gz

ADD owncloud.sh /var/www/html/owncloud.sh
RUN chmod a+x owncloud.sh

RUN ./owncloud.sh
CMD ["/run-apache.sh"]
