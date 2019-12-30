AEON recognition
====

Image recognition of the appearance of super "AEON" in Japan

## Requirement

- Docker

## Usage

### Train Task

#### Train original model

##### Generate dataset
```
docker-compose run --rm generate_dataset224
```

##### Train
```
docker-compose run --rm vgg16_transfer
```

***

#### VGG16 transfer learning model

##### Generate dataset
```
docker-compose run --rm vgg16_transfer
```

##### Train
```
docker-compose run --rm vgg16_transfer
```

#### Predict on comannd line

refference
```
docker-compose run --rm predict -m {model path} -s {image size} -i {input file}
```

exmaple
```
docker-compose run --rm predict -m /models/cnn.h5 -s 150 -i tests/toda1.jpeg
```

```
docker-compose run --rm predict -m /models/vgg16_transfer.h5 -s 224 -i tests/toda1.jpeg
```

### Run app

```
docker-compose up -d --force-recreate
```

## Author

[kuniiskywalker](https://github.com/kuniiskywalker)