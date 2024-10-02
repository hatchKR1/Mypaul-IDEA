from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

# 파일에 글 저장하는 함수
def save_post(content, user_ip):
    with open('posts.txt', 'a') as f:
        f.write(f"{user_ip} | {content} | {datetime.now()}\n")

# 파일에서 글 읽어오는 함수
def load_posts():
    posts = []
    try:
        with open('posts.txt', 'r') as f:
            for line in f:
                post = line.strip().split(" | ")
                posts.append({
                    'ip': post[0],
                    'content': post[1],
                    'date': post[2]
                })
    except FileNotFoundError:
        pass
    return posts

# 메인 페이지
@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

# 새 글 작성
@app.route('/new', methods=['POST'])
def new_post():
    content = request.form['content']
    user_ip = request.remote_addr
    save_post(content, user_ip)
    return redirect('/')

if __name__ == '__main__':
    
