FROM python:alpine
ARG DEVCACHE_HOST
ARG DEVCACHE_PORT
ENV DEVCACHE_HOST=0.0.0.0
ENV DEVCACHE_PORT=8001
RUN mkdir -p /srv/app
COPY server /srv/app/server
COPY cache /srv/app/cache
COPY devcache.py /srv/app
WORKDIR /srv/app
CMD ["python3","/srv/app/devcache.py"]
