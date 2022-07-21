FROM kureed/environment_for_bots:v1

WORKDIR /bot

RUN apk add git
RUN git clone https://github.com/KonstantinGanzew/telegram_bot.git

CMD [ "python3", "bot_telegram.py" ]
