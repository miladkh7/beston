#!/bin/bash
mytoken=123456
curl --data "token=$mytoken&text=$1&amount=$2" http://127.0.0.1:8000/submit/income/
