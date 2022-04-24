# summary: Start Bitbucket
# timeout: 2m
# entrypoint: /bin/bash

systemctl start bitbucket.service
monit monitor MONIT_CHECK_PROCESS_NAME
