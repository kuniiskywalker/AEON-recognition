AEON recognition
====

This app is a person who estimates which store from the appearance of AEON of Japanese supermarket.

## Demo

[DEMO LINK](https://aeon-recognition.herokuapp.com/)

![demo](https://github.com/kuniiskywalker/AEON-recognition/blob/master/demo.png?raw=true "sample")

## Requirement

- Docker

## Usage

VGG16 transfer learning model！

### 1. Build docker image

```
docker build -t aeon-recognition-ml .
```

### 2. Generate dataset

```
docker run --rm -v $(PWD):/app -t aeon-recognition-ml src/features/build_features.py
```

### 3. Train

#### On Docker
```
docker run --rm -v $(PWD):/app -t aeon-recognition-ml src/models/predict_model.py
```

### 4.  Predict on comannd line

#### Reference
```
docker run --rm -v $(PWD):/app -t aeon-recognition-ml src/models/predict_model.py -m {model path} -s {image size} -i {input file}
```

#### Exmaple

```
docker run --rm -v $(PWD):/app -t aeon-recognition-ml src/models/predict_model.py -m models/vgg16_transfer.h5 -s 224 -i data/tests/takahagi.jpg
```

## Author

[kuniiskywalker](https://github.com/kuniiskywalker)
