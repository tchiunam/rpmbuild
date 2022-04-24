# summary: Start Bamboo
# timeout: 2m
# entrypoint: /bin/bash

systemctl start bamboo.service
monit monitor MONIT_CHECK_PROCESS_NAME
