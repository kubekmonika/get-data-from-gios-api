"""
This is a file which will contain basic functions to call the GIOŚ API
"""

import requests
import errors


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


def get_all_sensors(station_id):
    """
    Returns a list of all sensors for a given station.

    Examplary response
    ------------------
    [{
        "id": 92,
        "stationId": 14,
        "param": {
            "paramName": "pył zawieszony PM10",
            "paramFormula": "PM10",
            "paramCode": "PM10",
            "idParam": 3
        }
    },
    {
        "id": 88,
        "stationId": 14,
        "param": {
            "paramName": "dwutlenek azotu",
            "paramFormula": "NO2",
            "paramCode": "NO2",
            "idParam": 6
        }
    }]
    """
    url = f"https://api.gios.gov.pl/pjp-api/rest/station/sensors/{station_id}"
    response = requests.get(url, timeout=5)
    if response.status_code == requests.codes.ok:
        if response.text:
            json = response.json()
            if json:
                return json
            else:
                raise errors.NoDataReturned(f'Response: "{response.text}"')
        else:
            raise errors.NoDataReturned(f'Response: "{response.text}"')
    else:
        response.raise_for_status()
