#!/bin/bash

set -o errexit
set -o errtrace

gl_log_level=${gl_log_level:-INFO}
gl_log_screen=${gl_log_screen:-true}
gl_log_color=${gl_log_color:-true}

declare -A LOG_LEVELS=( ["CRITICAL"]=0 ["ERROR"]=10 ["WARN"]=20 ["INFO"]=30 ["DEBUG"]=40 )

function get_current_time() {
    # Get the current time down to millisecond.

    local current_time=`date +%Y.%m.%d-%H:%M:%S.%N`
    echo ${current_time:0:23}
}

function colorize_message() {
    # Add color to the given string.

    local color=$1; shift
    local string=$1

    if ${gl_log_color}; then
        case ${color} in
            "GREEN") echo "\033[00;32;1m${string}\033[0m";;
            "LIGHT_BLUE") echo "\033[01;34;1m${string}\033[0m";;
            "RED") echo "\033[00;31;1m${string}\033[0m";;
            *) echo "$string";;
        esac
    else
        echo "$string"
    fi
}

function log() {
    # Logging message base on log level. The color of message of different log level is different.

    local level=$1; shift
    local process=$1; shift

    if [ ${LOG_LEVELS[${level}]} -le ${LOG_LEVELS["ERROR"]} ]; then
        ${gl_log_screen} && echo -e "`get_current_time` ${process} [`colorize_message RED ${level}`] `colorize_message RED "$*"`" >&2
        if [ ! -z ${gl_log_file} ]; then
            echo -e "`get_current_time` ${process} [${level}] $*" >> ${gl_log_file}
        fi
        if [ ${LOG_LEVELS[${level}]} -le ${LOG_LEVELS["CRITICAL"]} ]; then
            echo -e "`get_current_time` ${process} [`colorize_message RED ${level}`] `colorize_message RED "Exit."`" >&2
            exit 1
        fi
    elif [ ${LOG_LEVELS[${level}]} -le ${LOG_LEVELS["WARN"]} ]; then
        ${gl_log_screen} && echo -e "`get_current_time` ${process} [`colorize_message LIGHT_BLUE ${level}`] $*" >&2
        if [ ! -z ${gl_log_file} ]; then
            echo -e "`get_current_time` ${process} [${level}] $*" >> ${gl_log_file}
        fi
    elif [ ${LOG_LEVELS[${level}]} -le ${LOG_LEVELS["INFO"]} ]; then
        ${gl_log_screen} && echo "`get_current_time` ${process} [${level}] $*"
        if [ ! -z ${gl_log_file} ]; then
            echo "`get_current_time` ${process} [${level}] $*" >> ${gl_log_file}
        fi
    elif [ ${LOG_LEVELS[${level}]} -le ${LOG_LEVELS["DEBUG"]} ]; then
        ${gl_log_screen} && echo -e "`get_current_time` ${process} [`colorize_message GREEN ${level}`] $*"
        if [ ! -z ${gl_log_file} ]; then
            echo -e "`get_current_time` ${process} [$level] $*" >> ${gl_log_file}
        fi
    fi
}

function critical() {
    if [ ${LOG_LEVELS[${gl_log_level}]} -ge ${LOG_LEVELS["CRITICAL"]} ]; then
        local process=$1; shift
        log CRITICAL ${process} $*
    fi
}

function error() {
    if [ ${LOG_LEVELS[${gl_log_level}]} -ge ${LOG_LEVELS["ERROR"]} ]; then
        local process=$1; shift
        log ERROR ${process} $*
    fi
}

function warn() {
    if [ ${LOG_LEVELS[${gl_log_level}]} -ge ${LOG_LEVELS["WARN"]} ]; then
        local process=$1; shift
        log WARN ${process} $*
    fi
}

function info() {
    if [ ${LOG_LEVELS[${gl_log_level}]} -ge ${LOG_LEVELS["INFO"]} ]; then
        local process=$1; shift
        log INFO ${process} $*
    fi
}

function debug() {
    if [ ${LOG_LEVELS[${gl_log_level}]} -ge ${LOG_LEVELS["DEBUG"]} ]; then
        local process=$1; shift
        log DEBUG ${process} $*
    fi
}
