FROM debian

RUN apt-get update -y && apt-get install -y dialog apt-utils git python-pip && pip install python-telegram-bot gitpython --upgrade

COPY zizoo.py /usr/local/bin

RUN chmod 755 /usr/local/bin/zizoo.py && mkdir /var/repos

CMD exec /usr/local/bin/zizoo.py 

