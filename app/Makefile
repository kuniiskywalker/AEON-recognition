build:
	docker build -t aeon-recognition .
.PHONY: build

login:
	heroku container:login
.PHONY: login

deploy: build login
	heroku container:push --app aeon-recognition web
	heroku container:release --app aeon-recognition web
	heroku ps:scale --app aeon-recognition web=1
.PHONY: deploy
