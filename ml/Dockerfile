# tensorflowがpython3.7に対応していないため3.6を指定
FROM python:3.6-stretch 

RUN pip install --upgrade pip

RUN pip install pillow numpy tensorflow scikit-learn

RUN pip install beautifulsoup4 requests

WORKDIR /app

ENTRYPOINT ["python"]

