"""
This is a file which will contain basic functions to call the GIOŚ API
"""

import requests


def get_all_measuring_stations():
    """
    Returns a list of all measuring stations with their details.

    Examplary response
    ------------------
    [{
        "id": 14,
        "stationName": "Działoszyn",
        "gegrLat": "50.972167",
        "gegrLon": "14.941319",
        "city": {
            "id": 192,
            "name": "Działoszyn",
            "commune": {
                "communeName": "Bogatynia",
                "districtName": "zgorzelecki",
                "provinceName": "DOLNOŚLĄSKIE"
            }
        },
        "addressStreet": null
    }]
    """
    url = "https://api.gios.gov.pl/pjp-api/rest/station/findAll"
    response = requests.get(url, timeout=5)
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        response.raise_for_status()
        raise Exception("Something went wrong")
