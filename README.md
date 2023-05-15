# What is this repository?

気軽にグラフをプロットするときに使う．

Dockerでホスト環境を汚さずに使える．ホストとコンテナ内でファイル共有(≒ボリューム)を行っているため，「コンテナ内でプロット→ホストでグラフ画像をチェックする」ができる．

# Quick Start

イメージを取得&ビルド
```
    docker compose up -d
```

グラフプロットをするコンテナ(pythonがインストールしてある)に入る

```
    docker container exec -it con_plotter bash
```


コンテナ中でプロットプログラムを動かす
```
    python sin_plot.py
```

コンテナから出る: Control+D

コンテナを終了
```
    Docker compose down
```