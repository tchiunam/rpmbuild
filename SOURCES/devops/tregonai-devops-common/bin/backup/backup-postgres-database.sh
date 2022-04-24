#!/bin/bash

# ====================================
# Default variable
# ====================================
user=backup
is_compress=true

# ====================================
# Read arguments
# ====================================
function print_usage() {
    cat <<USAGE
Usage: $0 [-u <user>] -p <password> -d <database> -H <database host> -f <output filepath> [--no-compress]
  -u, --user             Backup user.
  -p, --password         Backup user password.
  -d, --database         Database for backup.
  -H, --host             Database host.
  -f, --output-filepath  Output filename (with path) before compression.
  --no-compress          Do not compress the dump.
  -h, --help             Print this help.
USAGE
    exit
}

arguments=`getopt -o u:p:d:H:f:h --long user:,password:,database:,host:,output-filepath:,no-compress,help -- "$@"`
eval set -- "$arguments"

while true; do
    case "$1" in
        -u | --user )
            user="$2"
            shift 2 ;;
        -p | --password )
            export PGPASSWORD="$2"
            shift 2 ;;
        -d | --database )
            database="$2"
            shift 2 ;;
        -H | --host )
            host="$2"
            shift 2 ;;
        -f | --output-filepath )
            out_filepath="$2"
            shift 2 ;;
        --no-compress )
            is_compress=false
            shift;;
        -h | --help )
            print_usage
            shift ;;
        -- ) shift; break ;;
        * ) break ;;
    esac
done

[ -z ${PGPASSWORD} ] || [ -z ${database} ] || [ -z ${host} ] || [ -z ${out_filepath} ] && print_usage

if ${is_compress}; then
    pg_dump -U ${user} -d ${database} -h ${host} | gzip > ${out_filepath}.gz
else
    pg_dump -U ${user} -d ${database} -h ${host} > ${out_filepath}
fi
