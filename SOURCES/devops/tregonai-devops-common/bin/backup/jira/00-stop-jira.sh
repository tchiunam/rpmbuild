# summary: Stop Jira
# timeout: 2m
# entrypoint: /bin/bash

monit unmonitor MONIT_CHECK_PROCESS_NAME
systemctl stop jira.service
