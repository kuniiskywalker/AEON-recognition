# Generate dataset

## Build container

```
docker build -t train .
```

## Run Container

```
docker run --rm -it -v $PWD/dataset:/app/dataset train 
```
