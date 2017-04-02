docker build -t vikasy/amahi_base -f Dockerfile0 .
docker run --name qqqq vikasy/amahi_base
docker rm qqqq
docker rmi test_imag
