FROM kureed/environment_for_bots:v1

WORKDIR /bot

COPY ./ /bot/

CMD [ "python3", "bot_telegram.py" ]
