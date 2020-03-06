# https://hub.docker.com/_/python
# The best Docker base image for your Python application (July 2019):
# https://pythonspeed.com/articles/base-image-python-docker-images/
# 
FROM jennerwein/ubuntu-python3

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . /app/

CMD [ "python3", "app.py" ]

