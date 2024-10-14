from flask import Flask

app = Flask(__name__)

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "文件不存在"

@app.route('/')
def send_file_content():
    file_content = read_text_file('text.txt')
    return file_content

if __name__ == '__main__':
    app.run(port=80)
