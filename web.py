from flask import Flask, render_template, request

from utils.ner import ner

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	return render_template("index.html")

@app.route('/result', methods=['POST'])
def extract():
	file = request.files['file']
	if file:
		content = file.read().decode('utf-8')
		lines = content.split(".")
		preview_text = ".".join(lines[:10])
	return render_template("result.html", preview_text = preview_text, **ner(content))

if __name__ == '__main__':
	app.run(debug=True)
