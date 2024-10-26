#!/usr/bin/env python3
""" Calculates how many launches each rocket has been used
"""
import requests


if __name__ == "__main__":
    # Get all launches
    launches_url = "https://api.spacexdata.com/v5/launches"
    response = requests.get(launches_url)
    launches = response.json()

    # Create a dictionary to use as a tally
    rocket_frequency = {}

    # Count launches per rocket
    for launch in launches:
        rocket_id = launch['rocket']

        if rocket_id in rocket_frequency:
            rocket_frequency[rocket_id]['frequency'] += 1
        else:
            rocket_frequency[rocket_id] = {}
            rocket_frequency[rocket_id]['frequency'] = 1

    # Get names for each rocket
    for id in rocket_frequency.keys():
        rocket_url = "https://api.spacexdata.com/v4/rockets/{}".format(id)
        response = requests.get(rocket_url)
        rocket = response.json()
        rocket_name = rocket['name']
        rocket_frequency[id]['name'] = rocket_name

    # Sort the rockets
    sorted_rockets = sorted(
        rocket_frequency.items(),
        key=lambda rocket: (-rocket[1]["frequency"], rocket[1]["name"])
    )

    for rocket, info in sorted_rockets:
        print("{}: {}".format(info['name'], info['frequency']))
