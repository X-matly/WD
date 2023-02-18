from wsgiref.validate import validator
import wtforms
from wtforms import IntegerField
from wtforms.validators import length, EqualTo


class jumpForm(wtforms.Form):
    user_ID = wtforms.IntegerField()

