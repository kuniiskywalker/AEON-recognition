# Docker Hubにあるpythonイメージをベースにする
FROM python:3.6-stretch

# 環境変数を設定する
ENV PYTHONUNBUFFERED 1

# コンテナ内にcodeディレクトリを作り、そこをワークディレクトリとする
RUN mkdir /code
WORKDIR /code

RUN pip install --upgrade pip

# ホストPCにあるrequirements.txtをコンテナ内のcodeディレクトリにコピーする
# コピーしたrequirements.txtを使ってパッケージをインストールする
ADD requirements.txt /code/
RUN pip install -r requirements.txt

RUN pip install pillow numpy tensorflow

# ホストPCの各種ファイルをcodeディレクトリにコピーする
ADD . /code/
