#!/bin/bash
# sends a POST request with data
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
