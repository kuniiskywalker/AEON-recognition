AEON recognition
====

Image recognition of the appearance of super "AEON" in Japan

## Demo

![デモ](https://github.com/kuniiskywalker/AEON-recognition/blob/master/demo.png?raw=true "サンプル")

## Requirement

- Docker

## Structure

```
.
├── README.md
├── app
│   ├── Dockerfile
│   ├── Makefile
│   ├── README.md
│   ├── aiapps
│   ├── carbike
│   ├── configs
│   ├── manage.py
│   └── requirements.txt
├── data
│   ├── configs
│   │           └── stores.json # label
│   ├── imagefiles_224.npy # train dataset
│   ├── original # train data
│   └── tests
├── docker-compose.yml
├── generate_dataset
│   ├── Dockerfile
│   ├── README.md
│   └── app_224.py
├── get_data
│   ├── Dockerfile
│   └── app.py
├── models
│   └── vgg16_transfer.h5
├── predict # predict command line 
│   ├── Dockerfile
│   └── app.py 
└── train 
    ├── Dockerfile
    ├── README.md
    ├── env_tensorflow.yml # conda env file
    └── vgg16_transfer.py
```

## Usage

VGG16 transfer learning model！

### 1. Generate dataset

```
docker-compose run --rm generate_dataset224
```

### 2. Train

#### On Docker
```
docker-compose run --rm vgg16_transfer
```

#### On Conda

Reference train/README.md

### 3.  Predict on comannd line

#### Reference
```
docker-compose run --rm predict -m {model path} -s {image size} -i {input file}
```

#### Exmaple

```
docker-compose run --rm predict -m /models/vgg16_transfer.h5 -s 224 -i tests/toda1.jpeg
```

### 4. Run web app

```
docker-compose up -d --force-recreate
```

http://localhost:8000

## Deploy for Heroku

Reference app/README.md

## Author

[kuniiskywalker](https://github.com/kuniiskywalker)