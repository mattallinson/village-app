from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.fields.html5 import DecimalRangeField

class ParameterForm(FlaskForm):
	prefix = StringField('Prefix (optional)')
	temperature = DecimalRangeField('Temperature', 
		default=1.0)
	submit = SubmitField('Make village names')