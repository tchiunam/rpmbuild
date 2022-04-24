# summary: Dump Jira database
# timeout: 15m
# entrypoint: /bin/bash

/opt/devops-common/bin/backup/backup-postgres-database.sh -p PASSWORD -d DATABASE -H HOST -f OUTPUT_FILEPATH
