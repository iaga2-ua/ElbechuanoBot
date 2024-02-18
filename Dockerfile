FROM python:3.10
WORKDIR /discordBot
COPY requirements.txt /discordBot/
RUN pip install -r requirements.txt
COPY . /discordBot
CMD python discordBot.py