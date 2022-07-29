#!/bin/bash
# sends arguments using get
curl -s "$1" -X GET -H 'X-HolbertonSchool-User-Id:98'
