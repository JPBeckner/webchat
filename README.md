# webchat
> Simple Webchat made with Django

This project uses Django Channels to handle WebSocket to make the chat connections.

## Instaling
> It's recommended to use Pipenv to the virtual environment and Python 3.8 to run the project.

Clone or download the project from GitHub. Go to the project directory and install the dependencies.

```shell
pipenv install --python 3.8
```

## Running
Run the project locally.

It's possible in some ways:
```shell
pipenv run execute  # recommended.
```
or
```shell
pipenv run python manage.py runserver 0.0.0.0:8000
```

Now, since it's running locally, just access: http://0.0.0.0:8000/

## Using The Stock Bot
Type on chat the command `/stock=` followed by some parameter:
```
/stock=parameter
```
Parameters example:
* amzn.us
* appl.us
* googl.us

## Notes:
* Unfortunately was not implemented communication via a message broker.
* It's possible to get in the different chat rooms.
* The bot will answer some messages that it doesn't understand (like `/stock=` with no parameters)
* Was chosen dependencies that keep the project simple to run and test,
considering the context in which and why it's was developed.
