# ZiZoo

The project contains a Telegram bot provides a zip archive of a requested repository from GitHub. <br>
The project created on Python 2.7 and uses python-telegram-bot API.<br>
To begin using ZiZoo find ZiZoo (ZiZoo_SPB_bot) in your Telegram client and type /start (press START button in your client).<br>
<br>
Source code of ZiZoo is zizoo.py file. To get started with ZiZoo you need python v2 and git installed on your system.<br>
You have to install python-telegram-bot and python-git python packages.<br>

ZiZoo was tested on Debian 9 and can works inside a docker container. If you would like to use Docker configuration, please get the source code (zizoo.py), Dockerfile and run_me.sh and put them on the same directory in your system (eg, your home dir).
You system should be ready to run Docker of course.


## Working with telegram bot:

Type **/start**  to get the welcome message. You also be proposed to get an additional help information.
Type **/help** to view a help information and example, how to use ZiZoo to get a copy of GitHub repository. 
Type **/get username reponame** to get a copy of **github.com/username/reponame**. You will receive a zip-archive **username.reponame.zip** contins the clone of requested repository, eg. if you type 
