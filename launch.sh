#!/usr/bin/env bash

killall -s INT uwsgi
uwsgi -ini uwsgi.ini

systemctl restart nginx
