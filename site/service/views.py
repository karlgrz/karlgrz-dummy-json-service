import os
from flask import Flask, request, redirect, render_template, url_for, abort, session, send_from_directory, flash, Response, g
import uuid
from werkzeug import secure_filename
import json
import socket
from __init__ import app, logger 
import hashlib

@app.route('/', methods=['GET', 'POST'])
def home():
    hostname = socket.gethostname()
    data = {}
    data['hostname'] = hostname
    data['status'] = 'ok'
    return json.dumps(data)

@app.route('/monitor')
def about():
    return json.dumps({'status':'ok'})
