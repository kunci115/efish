FROM python:3.9.4
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY . /code
WORKDIR /code
#RUN ls
RUN pip --default-timeout=1000 install --no-cache-dir -r coreconnect/requirements.txt
#
