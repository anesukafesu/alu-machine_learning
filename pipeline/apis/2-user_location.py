#!/usr/bin/env python3
""" Prints the location of a GitHub user specified
as an arg to the script
"""
import sys
import requests
import time

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data['location'])
    elif response.status_code == 403:
        rate_limit_reset = int(response.headers['X-Ratelimit-Reset'])
        current_time = int(time.time())
        reset_time_remaining = int((rate_limit_reset - current_time) / 60)
        print('Reset in {} min.'.format(reset_time_remaining))
    elif response.status_code == 404:
        print('Not found')
    else:
        print('Error:', response.status_code)
