# summary: Archive Bitbucket home directory
# timeout: 1h
# entrypoint: /bin/bash

tar cz --exclude="export" -C BITBUCKET_HOME_BASEPATH -f OUTPUT_FILEPATH BITBUCKET_DIR
