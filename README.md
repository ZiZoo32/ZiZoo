# ZiZoo

The project contains a Telegram bot provides a zip archive of a requested repository from GitHub. <br>
The project created on Python 2.7 and uses python-telegram-bot API.<br>
To begin using **ZiZoo** find ZiZoo (ZiZoo_SPB_bot) in your Telegram client and type **/start** (press START button in your client).<br>
<br>
Source code of **ZiZoo** is **zizoo.py** file. To get started with **ZiZoo** you need python v2 and git installed on your system.<br>
You have to install python-telegram-bot and python-git python packages.<br>
<br>
ZiZoo was tested on Debian 9 and can works inside a docker container.<br>
If you would like to use Docker configuration, please get the source code (**zizoo.py**), **Dockerfile** and **run_me.sh** and put them on the same directory in your system (eg, your home dir) and run run_me.sh<br>
You system should be ready to run Docker of course and you need to make **run_me.sh** and **zizoo.py** executable (eg. **chmod 755 run_me.sh**).<br>
<br>
## Working with telegram bot:
Type **/start**  to get the welcome message. You also be proposed to get an additional help information.<br><br>
Type **/help** to view a help information and example, how to use **ZiZoo** to get a copy of GitHub repository.<br><br>
Type **/get username reponame** to get a copy of **github.com/username/reponame**. You will receive a zip-archive **username.reponame.zip** contins the clone of requested repository, eg. if you type **/get zizoo32 zizoo** you will receive the copy of **this** repository.<br><br>
Zip archives locate on the same system with zizoo.py run. If the archive of the requested repository is already exists, **ZiZoo** will not make a copy of the repository, just send the archive to the requester. But if the archive was made more than a week ago, it will be created again. <br>
You will receive a time creation information in the next message from **ZiZoo**. Please note, that **ZiZoo** uses MSK timezone (GMT+3).<br><br>
**username** and **reponame** should be type next to **/get** command and contains English letters and digits only. If you use non-ASCII symbols in your request, you will get an error message.<br>
You need to put two arguments in **/get** request, if you put less than two, you will receive an error message.<br>


