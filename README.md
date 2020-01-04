AEON recognition
====

This app is a person who estimates which store from the appearance of AEON of Japanese supermarket.

## Demo

[DEMO LINK](https://aeon-recognition.herokuapp.com/)

![demo](https://github.com/kuniiskywalker/AEON-recognition/blob/master/demo.png?raw=true "sample")

## Requirement

- Docker

## Structure

```
.
├── api
│   ├── Dockerfile
│   ├── Makefile
│   ├── README.md
│   └── app
│       ├── templates
│       │    └── index.html
│       │
│       ├── main.py
│       ├── stores.json
│       └── vgg16_transfer.h5
├── ml
│   ├── configs
│   │    └── stores.json
│   ├── data
│   │    ├── processed
│   │    └── raw
│   ├── models
│   ├── src
│   │    ├── data
│   │    │    └── make_datase.py
│   │    ├── features
│   │    │    └── build_features.py
│   │    └── models
│   │         ├── predict_model.py
│   │         └── train_model.py
│   ├── Dockerfile
│   ├── Makefile
│   └── README.md
├── README.md
└── train_history.md
```

## Author

[kuniiskywalker](https://github.com/kuniiskywalker)