#!/bin/bash

docker build -t zizoo -f Dockerfile . && docker run -d --rm --name zizoo zizoo && sleep 1 ; docker exec -it zizoo /usr/bin/tail -f /var/log/zizoo.log
