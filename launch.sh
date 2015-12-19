#!/usr/bin/env bash

uwsgi -ini uwsgi.ini

systemctl restart nginx
