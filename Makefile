run:
        docker run -d --name pytestbot tgbot:first
run-dev:
        docker run -d --rm --name tgbot tgbot:first
stop:
        docker stop tgbot
