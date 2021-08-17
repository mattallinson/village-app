# Village-app
This is a Flask app that turns the AI model built in [English Village Names](https://github.com/mattallinson/english_villages) into a website that is currently being hosted at http://villagebot.xyz.

## Usage
To get the app up and running clone repo, cd and then run `$ bash setup.sh` which should take care of installing all the correct repositories and setting up the secret key. 
Running `$ python app.py` as root will then serve the app at port 80

## Dummy.py
To help test updates with style and layout without having to go through the time-consuming processes of booting up tensorflow each time, `dummy.py` is a boilerplate version of the page which loads the same HTML templates but doesn't have any of the hardcore AI which takes ages to load. It loads very quickly and serves at port 8080

## License
MIT
