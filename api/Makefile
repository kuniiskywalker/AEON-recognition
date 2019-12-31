build:
	docker build -t aeon-recognition .
.PHONY: build

login:
	heroku container:login
.PHONY: login

restart:
	heroku restart --app aeon-recognition
.PHONY: restart

logs:
	heroku logs --app aeon-recognition
.PHONY: logs

config:
	heroku ps:scale --app aeon-recognition web=1
.PHONY: config

deploy: build login
	heroku container:push --app aeon-recognition web
	heroku container:release --app aeon-recognition web
.PHONY: deploy
