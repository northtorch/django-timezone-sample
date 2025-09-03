# django-timezone-sample

DjangoとPostgresのタイムゾーン設定による動作の違いを確認するためのサンプルプロジェクト
Django上でDateTimeFieldを持つmodelについて、作成直後およびDBから読込直後に、対象のフィールドがどのようなタイムゾーン情報を持つかをダンプする

## 動作環境

- Windows WSL2 ( Ubuntu 24.04LTS )上での動作を想定  
  それ以外の環境の場合、セットアップ手順のコマンド等を適宜読みかえること
  ※参考URL https://learn.microsoft.com/ja-jp/windows/wsl/install
- Docker Desktopインストール済み
  ※参考URL https://docs.docker.jp/desktop/install/windows-install.html

## 使用方法

1. 実験環境用に環境変数を整える

    .envファイルを編集する
    詳細は[.envファイルの設定項目](#envファイルの設定項目)を参照

2. 実験用のコマンドを実行する

    ```bash
    $ docker compose up -d --build
    $ bash run_check_timezone.sh
    $ docker compose down -v
    ```

    .envの設定に沿った実行結果が出力される

## .envファイルの設定項目

| 設定項目 | 用途 | 備考 |
| :-- | :-- | :-- |
| DJANGO_USE_TZ | Djangoに設定する USE_TZ の値 | |
| DJANGO_TIME_ZONE | Djangoに設定する TIME_ZONE の値 | |
| POSTGRES_DB | PostgreSqlで作成するデータベース名 | |
| POSTGRES_USER | PostgreSqlで作成するユーザ名 | |
| POSTGRES_PASSWORD | PostgreSqlで作成するユーザのパスワード | |
| POSTGRES_HOST | PostgreSqlをホストするサービス名 | |
| POSTGRES_PORT | PostgreSql接続用のポート番号 | |
| TZ | PostgreSqlに設定するタイムゾーン | |
