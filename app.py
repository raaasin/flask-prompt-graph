from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import pandas as pd
from dotenv import load_dotenv
from flask import jsonify


load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_file():
    print("Upload page accessed")
    return render_template('upload.html')

@app.route('/upload_file_and_start_chat', methods=['POST'])
def upload_file_and_start_chat():
    if 'file' not in request.files:
        print("No file part")
        return 'No file part'
    
    file = request.files['file']

    if file.filename == '':
        print("No selected file")
        return 'No selected file'

    if file and allowed_file(file.filename):
        filename = 'data.csv'
        file.save((filename))
        print("File saved successfully")
    else:
        print("Invalid file format")
        return 'Invalid file format'

@app.route('/chat')
def chat():
    print("Chat page accessed")
    df=pd.read_csv('data.csv')
    columns=df.columns.tolist()
    data_types=df.dtypes.to_dict()
    null_values=df.isnull().sum().to_dict()
    example_data=df.head().to_dict()
    GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
    print(GEMINI_API_KEY)
    return render_template('chat.html', columns=columns, GEMINI_API_KEY=GEMINI_API_KEY, data_types=data_types, null_values=null_values, example_data=example_data)

@app.route('/get_image')
def get_image():
    try:
        return send_file('graph.png', mimetype='image/png')
    except Exception as e:
        return str(e)
    
@app.route('/execute_code', methods=['POST'])
def execute_code():
    #print request data
    data = request.json
    code = data['code']
    try:
        print(code)
        exec(code)
        print("Code executed successfully")
        #return data.message as 'graph.png'
        return jsonify(message='graph.png')

    except Exception as e:
        #return jsonified error message
        print("Error executing code:", str(e))
        return jsonify(message=str(e))

if __name__ == '__main__':
    app.run()
