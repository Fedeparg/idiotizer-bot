# Idiotizer bot

The only bot you will ever need to win any discussion.

## 🤖 How does the bot work?

The bot takes the input from the user and returns possible ways to make it sound like a complete dumbass (with love).

### Example input

- I am very inteligent

### Possible outputs

- I im viry intiligint
- I aM vErY iNTeLiGEnT

Nobody will doubt this statement.

## ⚙️ How is this developed?

The bot is developed in Python using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot). It is offered with the source code and with the Dockerfile to create the image.

The code is prepared to listen on port 8080 (as stated in the Dockerfile) and uses a bot token from the os environment variables.

```Docker
docker build -t idiotizer .
docker run -d idiotizer
```

## 🤷 Why this exists?

See, London is a pretty boring place once you have seen those magnificent Formula E cars run around the circuit at crazy speeds and so close to each other that you have to reduce the emotion doing something completely unrelated and not useful at all.

TLDR; Why not? 🤪
