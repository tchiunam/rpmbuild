# summary: Archive Jira home directory
# timeout: 30m
# entrypoint: /bin/bash

tar cz --exclude="export" -C JIRA_HOME_BASEPATH -f OUTPUT_FILEPATH JIRA_DIR
