# summary: Start SonarQube
# timeout: 2m
# entrypoint: /bin/bash

systemctl start sonarqube.service
monit monitor MONIT_CHECK_PROCESS_NAME
