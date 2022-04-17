@echo off

call %~dp0telebot\Scripts\activate

cd %~dp0telebot

set TOKEN=5259775120:AAHUyIqLMGBRTcbMDcdG3766QL9S-Xzo2zo

python.exe bot_telegram.py

pause