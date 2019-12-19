# -*- coding:utf-8 -*-
from flask import Blueprint
import sys
sys.path.append(".")
main = Blueprint('main', __name__)

from . import views, errors