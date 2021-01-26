FROM debian:stable-slim
LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-sqlite3"
LABEL version="latest"

RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get -yq --no-install-recommends install sqlite3=3.* && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
	mkdir -p /root/events_api

WORKDIR /root/events_api
ENTRYPOINT [ "sqlite3" ]
