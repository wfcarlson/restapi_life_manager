# base image
FROM python:2.7.15
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
RUN set -ex; apt-get update; apt-get install -y software-properties-common; add-apt-repository -y non-free; apt-get update; apt-get -y install flac ffmpeg lame vorbis-tools faac faad


RUN mkdir /code/
WORKDIR /code/
ADD . /code/
RUN python manage.py migrate


EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]