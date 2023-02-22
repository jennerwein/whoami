# My image with python, pip3, iproute2, curl, vim ...
# https://hub.docker.com/repository/docker/jennerwein/ubuntu-python3/general
FROM jennerwein/ubuntu-python3:v1.2.2

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY ./app /app/
EXPOSE 80/tcp

CMD [ "python3", "app.py" ]

