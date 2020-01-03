FROM python:3.6-stretch

# 環境変数を設定する
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn email-validator python-multipart Jinja2
RUN pip install pillow numpy tensorflow

EXPOSE 80

COPY ./app /app

CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT
