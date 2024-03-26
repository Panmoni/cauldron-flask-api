docker images
docker ps -a

docker build -t my-flask-app .
docker run -p 8000:8000 my-flask-app
