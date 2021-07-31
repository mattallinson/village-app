from flask import Flask, render_template, url_for, redirect, session
from forms import ParameterForm
from waitress import serve
from textgenrnn import textgenrnn


def village_maker(textgen, temperature=1.0, prefix=None):
	villages = textgen.generate(5, temperature=temperature, prefix=prefix, 
		return_as_list=True)
	return villages

# Initialises 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a random string'	
textgen = textgenrnn('villages_4e.hdf5') # imports weights

@app.route("/", methods=['GET', 'POST'])
def index():
	# Makes blank list of villages
	if 'villages' in session:
		session['villages'] = session.get('villages')
	else:
		session['villages'] = []

	form = ParameterForm()

	if form.validate_on_submit():
		user_prefix = form.prefix.data.title()
		user_temperature = float(form.temperature.data)
		session['villages'].extend(
			village_maker(textgen, temperature=user_temperature, prefix=user_prefix))

		return render_template("base.html", 
			villages=session['villages'][::-1], #list in reverse order
			form=form)

	return render_template("base.html", 
		villages=session['villages'], 
		form=form)

if __name__ == '__main__':
	serve(app, host='0.0.0.0', port=5000)