docker build -t test_image .
docker run --name qqqq test_image
docker rm qqqq
docker rmi test_imag
