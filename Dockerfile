# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /scrapy
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
EXPOSE 6800
CMD ["bash", "crawl.sh"]
