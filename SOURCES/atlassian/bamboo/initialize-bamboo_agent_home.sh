#!/bin/bash

bamboo_server_url=$1
if [ "${bamboo_server_url}" == "" ]; then
    # Do not exit and let the java call to return its usage
    echo "Usage: $0 http://<bamboo server>/agentServer" >&2
    echo -e "Example: $0 http://devbamboo/agentServer\n" >&2
fi

/usr/java/jdk1.8.0_66x64/bin/java -Dbamboo.home=/data/bamboo_agent -jar JAR_FILE ${bamboo_server_url}

