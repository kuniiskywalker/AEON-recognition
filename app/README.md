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
|  PORT  |  django port (When running on heroku, there is no need to set because heroku is allocated)  |
|  DEBUG  | enable debug : 1, no debug: 0 (default: 0)  |
|  SECRET_KEY  |  geneted django key  |
|  ADDITIONAL_ALLOW_HOST  |  aeon-recognition.herokuapp.com  |

### Local docker

```
docker run -d --name aeon-recognition -e "PORT=8765" -e "DEBUG=1" -p 8007:8765 aeon-recognition
```

### Deploy

#### Initial setup

```
heroku config:set SECRET_KEY=SOME_SECRET_VALUE -a HEROKU APP NAME
```


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

## Author

[kuniiskywalker](https://github.com/kuniiskywalker)
