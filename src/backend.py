from flask import Flask, send_from_directory
from gtts import gTTS
import os

app = Flask(__name__)

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "文件不存在"

def text_to_audio(text, output_filename):
    if not text:
        raise ValueError("No text provided for audio conversion.")
    tts = gTTS(text=text, lang='en')  # 可以根据需要调整语言
    tts.save(output_filename)

@app.route('/')
def send_file_content():
    file_content = read_text_file('text.txt')
    if file_content == "文件不存在":
        return "无法找到有效的文本内容进行音频转换。", 404
    audio_filename = "output.wav"
    text_to_audio(file_content, audio_filename)
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), audio_filename, as_attachment=True)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(port=80)