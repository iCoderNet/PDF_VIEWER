import sys
import os
from flask import Flask, redirect, request, send_from_directory
import webview
import threading

# PyInstaller'da ishlayotganimizni aniqlash uchun
def resource_path(relative_path):
    """ Fayllarni to'g'ri yo'lda ochish uchun resurs yo'lini aniqlaydi """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller tomonidan o'rnatilgan joy
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)

app = Flask(__name__, static_folder=resource_path('static'))

@app.route('/')
def index():
    return redirect('/static/file.pdf')

@app.route('/videos')
def videos():
    page = request.args.get('page', 1)

    video_thread = threading.Thread(
        target=open_video_window, 
        args=("Simple Penetration Testing Tutorial for Beginners!", "http://127.0.0.1:5669/static/pentesting.mp4")
    )
    video_thread.start()

    return redirect(f'/static/file.pdf#page={page}&zoom=fitwidth')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

def run_flask():
    app.run(debug=True, port=5669, use_reloader=False)

def open_video_window(title, url):
    webview.create_window(title, url)
    webview.start()

def open_main_window():
    webview.create_window("Aparat xavfsizligi - Mustaqil ish", "http://127.0.0.1:5669", maximized=True)
    webview.start()

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    open_main_window()
