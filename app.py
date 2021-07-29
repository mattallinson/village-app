from flask import Flask, render_template, url_for, redirect
from forms import ParameterForm
from textgenrnn import textgenrnn

def village_maker(temperature=1.0, prefix=None):
	textgen = textgenrnn('villages_4e.hdf5') # imports weights
	villages = textgen.generate(5, temperature=temperature, prefix=prefix, 
		return_as_list=True)
	return villages

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a random string'
villages=[]	

@app.route("/", methods=['GET', 'POST'])
def index():
	form = ParameterForm()
	if form.validate_on_submit():
		user_prefix = form.prefix.data.title()
		user_temperature = float(form.temperature.data)
		villages.extend(
			village_maker(temperature=user_temperature, prefix=user_prefix))
		#fun fact, you can't use += when using a function to add to a list from outside
		#the function, you have use 'extend'
		return render_template("base.html", villages=villages[::-1], form=form)
	return render_template("base.html", villages=villages, form=form)

if __name__ == '__main__':
	app.run()