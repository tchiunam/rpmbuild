# summary: Dump SonarQube database
# timeout: 5m
# entrypoint: /bin/bash

/opt/devops-common/bin/backup/backup-postgres-database.sh -p PASSWORD -d DATABASE -H HOST -f OUTPUT_FILEPATH
