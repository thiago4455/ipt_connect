FROM python:2

ADD entrypoint.sh /entrypoint.sh
ADD requirements.txt requirements.txt

RUN \
    chmod +x /entrypoint.sh && \
    apt-get update && \
    apt-get install -y --no-install-recommends gettext && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
