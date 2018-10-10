from flask import Flask

app = Flask(__name__)

from app import routes #akin to django urls.py
