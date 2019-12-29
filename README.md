AEON recognition
====

Image recognition of the appearance of super "AEON" in Japan

## Requirement

- Docker

## Usage

### Original model

#### generate dataset
```
docker-compose run --rm generate_dataset224
```

#### train
```
docker-compose run --rm vgg16_transfer
```

***

### VGG16 transfer learning model

#### generate dataset
```
docker-compose run --rm vgg16_transfer
```

#### train
```
docker-compose run --rm vgg16_transfer
```

### predict

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

## Author

[kuniiskywalker](https://github.com/kuniiskywalker)