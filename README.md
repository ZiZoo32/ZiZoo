# ZiZoo

The project is a Telegram bot that provides a zip-archive of a repository from GitHub. <br>
The project is created on Python 2.7 using python-telegram-bot API.<br><br>
The source code of **ZiZoo** is a **zizoo.py** file. To start working with **ZiZoo** you need python v2 and git installed on your system.<br>
You have to install python-telegram-bot and python-git packages as well.<br>
<br>
ZiZoo was tested on Debian 9 and can work inside a docker container.<br><br>
If you use Docker configuration, please get the source code (**zizoo.py**), **Dockerfile** and **runme.sh** and put them on the same directory in your system (eg. your home dir) and run **runme.sh**<br>
Prepare your system for running Docker and make sure that **runme.sh** is executable (run **chmod 755 runme.sh**).<br><br>
To begin using **ZiZoo** find ZiZoo (ZiZoo_SPB_bot) in your Telegram client and type **/start** or press START button in your client interface.<br>
<br>
## Working with telegram bot
Type **/start**  to get a welcome message.<br><br>
Type **/help** to view help information and example, how to use **ZiZoo** in order to get a copy of GitHub repository.<br><br>
Type **/get username reponame** to get a copy of **github.com/username/reponame**. You receive a zip-archive **username.reponame.zip** that contains the clone of the requested repository, eg. if you type **/get zizoo32 zizoo** you will receive **zizoo32.zizoo.zip** file with the copy of **this** repository.<br><br>
Zip-archives are located in the same system where **zizoo.py** runs. If the archive of the requested repository already exists, **ZiZoo** will not make a copy of the repository, it will just send the archive to the requester. But if the archive was created more than a week ago, you would get a new one. <br>
You receive an archive creation time in the next message from **ZiZoo**. Please note, that **ZiZoo** uses MSK timezone (GMT+3).<br><br>
Type **username** and **reponame** next to **/get** command and use English letters and digits only. If you use non-ASCII symbols in your request, you will get an error message.<br><br>
Type no less than two arguments (**usernname** and **reponame**) in **/get** request. If you put less than two, you will receive an error message. If you put more than two arguments, all unnecessary arguments will be ignored.<br><br>
If you type wrong username or a name of repository, you will get a response that such repository does not exist.<br><br>
**ZiZoo** an process any other type of messages and command but responses do not contain any useful information, only suggestions to run **/help**.<br>
## Logging
**ZiZoo** logs all actions it does. By default, all iformation store in **/var/log/zizoo.log**.<br><br>
If you use Docker, **ZiZoo** uses log file inside the container. When you run **runme.sh** it automatically creates an image, starts container and connects stdout to **ZiZoo** log using **tail** in follow mode (output appended data as the file grows).<br><br>
You can also use any other tools to ckeck **ZiZoo** log. Use **docker exec -it zizoo \<command>**.<br><br>
If you use the default configuration (**Dockerfile** and **runme.sh**) docker container will be removed immediately after he stops.<br>
If you run **zizoo.py** on a host system, use **\<Ctrl+C>** key to stop it.



