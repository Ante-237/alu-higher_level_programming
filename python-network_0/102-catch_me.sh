#!/bin/bash
# bash script makes request to certain ip , ctf style 
curl -sL 0.0.0.0:5000/catch_me -X PUT "You got me!" -H "Origin: School" -d "user_id=98".
