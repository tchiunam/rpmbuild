# summary: Archive Bamboo home directory
# timeout: 45m
# entrypoint: /bin/bash

tar cz --exclude="artifacts" --exclude="build-dir" --exclude="build_logs" -C BAMBOO_HOME_BASEPATH -f OUTPUT_FILEPATH BAMBOO_DIR
