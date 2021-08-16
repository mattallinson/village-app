'''Runs everything the same but does not import tensorflow and uses 
boilerplate text, therefore loads very quickly, mostly used for 
checking configs and css during development and debugging
'''

from flask import Flask, render_template, url_for, redirect, session
from waitress import serve

from forms import ParameterForm

# Initialise app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a random string'	

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
		
		'''code below makes 5 new village name and addes them to the
		list of village names, which then gets passed to render_template
		'''

		session['villages'].extend(
			["a funny village name"])

		return render_template("index.html", 
			villages=session['villages'][::-1], #list in reverse order
			form=form)

	return render_template("index.html", 
		villages=session['villages'], 
		form=form)

@app.route("/clear-list", methods=['GET', 'POST'])
def clear_list():
	session.pop('villages')
	return redirect(url_for('index'))

if __name__ == '__main__':
	print("Booted without AI")
	serve(app, host='0.0.0.0', port=5000)