FROM python:3.7.3-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /product-app
WORKDIR /product-app
RUN chmod +x boot.sh


ENTRYPOINT ["./boot.sh"]