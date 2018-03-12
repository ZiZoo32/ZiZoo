# ZiZoo

The project contains a Telegram bot provides a zip archive of a requested repository from GitHub. 
The project created on Python 2.7 and uses python-telegram-bot API.
To begin using ZiZoo find ZiZoo (ZiZoo_SPB_bot) in your Telegram client and type /start (press START button in your client)

Source code of ZiZoo is zizoo.py file. To get started with ZiZoo you need python v2 and git installed on your system. You have to install python-telegram-bot and python-git python packages.

ZiZoo was tested on Debian 9 and can works inside a docker container. If you would like to use Docker configuration, please get the source code (zizoo.py), Dockerfile and run_me.sh and put them on the same directory in your system (eg, your home dir).
You system should be ready to run Docker of course.

## Working with telegram bot:
**/start** - returns the welcome message and suggest to use /help
