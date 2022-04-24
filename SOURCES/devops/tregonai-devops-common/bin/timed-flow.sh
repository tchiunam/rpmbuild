#!/bin/bash

source /opt/devops-common/lib/logging.sh

set -e

# ====================================
# Default variable
# ====================================
declare -a job_attrs=(summary timeout entrypoint)
declare -a jobs
declare -A job_detail


# ====================================
# Read arguments
# ====================================
function print_usage() {
    cat <<USAGE
Usage: $0 -p <job path> [--preview]
  -p, --job-path         Path to your jobs.
  --preview              Preview job detail.
  -h, --help             Print this help.
USAGE
    exit
}

arguments=`getopt -o p:h --long job-path:,preview,help -- "$@"`
eval set -- "$arguments"

while true; do
    case "$1" in
        -p | --job-path )
            job_path="$2"
            shift 2 ;;
        --preview )
            preview=true
            shift ;;
        -h | --help )
            print_usage
            shift ;;
        -- ) shift; break ;;
        * ) break ;;
    esac
done


# ====================================
# Function
# ====================================
function load_jobs() {
    eval job_path=${job_path}
    for f in `ls ${job_path}`; do
        jobs+=(${f})
        job_detail[${f}-file]=${job_path}/${f}
        for attr in ${job_attrs[@]}; do
            attr_prefix="# ${attr}: "
            attr_value=`grep -m 1 "^${attr_prefix}" ${job_path}/${f}`
            job_detail[${f}-${attr}]="${attr_value:${#attr_prefix}}"
        done
    done
}

function preview_jobs() {
    # Print the detail of jobs
    for (( i=0; i<${#jobs[@]}; i++ )); do
        echo "[${jobs[$i]}]"
        job_name=${jobs[$i]}
        for attr in ${job_attrs[@]}; do
            echo "${attr^}: ${job_detail[${job_name}-${attr}]}"
        done
        echo
    done
    exit
}

function run_jobs() {
    for (( i=0; i<${#jobs[@]}; i++ )); do
        info ${FUNCNAME}:${LINENO} "Job [${i}]: ${jobs[$i]}"
        job_name=${jobs[$i]}
        for attr in ${job_attrs[@]}; do
            info ${FUNCNAME}:${LINENO} "${attr^}: ${job_detail[${job_name}-${attr}]}"
        done
        start_time=`date +%s`
        timeout --preserve-status -s 9 ${job_detail[${job_name}-timeout]} ${job_detail[${job_name}-entrypoint]} ${job_detail[${job_name}-file]}
        end_time=`date +%s`
        sec_spent=$((end_time-start_time))
        hours=$((${sec_spent}/3600))
        minutes=$((${sec_spent}%3600/60))
        seconds=$((${sec_spent}%60))
        info ${FUNCNAME}:${LINENO} "Time spent: ${hours}h:${minutes}m:${seconds}s"
        info ${FUNCNAME}:${LINENO} "record:${job_name}:${hours}:${minutes}:${seconds}"
    done
    exit
}


# ====================================
# Main
# ====================================
[ -z ${job_path} ] && print_usage

load_jobs
${preview:-false} && preview_jobs
run_jobs
