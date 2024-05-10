from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/upload_file_and_start_chat', methods=['POST'])
def upload_file_and_start_chat():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):
        filename = 'data.csv'
        file.save((filename))
    else:
        return 'Invalid file format'

@app.route('/chat')
def chat():
    df=pd.read_csv('data.csv')
    columns=df.columns.tolist()
    data_types=df.dtypes.to_dict()
    null_values=df.isnull().sum().to_dict()
    example_data=df.head().to_dict()
    return render_template('chat.html', columns=columns, GEMINI_API_KEY=GEMINI_API_KEY, data_types=data_types, null_values=null_values, example_data=example_data)


@app.route('/send_message', methods=['POST'])
def send_message():
    # Dummy response for demonstration
    user_message = request.form.get('user_message')
    return user_message.upper()  # Echo the message in uppercase

if __name__ == '__main__':
    app.run(debug=True)
