FROM python:3.9.2-slim-buster
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
RUN apt -qq update && apt -qq install -y git wget pv jq wget python3-dev ffmpeg mediainfo
RUN python -m pip install --upgrade pip
COPY . .
EXPOSE 80
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]