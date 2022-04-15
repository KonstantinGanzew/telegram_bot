@echo off

call %~dp0telebot\Scripts\activate

cd %~dp0telebot

set TOKEN=925421434:AAE0_o3dvtjbpaovvlDZAbC-CvKRGtPspT4

python.exe bot_telegram.py

pause