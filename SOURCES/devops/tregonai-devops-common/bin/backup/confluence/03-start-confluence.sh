# summary: Start Confluence
# timeout: 2m
# entrypoint: /bin/bash

systemctl start confluence.service
monit monitor MONIT_CHECK_PROCESS_NAME
