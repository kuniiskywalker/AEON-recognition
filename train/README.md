Train AEON recognition
====

Image recognition of the appearance of super "AEON" in Japan

## Requirement

- Docker

## Installation

### Create conda env

```
conda env create -f=env_tensorflow.yml
```

### Activate conda env

```
conda activate env_tensorflow
```

## Usage

### Train

Input dataset file path
```
../data/imagefiles_224.npy
```

Output model path
```
../models/vgg16_transfer.h5
```

Run train
```
python vgg16_transfer.py
```

## Author

[kuniiskywalker](https://github.com/kuniiskywalker)

