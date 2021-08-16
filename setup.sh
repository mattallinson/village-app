# Get pip and venv up and running, and install venv
apt install python3.8-venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

# Install textgenrnn, correct for weird dependencies
pip3 install git+git://github.com/minimaxir/textgenrnn.git
pip3 install h5py~=3.1.0
pip3 install numpy~=1.19.2

# Get everything for flask installed
pip3 install waitress
pip3 install flask
pip3 install flask_wtf

# Creates Secret Key and stores it 
echo $(openssl rand -base64 12) >> secretKey
echo "Good Luck!"