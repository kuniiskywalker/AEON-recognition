# tensorflowがpython3.7に対応していないため3.6を指定
FROM python:3.6-stretch 

RUN pip install --upgrade pip

# numpy 1.16.1から1.16.3になる際にallow_pickle=Falseがデフォルトになったため1.16.1を指定
RUN pip install pillow numpy==1.16.1 tensorflow

WORKDIR /app

ADD app.py /app/

CMD ["python", "app.py"]
