FROM karlgrz/ubuntu-14.04-base-flask
VOLUME ["/var/www/service/log/"]
EXPOSE 8888

ADD site /srv

CMD ["/srv/start.sh"]
