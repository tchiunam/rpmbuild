# summary: Notify all Toad instances to go offline
# timeout: 2m
# entrypoint: /bin/bash

source /opt/devops-common/lib/logging.sh

declare -a dev_hosts prod_hosts
dev_hosts=(audevtoad01.hk.tregonai.com hkdevtoad01.hk.tregonai.com)
prod_hosts=(hktrntoad01.hk.tregonai.com
            austgtoad01.hk.tregonai.com
            hkstgtoad01.hk.tregonai.com
            syduattoad01.au.tregonai.com
            hkuattoad01.hk.tregonai.com
            sydtoad01.au.tregonai.com
            hktoad01.hk.tregonai.com)

# Continue doing backup even if notification failed
set +e
if [[ `hostname` =~ ^hkbitbucket ]]; then
    for host in ${prod_hosts[@]}; do
        info Main::${LINENO} "Notifying ${host}"
        # Update with a valid token
        curl -isS --insecure -X PUT -H "Content-Type: application/json" -d '{ "user" : "bitbucket", "token" : "<bitbucket_token>", "mode" : "offline" }' https://${host}:5000/tofu/api/1.0/trading_service/misc/toadtsd/mode
    done
else
    for host in ${dev_hosts[@]}; do
        # dev toad may not be up
        info Main::${LINENO} "Notifying ${host}"
        # Update with a valid token
        curl -isS --insecure -X PUT -H "Content-Type: application/json" -d '{ "user" : "bitbucket", "token" : "<bitbucket_token>", "mode" : "offline" }' https://${host}:5000/tofu/api/1.0/trading_service/misc/toadtsd/mode > /dev/null 2>&1
    done
fi
set -e
