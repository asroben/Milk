import os, datetime, time
import path

from path import path
from flask import Flask, url_for, request, redirect, render_template
# from werkzeug import secure_filename

UPLOAD_FOLDER = '/var/www/KasaDaka/FlaskKasadaka/templates/flask_init/static/messages'
ALLOWED_EXTENSIONS = set(['wav'])

messages_dir = '/var/www/KasaDaka/FlaskKasadaka/templates/flask_init/static/messages'

# Create an instance of the Flask Class
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Utility to check received messages are in the correct format
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/voice')
@app.route('/home')
def index():
    # #Change the DAYS based on farmer feedback
    # DAYS = 5
    # removed = 0
    # d = path(messages_dir)
    # time_in_secs = time.time() - (DAYS * 24 * 60 * 60)
   
    # # For each file in messages directory check if it should be removed
    # for i in d.walk():
    #     print(time.ctime(os.path.getmtime(i)))
    #     if i.isfile():
    #         # If file is older than DAYS, remove it
    #         if i.mtime <= time_in_secs:
    #             i.remove()
    #             removed += 1
    # print(removed)
    return render_template("main.xml")

@app.route('/voice/english')
def english():
    message_files = [f for f in os.listdir(messages_dir) if f.endswith('wav')]
    message_files_number = len(message_files)
    return render_template("english.xml", message_files_number = message_files_number,
                        message_files = message_files)



# Receive recordings, save them with appropriate name, and render xml
@app.route('/voice/recording', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['message']
        if file and allowed_file(file.filename):
            filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".wav"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('recording_received.xml')
    return render_template('not_recorded.xml')

# if run from the terminal, define cloud9 host and port
if __name__ == '__main__':
    # Below items are not needed if running on a linux machine, just for Cloud9
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)

 