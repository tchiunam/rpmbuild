# summary: Start Jira
# timeout: 2m
# entrypoint: /bin/bash

systemctl start jira.service
monit monitor MONIT_CHECK_PROCESS_NAME
