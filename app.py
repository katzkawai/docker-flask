# 必要なモジュールのインポート
from flask import Flask, render_template, request, redirect, url_for
import os
import json
from datetime import datetime

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# メモデータを保存するJSONファイルのパス
NOTES_FILE = 'notes.json'

def load_notes():
    """保存されているメモをJSONファイルから読み込む関数"""
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_notes(notes):
    """メモのリストをJSONファイルに保存する関数"""
    with open(NOTES_FILE, 'w', encoding='utf-8') as f:
        # ensure_ascii=Falseで日本語をそのまま保存
        json.dump(notes, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """トップページを表示する関数（メモ一覧表示）"""
    notes = load_notes()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    """新しいメモを追加する関数"""
    # フォームから送信されたメモの内容を取得
    content = request.form.get('content')
    if content:
        # 既存のメモを読み込み
        notes = load_notes()
        # 新しいメモのデータを作成
        note = {
            'id': len(notes) + 1,
            'content': content,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        # メモリストに追加して保存
        notes.append(note)
        save_notes(notes)
    # トップページにリダイレクト
    return redirect(url_for('index'))

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    """指定されたIDのメモを削除する関数"""
    # 既存のメモを読み込み
    notes = load_notes()
    # 指定されたID以外のメモだけを残す
    notes = [note for note in notes if note['id'] != note_id]
    # 更新されたリストを保存
    save_notes(notes)
    # トップページにリダイレクト
    return redirect(url_for('index'))

if __name__ == '__main__':
    # アプリケーションを起動
    # host='0.0.0.0'で全てのIPアドレスからアクセス可能
    # port=5000でポート5000を使用
    # debug=Trueで開発モード（自動リロードとデバッグ情報表示）
    app.run(host='0.0.0.0', port=5000, debug=True)