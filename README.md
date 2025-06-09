# メモ帳アプリ (Flask + Docker)

シンプルなWebベースのメモ帳アプリケーションです。FlaskフレームワークとDockerを使用して構築されています。

## 機能

- ✏️ メモの作成
- 📋 メモの一覧表示
- 🗑️ メモの削除
- 💾 データの永続化
- 🌐 日本語対応

## デモ

![メモ帳アプリ](https://via.placeholder.com/800x400?text=メモ帳アプリのスクリーンショット)

## クイックスタート

### Docker Hubから実行

最も簡単な方法は、Docker Hubから直接イメージを取得して実行することです：

```bash
docker run -p 5000:5000 katzkawai/memo-app:latest
```

ブラウザで http://localhost:5000 にアクセスしてください。

## 詳細な起動方法

### 1. 基本的な起動

```bash
# イメージを取得
docker pull katzkawai/memo-app:latest

# コンテナを実行
docker run -p 5000:5000 katzkawai/memo-app:latest
```

### 2. バックグラウンドで実行

```bash
docker run -d -p 5000:5000 --name my-memo-app katzkawai/memo-app:latest
```

### 3. データを永続化して実行

メモデータをコンテナの再起動後も保持したい場合：

```bash
# データ保存用ディレクトリを作成
mkdir -p ./memo-data
echo '[]' > ./memo-data/notes.json

# ボリュームマウントで実行
docker run -d -p 5000:5000 \
  -v $(pwd)/memo-data/notes.json:/app/notes.json \
  --name memo-app-persistent \
  katzkawai/memo-app:latest
```

### 4. 別のポートで実行

```bash
# ポート8080で実行
docker run -d -p 8080:5000 katzkawai/memo-app:latest
```

この場合は http://localhost:8080 でアクセスします。

## ローカルでのビルドと実行

### リポジトリのクローン

```bash
git clone https://github.com/katzkawai/docker-flask.git
cd docker-flask
```

### Dockerイメージのビルド

```bash
docker build -t memo-app .
```

### ローカルイメージから実行

```bash
docker run -p 5000:5000 memo-app
```

### Dockerを使わない実行方法

```bash
# 依存関係のインストール
pip install -r requirements.txt

# アプリケーションの実行
python app.py
```

## コンテナの管理

### コンテナの確認

```bash
docker ps
```

### コンテナの停止

```bash
docker stop <container-name>
```

### コンテナの削除

```bash
docker rm <container-name>
```

### ログの確認

```bash
docker logs <container-name>
```

## 技術仕様

### 使用技術

- **バックエンド**: Flask 3.0.3 (Python 3.8)
- **フロントエンド**: HTML5, CSS3 (レスポンシブデザイン)
- **データ保存**: JSON ファイル
- **コンテナ化**: Docker
- **ベースイメージ**: python:3.8

### プロジェクト構成

```
docker-flask/
├── app.py                 # Flaskアプリケーション本体
├── requirements.txt       # Python依存関係
├── Dockerfile            # Dockerイメージ定義
├── templates/            # HTMLテンプレート
│   └── index.html       # メイン画面
├── CLAUDE.md            # 開発者向けドキュメント
├── README.md            # このファイル
└── .gitignore           # Git除外設定
```

### API エンドポイント

| メソッド | パス | 説明 |
|---------|------|------|
| GET | `/` | メモ一覧画面を表示 |
| POST | `/add` | 新しいメモを追加 |
| GET | `/delete/<id>` | 指定IDのメモを削除 |

### データ形式

メモデータは以下のJSON形式で保存されます：

```json
[
  {
    "id": 1,
    "content": "メモの内容",
    "created_at": "2025-06-09 20:52:04"
  }
]
```

### 環境変数

現在のバージョンでは環境変数は使用していません。

### ポート

- コンテナ内部: 5000
- ホスト側: 任意（デフォルト: 5000）

## セキュリティに関する注意

- このアプリケーションは開発/学習用です
- 本番環境での使用には適切なセキュリティ対策が必要です
- デバッグモードは本番環境では無効にしてください

## トラブルシューティング

### ポートが既に使用されている場合

```bash
# 別のポートで実行
docker run -p 8080:5000 katzkawai/memo-app:latest
```

### データが保存されない場合

ボリュームマウントを使用してデータを永続化してください（上記「データを永続化して実行」参照）。

### コンテナが起動しない場合

```bash
# ログを確認
docker logs <container-name>
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 作者

- GitHub: [@katzkawai](https://github.com/katzkawai)
- Docker Hub: [katzkawai/memo-app](https://hub.docker.com/r/katzkawai/memo-app)

## 貢献

プルリクエストは歓迎します。大きな変更の場合は、まずイシューを作成して変更内容を議論してください。