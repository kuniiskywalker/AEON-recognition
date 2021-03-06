AEON recognition
====

Image recognition of the appearance of super "AEON" in Japan

## Requirement

- Docker
- Heroku-cli

## Usage

### Environment

|  Key |  Memo  |
| ---- | ---- |
|  PORT  |  port (When running on heroku, there is no need to set because heroku is allocated)  |

### Local docker

1. Build image
```
docker build -t aeon-recognition .
```

2. Run container
```
docker run -d --name aeon-recognition -e "PORT=8765" -p 8007:8765 aeon-recognition
```

http://localhost:8000

### Deploy

#### Initial setup

1. Login
```
heroku container:login
```

2. Build image

```
docker build -t aeon-recognition .
```

3. Push Image
```
heroku container:push --app aeon-recognition web
```

4. Release
```
heroku container:release --app aeon-recognition web
```

## API

## Endpoint

```
- POST /predict
```

### Parameters

|  Name  |  Type  |  Required  |  Default  |  Description  |
| ---- | ---- | ---- | ---- | ---- |
|  file  |  file  | ◯  |   |  jpg  |

### Response

```
0: label
1: predicted percentage
```

### Example Request

```
curl -X POST -F file=@/home/user/nagakute.jpeg http://localhost:8007/predict/
```

### Example　Response

```
Status: 200 OK
```

```
["高萩店", 23]
```

## Author

[kuniiskywalker](https://github.com/kuniiskywalker)
