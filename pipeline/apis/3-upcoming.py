#!/usr/bin/env python3
""" Get's the earliest upcoming launch from the unofficial SpaceX API.
"""
import requests

if __name__ == '__main__':
    # Getting all upcoming launches
    upcoming_endpoint = 'https://api.spacexdata.com/v4/launches/upcoming'
    response = requests.get(upcoming_endpoint)
    upcoming_launches = response.json()

    # Sorting them to get the earliest launch
    upcoming_launch = sorted(upcoming_launches, key=lambda l: l['date_unix'])[0]

    # Get the rocket for that launch
    rocket_id = upcoming_launch['rocket']
    rocket_url = 'https://api.spacexdata.com/v4/rockets/{}'.format(rocket_id)
    response = requests.get(rocket_url)
    rocket_name = response.json()['name']

    # Get the launchpad to be used
    launchpad_id = upcoming_launch['launchpad']
    launchpad_url = 'https://api.spacexdata.com/v4/launchpads/{}'.format(
        launchpad_id
    )
    response = requests.get(launchpad_url)
    launchpad = response.json()
    launchpad_name = launchpad['name']

    # Get the locality and the local date
    launchpad_locality = launchpad['locality']
    date_local = upcoming_launch['date_local']

    output = "{} ({}) {} - {} ({})".format(
        upcoming_launch['name'],
        date_local,
        rocket_name,
        launchpad_name,
        launchpad_locality
    )

    print(output)
