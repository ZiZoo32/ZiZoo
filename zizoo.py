#!/usr/bin/python

import os, time, sys, zipfile, shutil, sys

# Processing repository

def check_zipfile(zipfile_name):
    os.chdir("/var/repos")
    if os.path.exists(zipfile_name) == True:
        zip_mtime = os.path.getmtime(zipfile_name)
        now = time.time()
        if now - zip_mtime < 604800:
            return True
    return False


def clone_repo(repo_url, local_dir):    
    from git import Repo
    from urllib import urlopen
    code = urlopen(repo_url)
    if code.getcode() != 200:
        return False
    os.chdir("/var/repos")
    os.mkdir(local_dir)
    Repo.clone_from(repo_url,local_dir)
    return True


def create_zipfile(zipfile_name, local_dir):    
    os.chdir("/var/repos")
    z = zipfile.ZipFile(zipfile_name, 'w')       
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            z.write(os.path.join(root,file))
    z.close()
    shutil.rmtree(local_dir)


def tlg_get_zipfile(user_name, repo_name):
    repo_url = "https://github.com/" + user_name + "/" + repo_name
    local_dir = str(user_name + "." + repo_name).lower()
    zipfile_name = local_dir + ".zip"
    os.chdir("/var/repos")
    if check_zipfile(zipfile_name) == True:
        return 0
    if os.path.exists(local_dir) == True:
        return 2
    if clone_repo(repo_url,local_dir) == False:
        return 4
    create_zipfile(zipfile_name,local_dir)
    return 1


# Logging 

def logger(user_info, status, * args, **kwargs):
    from datetime import datetime
    request = kwargs.get('request', None)
    zipfile_name = kwargs.get('zipfile_name', None) 
    orig_stdout = sys.stdout
    log_file = open('/var/log/zizoo.log', 'a+')
    sys.stdout = log_file
    log_time = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    log_text = " User ID:" + user_info[0] + " ("

    if user_info[1] != 'None':
        log_text = log_text + "\"" + user_info[1] + "\", "
    log_text = log_text + user_info[2] 
    if user_info[3] != 'None':
        log_text = log_text + " " + user_info[3] + ") "
    else:
        log_text = log_time + log_text + ") "
    if status == 512:     
        log_text = log_time + log_text + "is using non-ASCII symbols in a user or repository name"
    if status == 256:
        log_text = log_time + log_text + "has sent an unknown command " + request 
    if status == 128:
        log_text = log_time + log_text + "has sent a message: " + request 
    if status == 64:
        log_text = log_time + log_text + "has requested a help"
    if status == 32:
        log_text = log_time + log_text + "has sent a start command"
    if status == 16:
        log_text = log_time + log_text + "has requested a copy of GITHUB, but forgot to specify username and a repository"
    if status == 8:
        log_text = log_time + log_text + "has requested a copy of GITHUB for user " + request + ", but forgot to specify a repository"
    if status == 4:     
        log_text = log_time + log_text + "has requested a copy of GITHUB repository " +  request[1] + " for user " + request[0] + ", but such repository is not available"
    if status == 2:     
        log_text = log_time + log_text + "has requested a copy of GITHUB repository " +  request[1] + " for user " + request[0] + ", but archive is being processed rigt now by another request"
    if status == 1:     
        log_text = log_time + " Archive " + zipfile_name + " successfully processed and sent to the" + log_text
    if status == 0:     
        log_text = log_time + " Archive " + zipfile_name + " sent to the" + log_text

    if user_info == 'start':
        log_text = log_time + " ZiZoo telegram bot started"
    if user_info == 'stop':
        log_text = log_time + " ZiZoo telegram bot stopped"

    print log_text
    sys.stdout = orig_stdout
    log_file.close()


# Telegram bot implementation

from telegram.ext import Updater
updater = Updater(token='568894804:AAEvJxvlfMrfbe1CxgHkSMvXJcCIJF_Nfsk')
dispatcher = updater.dispatcher
logger('start',-1)

updater.start_polling()

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bresults = bot.getChat(update.message.chat_id)
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot. I can give you a copy of GITHUB repository. Type /help to get more information.")
    user_info = [ str(update.message.from_user.id),  str(update.message.from_user.username), str(update.message.from_user.first_name), str(update.message.from_user.last_name)] 
    logger(user_info,32)

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="You say \"" + update.message.text + "\". I can't talk to you, but I can give you a copy of GITHUB repository. Type /help to get more information.")
    user_info = [ str(update.message.from_user.id),  str(update.message.from_user.username), str(update.message.from_user.first_name), str(update.message.from_user.last_name)] 
    text = (update.message.text)
    logger(user_info,128,request=repr(text))

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="To get zip archive of a repository from GITHUB please provide your username and repository name in /get request. Use: /get username repository")
    user_info = [ str(update.message.from_user.id),  str(update.message.from_user.username), str(update.message.from_user.first_name), str(update.message.from_user.last_name)] 
    logger(user_info,64)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)


def is_ascii(arg):
    for c in arg:
        if ord(c) >= 128: 
           return False
    return True

def getrepo(bot, update, args):
    from datetime import datetime
    if len(args) == 0:
        status = 16
    elif len(args) == 1:
        status = 8
    else:   
        if (is_ascii(args[0]) == False) or (is_ascii(args[1]) == False):
            status = 512
        else:
            zipfile_name = str('.'.join(args[0:2]).lower() + ".zip")
            status = tlg_get_zipfile(args[0],args[1])

    user_info = [ str(update.message.from_user.id),  str(update.message.from_user.username), str(update.message.from_user.first_name), str(update.message.from_user.last_name)] 
    os.chdir("/var/repos")

    if (status == 0) or (status == 1):
        zipfile_time = datetime.fromtimestamp(os.path.getmtime(zipfile_name)).strftime('%Y-%m-%d %H:%M:%S')
        bot.send_document(chat_id=update.message.chat_id, document=open(zipfile_name,'rb'))
        bot.send_message(chat_id=update.message.chat_id, text="Arhive created from GITHUB on " + zipfile_time + ". Thanks for using ZiZoo.")
        logger(user_info,status,request=args,zipfile_name=zipfile_name)
    if status == 2:
        bot.send_message(chat_id=update.message.chat_id, text="Repository \"" + args[1] + "\" is being processed by another user. Please try again later.")
        logger(user_info,status,request=args)
    if status == 4:
        bot.send_message(chat_id=update.message.chat_id, text="Repository \"" + args[1] + "\" not found for user \"" + args[0] + "\". Type /help to get more information.")
        logger(user_info,status,request=args)
    if status == 8:
        bot.send_message(chat_id=update.message.chat_id, text="Repository name missed. Type /help to get more information.")
        logger(user_info,status,request=args[0])
    if status == 16:
        bot.send_message(chat_id=update.message.chat_id, text="Username missed. Type /help to get more information.")
        logger(user_info,status)
    if status == 512:
        bot.send_message(chat_id=update.message.chat_id, text="Please use only English letters or digits for your /get request. Type /help to get more information.")
        logger(user_info,status)

getrepo_handler = CommandHandler('get', getrepo, pass_args=True)
dispatcher.add_handler(getrepo_handler)



def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand your command. Type /help to get more information.")
    user_info = [ str(update.message.from_user.id),  str(update.message.from_user.username), str(update.message.from_user.first_name), str(update.message.from_user.last_name)] 
    if is_ascii(update.message.text) == False:
        text = repr(update.message.text)
    else:
        text = str(update.message.text)

    logger(user_info,256,request=text)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


updater.idle()
updater.stop()
logger('stop',-1)
