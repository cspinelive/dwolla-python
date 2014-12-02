'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  This file contains functionality for all contact related endpoints.
'''

import __init__ as d
from rest import r


def get(params=False, access_token=False):
    """
    Get contacts from user associated with OAuth token.

    :param params: Dictionary with additional parameters.
    :return: Dictionary with contacts.
    """
    p = {'oauth_token': access_token if access_token else d.access_token}

    if params:
        p = dict(p.items() + params.items())

    return r._get('/contacts/', p)


def nearby(lat, lon, params=False):
    """
    Returns Dwolla spots near the specified geographical location.

    :param lat: Double of latitudinal coordinates.
    :param lon: Double of longitudinal coordinates.
    :param params: Dictionary with additional parameters.
    :return: Dictionary with spots.
    """
    if not lat:
        raise Exception('nearby() requires lat parameter')
    if not lon:
        raise Exception('nearby() requires lon parameter')

    p = {
        'client_id': d.client_id,
        'client_secret': d.client_secret,
        'latitude': lat,
        'longitude': lon
    }

    if params:
        p = dict(p.items() + params.items())

    return r._get('/contacts/nearby/', p)