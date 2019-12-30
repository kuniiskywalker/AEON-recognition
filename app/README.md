AEON recognition
====

Image recognition of the appearance of super "AEON" in Japan

## Requirement

- Docker
- Heroku-cli

## Deploy

### Initial setup

```
heroku config:set SECRET_KEY=SOME_SECRET_VALUE -a HEROKU APP NAME
```

## Usage

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
