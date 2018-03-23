FROM python:3.6
MAINTAINER Brian Curtin <brian@python.org>

WORKDIR /pine
ADD . /pine
RUN pip3 install -r requirements.txt

EXPOSE 6666

CMD ["python", "source/pine/main.py"]
