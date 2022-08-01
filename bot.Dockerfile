# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /bot
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#COPY download_models.sh download_models.sh
#RUN bash download_models.sh

COPY . .
CMD ["bash", "send.sh"]
