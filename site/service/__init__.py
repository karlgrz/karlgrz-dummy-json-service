import os
from flask import Flask, request, redirect, render_template, url_for, abort, session, send_from_directory, flash, Response, g
import uuid
import json
import logging

logger = logging.getLogger('web')
file_handler = logging.FileHandler('log/web.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

logger.debug(__name__)

app = Flask(__name__)
app.secret_key = 'dummy-secret-key' 

from views import *
