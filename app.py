from flask import Flask, render_template, request, send_file
import os
import pandas as pd
from src.sentiment_analyzer import analyze_reviews

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
REPORT_FOLDER = 'reports'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    result_data = None
    summary = None
    download_ready = False

    if request.method == 'POST':
        file = request.files['file']
        if file.filename.endswith('.csv'):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            df = analyze_reviews(filepath)
            result_data = df.to_dict(orient='records')
            summary = df['Sentiment'].value_counts().to_dict()
            download_ready = True

    return render_template('index.html', result=result_data, summary=summary, download_ready=download_ready)

@app.route('/download')
def download_file():
    return send_file('reports/analyzed_reviews.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
