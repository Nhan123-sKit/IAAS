from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TRANSLATE_API_URL = 'https://api.mymemory.translated.net/get'

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ''
    if request.method == 'POST':
        text = request.form['text']
        source_language = request.form['source_language']
        target_language = request.form['target_language']
        
        params = {
            "q": text,
            "langpair": f"{source_language}|{target_language}"
        }
        response = requests.get(TRANSLATE_API_URL, params=params)
        
        if response.status_code == 200:
            translated_text = response.json()['responseData']['translatedText']
        else:
            translated_text = 'Lỗi khi dịch văn bản.'
    
    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)