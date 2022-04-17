@echo off

call %~dp0telebot\Scripts\activate

cd %~dp0telebot

set TOKEN=1810556658:AAHPm_ngxFX3CyYXohrUQ_AB4_XwjgzzB8I

python.exe bot_telegram.py

pause