# Original model

## generate dataset
```
docker-compose run --rm generate_dataset
```

## train
```
docker-compose run --rm vgg16_transfer
```

***

# VGG16 transfer learning model

## generate dataset
```
docker-compose run --rm vgg16_transfer
```

## train
```
docker-compose run --rm vgg16_transfer
```

## predict

```
docker-compose run --rm predict tests/toda1.jpeg
```

