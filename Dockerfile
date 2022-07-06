FROM python:3.9.12

WORKDIR /home/Telegram_bot
ENV TELEGRAM_API_TOKEN=""

COPY ./requirements.txt /home/Telegram_bot/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r /home/Telegram_bot/requirements.txt

COPY . /home/Telegram_bot