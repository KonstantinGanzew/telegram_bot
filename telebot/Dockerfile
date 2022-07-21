# Контейнер с необходимым для работы бота
# 1. Импортируем контейнер с питоном
# 2. Доставляем необходимые библиотеки
# 3. Устанавливаем часовой пояс

FROM alpine

RUN apk update 
RUN apk add python3
RUN apk add py-pip
RUN apk add tzdata
ENV TZ=Asia/Yekaterinburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip3 install aiogram
RUN pip3 install asyncio
RUN pip3 install aioschedule
RUN pip3 install datetime
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade google-api-python-client
RUN pip3 install --upgrade oauth2client 
RUN pip3 install bs4