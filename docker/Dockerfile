FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN useradd -ms /bin/bash app

RUN apt-get update \
    && apt-get install -y netcat \
    && apt-get -y autoremove \
    && rm -rf /var/cache/apt/archives/*

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY --chown=app:app requirements.txt /requirements.txt

USER app
ENV PATH="/home/app/.local/bin:$PATH"
RUN pip3 install --no-cache-dir -U pip setuptools
RUN pip3 install --no-cache-dir -r /requirements.txt

COPY . .

EXPOSE 8080

COPY ./docker/docker-entrypoint.sh /entrypoint/docker-entrypoint.sh
ENTRYPOINT ["/entrypoint/docker-entrypoint.sh"]