FROM python:3.9.2-slim-buster
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
RUN apt -qq update && apt -qq install -y git wget pv jq wget python3-dev ffmpeg mediainfo
COPY . .
RUN pip3 install -r requirements.txt
ENV PORT = 8080 
EXPOSE 8080
CMD ["bash","run.sh"]