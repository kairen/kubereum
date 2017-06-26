FROM alpine:3.5
MAINTAINER Kyle Bai(kyle.b@inwinstack.com)

RUN  apk add --no-cache python ca-certificates curl && \
  python -m ensurepip && \
  rm -r /usr/lib/python*/ensurepip && \
  pip install -U requests && \
  rm -r /usr/lib/python2.7/site-packages/pip /usr/bin/pip && \
  rm -r /root/.cache

COPY auto_peer.py /etc/auto_peer.py
