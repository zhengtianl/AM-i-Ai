from flask import Flask, send_file
from gtts import gTTS
import os

app = Flask(__name__)

def text_to_audio(text, output_filename):
    tts = gTTS(text=text, lang='en')  # 可以根据需要调整语言
    tts.save(output_filename)

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "文件不存在"

@app.route('/')
def send_file_content():
    text = read_text_file('text.txt')
    audio_filename = "output.wav"
    text_to_audio(text, audio_filename)
    return send_file(audio_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(port=80)