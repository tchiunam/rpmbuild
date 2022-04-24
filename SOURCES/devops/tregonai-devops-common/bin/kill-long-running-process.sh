#!/bin/bash

set -o errexit

# ====================================
# Default variable
# ====================================
pattern=""
user=""
declare -i max_seconds=-1 signal=15
is_chatty=false

# ====================================
# Read arguments
# ====================================
function print_usage() {
    cat <<USAGE
Usage: $0 [-u user] [-n <pattern>] [-m <max seconds>] [-s <signal>] [-c]
  -u, --user             Process owner.
  -n, --pattern          Pattern to be matched with process.
  -m, --max-seconds      Max running time in seconds.
  -s, --signal           Kill signal (without '-'). Default is 15.
  -c, --chatty           Print messages when processing.
  -h, --help             Print this help.
USAGE
    exit
}

arguments=`getopt -o u:n:m:s:ch --long user:,pattern:,max-seconds:,signal:,chatty,help -- "$@"`
eval set -- "${arguments}"

while true; do
    case "$1" in
        -u | --user )
            user="${2}"
            shift 2 ;;
        -n | --pattern )
            pattern="${2}"
            shift 2 ;;
        -m | --max-seconds )
            max_seconds="${2}"
            shift 2 ;;
        -s | --signal )
            signal="${2}"
            shift ;;
        -c | --chatty )
            is_chatty=true
            shift ;;
        -h | --help )
            print_usage
            shift ;;
        -- ) shift; break ;;
        * ) break ;;
    esac
done

[ -z ${user} ] || [ -z ${pattern} ] || [ ${max_seconds} -le 0 ] && print_usage

for process in `/bin/find /proc -maxdepth 1 -type d -name "[1-9][0-9]*" -user "${user}" 2>/dev/null`; do
    /bin/grep -q -- "${pattern}" ${process}/cmdline 2> /dev/null || continue
    pid=`basename ${process}`
    # Exclude myself
    [ $$ -eq ${pid} ] && continue
    etime=`ps --pid ${pid} --format etime=`

    days=0
    hours=0
    mins=0
    if [[ ${etime} =~ ([0-9]*[0-9])-([0-9][0-9]):([0-9][0-9]):([0-9][0-9]) ]]; then
        days=${BASH_REMATCH[1]#0}
        hours=${BASH_REMATCH[2]#0}
        mins=${BASH_REMATCH[3]#0}
        seconds=${BASH_REMATCH[4]#0}
    elif [[ ${etime} =~ ([0-9][0-9]):([0-9][0-9]):([0-9][0-9]) ]]; then
        hours=${BASH_REMATCH[1]#0}
        mins=${BASH_REMATCH[2]#0}
        seconds=${BASH_REMATCH[3]#0}
    elif [[ ${etime} =~ ([0-9][0-9]):([0-9][0-9]) ]]; then
        mins=${BASH_REMATCH[1]#0}
        seconds=${BASH_REMATCH[2]#0}
    elif [[ ${etime} =~ ([0-9][0-9]) ]]; then
        seconds=${BASH_REMATCH[1]#0}
    else
        # Process probably dead
        continue
    fi

    elapsed_seconds=$((( ( ( ( days * 24 ) + hours ) * 60 ) + mins ) * 60 + seconds))
    if ${is_chatty}; then
        echo "killing pid=${pid}, etime='${etime}', cmdline='`cat ${process}/cmdline`'" 
    fi
    [ ${elapsed_seconds} -ge ${max_seconds} ] && /bin/kill -${signal} ${pid}
done
