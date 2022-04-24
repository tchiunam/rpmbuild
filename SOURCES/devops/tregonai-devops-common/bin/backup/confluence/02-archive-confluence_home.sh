# summary: Archive Confluence home directory
# timeout: 45m
# entrypoint: /bin/bash

tar cz --exclude="backups" --exclude="recovery" --exclude="restore" -C CONFLUENCE_HOME_BASEPATH -f OUTPUT_FILEPATH CONFLUENCE_DIR
