# My image with python, pip3, iproute2, curl, vim ...
FROM jennerwein/ubuntu-python3

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY ./app /app/
EXPOSE 80/tcp

CMD [ "python3", "app.py" ]

