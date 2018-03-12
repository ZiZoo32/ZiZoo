# ZiZoo

The project contains a Telegram bot provides a zip archive of a requested repository from GitHub. <br>
The project created on Python 2.7 and uses python-telegram-bot API.<br><br>
Source code of **ZiZoo** is **zizoo.py** file. To get started with **ZiZoo** you need python v2 and git installed on your system.<br>
You have to install python-telegram-bot and python-git python packages.<br>
<br>
ZiZoo was tested on Debian 9 and can works inside a docker container.<br>
If you would like to use Docker configuration, please get the source code (**zizoo.py**), **Dockerfile** and **run_me.sh** and put them on the same directory in your system (eg, your home dir) and run **run_me.sh**<br>
You system should be ready to run Docker of course and you need to make **run_me.sh** and **zizoo.py** executable (eg. **chmod 755 run_me.sh**).<br><br>
To begin using **ZiZoo** find ZiZoo (ZiZoo_SPB_bot) in your Telegram client and type **/start** (press START button in your client).<br>
<br>
<br>
## Working with telegram bot:
Type **/start**  to get the welcome message. You also be proposed to get an additional help information.<br><br>
Type **/help** to view a help information and example, how to use **ZiZoo** to get a copy of GitHub repository.<br><br>
Type **/get username reponame** to get a copy of **github.com/username/reponame**. You will receive a zip-archive **username.reponame.zip** contins the clone of requested repository, eg. if you type **/get zizoo32 zizoo** you will receive **zizoo32.zizoo.zip** file contains the copy of **this** repository.<br><br>
Zip archives locate on the same system with zizoo.py run. If the archive of the requested repository is already exists, **ZiZoo** will not make a copy of the repository, just send the archive to the requester. But if the archive was made more than a week ago, it will be created again. <br>
You will receive a time creation information in the next message from **ZiZoo**. Please note, that **ZiZoo** uses MSK timezone (GMT+3).<br><br>
**username** and **reponame** should be type next to **/get** command and contains English letters and digits only. If you use non-ASCII symbols in your request, you will get an error message.<br><br>
You need to put two arguments (**usernname** and **reponame**) in **/get** request, if you put less than two, you will receive an error message. If you put more than two arguments, all arguments since third will be ignored.<br><br>
If you type wrong username or a name of repository, you will get a response that such repository does not exist.<br><br>
**ZiZoo** an process any other type of messages and command but responses do not contain any useful information, only suggestions to run **/help**.<br>
## Logging
**ZiZoo** logs all actions it does. By default, all iformation store in **/var/log/zizoo.log**.<br><br>
If you use Docker, **ZiZoo** uses log file inside the container. When you run **run_me.sh** it automatically creates an image, starts container and connects stdout to **ZiZoo** log using **tail** in follow mode (output appended data as the file grows).<br><br>
You can also use any other tools to ckeck **ZiZoo** log. Use **docker exec -it zizoo \<command>**.<br><br>
If you use the default configuration (**Dockerfile** and **run_me.sh**) docker container will be removed immediately after he stops.<br>
If you run **zizoo.py** on a host system, use **\<Ctrl+C>** key to stop it.



