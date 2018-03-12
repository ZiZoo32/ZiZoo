FROM debian

MAINTAINER Alexander Yarmolinsky <alexander.yarmolinsky@mail.ru>

ENV TZ="Europe/Moscow"

RUN apt-get update -y && apt-get install -y dialog apt-utils git python-pip && pip install python-telegram-bot gitpython --upgrade

RUN ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && dpkg-reconfigure --frontend noninteractive tzdata

COPY zizoo.py /usr/local/bin

RUN chmod 755 /usr/local/bin/zizoo.py && mkdir /var/repos

CMD exec /usr/local/bin/zizoo.py 

