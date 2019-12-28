# Generate dataset

## Build container

```
docker build -t generate_dataset .
```

## Run Container

```
docker run --rm -it -v $PWD/dataset:/app/dataset generate_dataset
```
"magefiles.npy" file is generated in dataset directory
