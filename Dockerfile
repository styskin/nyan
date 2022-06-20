# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /scrapy
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY channels.json channels.json
COPY configs configs
COPY crawler crawler
COPY scrapy.cfg scrapy.cfg
COPY crawl.sh crawl.sh
EXPOSE 6800
CMD ["bash", "crawl.sh"]
