#!/usr/bin/python

import argparse
import os
import sys

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# ====================================
# Default Variable
# ====================================
# Update with valid token and room numbers
tokens = {"dev": "<dev_token>",
          "prod": "<prod_token>"}
rooms = {"dev": <hipchat dev room number>,
         "prod": <hipchat prod room number>}
color = {"critical": "red",
         "warning": "yellow",
         "ok": "green",
         "unknown": "gray"}

# ====================================
# Build argument parser
# ====================================
parser = argparse.ArgumentParser(description="Send hipchat message for monit notifications.",
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-e", "--env", action="store", required=True, choices=["dev", "prod"],
                    help="Environment.")
parser.add_argument("-l", "--message-level", action="store", default="unknown", choices=color.keys(),
                    help="Message level.")

args = parser.parse_args()

# Print help if no argument is given.
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

request_url = "https://api.hipchat.com/v2/room/{0}/notification".format(rooms[args.env])
headers = {"Authorization": "Bearer {0}".format(tokens[args.env])}
payload = {"color": color[args.message_level],
           "from": os.getenv("MONIT_HOST"),
           "message": "<b>{service}</b> {event} {url}<ul><li>Date: {date}</li><li>Description: {description}</li><li>CPU: {cpu}</li><li>Memory: {memory}</li><li>Status: {status}</li><ul>".format(
               service=os.getenv("MONIT_SERVICE"),
               event=os.getenv("MONIT_EVENT"),
               date=os.getenv("MONIT_DATE"),
               description=os.getenv("MONIT_DESCRIPTION"),
               cpu=os.getenv("MONIT_PROCESS_CPU_PERCENT"),
               memory=os.getenv("MONIT_PROCESS_MEMORY"),
               status=os.getenv("MONIT_PROGRAM_STATUS"),
               url="<a href=\"http://{0}:2812\">http://{0}:2812</a>".format(os.getenv("MONIT_HOST"))),
           "message_format": "html",
           "notify": True}

r = requests.post(request_url, headers=headers, json=payload, verify=False)
if r.status_code != requests.codes.no_content:
    print("HTTP return code: {0}".format(r.status_code))
    print("Result: {0}".format(r.text))
