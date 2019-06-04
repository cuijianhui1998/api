from flask import Blueprint


web = Blueprint('web',__name__)

from app.web import movie
from app.web import league
from app.web import other
from app.web import anchor