from flask import Flask
from flask import render_template
from flask import request
from urllib.parse import urlparse
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mock():
	if request.method == 'POST':
	    url = request.form['url']
	    paurl = urlparse(url)
	    if paurl.netloc != '':
	        return render_template('index.html',url=url)	
	    else:
	        return render_template('index.html',url='Invalid URL')	
	else:
		return render_template('index.html')
    
