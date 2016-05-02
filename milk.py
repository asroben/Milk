import os

from flask import Flask, url_for, request, render_template

messages_dir = '/home/ubuntu/workspace/flask_init/static/messages'

# Create an instance of the Flask Class
app = Flask(__name__)

@app.route('/voice')
@app.route('/home')
def index():
    music_files = [f for f in os.listdir(messages_dir) if f.endswith('wav')]
    music_files_number = len(music_files)
    print(music_files, music_files_number)
    return render_template("main_menu.xml",
                        title = 'Home',
                        music_files_number = music_files_number,
                        music_files = music_files)


# if run from the terminal, define cloud9 host and port
if __name__ == '__main__':
    # Below items are not needed if running on a linux machine, just for Cloud9
    host = os.getenv('IP', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)

 