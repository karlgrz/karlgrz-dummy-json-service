#!/bin/bash

cd /srv
uwsgi --http 0.0.0.0:8888 --module service --callable app --enable-threads
