1. Link to repo: https://hub.docker.com/repository/docker/andriy13/lab_4
2. Link to image django: https://hub.docker.com/layers/131415772/andriy13/lab_4/django/images/sha256-63be9f1be85f3a1353c2191c29bdf83a32ea092d4ee879624492de29e3634f5d?context=explore
3. Link to image monitoring: https://hub.docker.com/layers/131416049/andriy13/lab_4/monitoring/images/sha256-0e23dac568ed591034ab481cce449c0951b76a5689438ac71a91530be6dca347?context=explore

4. Using commands: 1)docker -v, 2)docker -h, 3)docker run docker/whalesay cowsay Docker is fun
5. Using commands: 1)docker pull python:3.8-slim, 2)docker images, 3)docker inspect python:3.8-slim
6. Using commands: sudo docker build -t andriy13/lab_4:django ., sudo docker build --file Dockerfile.momitoring -t andriy13/lab_4:monitoring .
7. Using command docker run -it --name=django --rm -p 8000:8000 andriy13/lab_4:django
8. Using command: sudo docker run -it --net=host --name=monitoring --rm -v $(pwd)/server.log:/app/server.log andriy13/lab_4:monitoring 
