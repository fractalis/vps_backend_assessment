FROM alpine:latest

RUN apk add --update --no-cache python3 python3-dev gcc g++ && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools wheel

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

COPY vps_backend_assessment/ ./vps_backend_assessment/

CMD ["python", "-m", "vps_backend_assessment"]