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

```
docker run -d --name aeon-recognition -e "PORT=8765" -p 8007:8765 aeon-recognition
```

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

## Author

[kuniiskywalker](https://github.com/kuniiskywalker)
