#!/usr/bin/python

import itertools
from collections import OrderedDict
import requests
import uuid
from datetime import datetime

def post(params):
    return requests.post('http://ec2-13-211-167-117.ap-southeast-2.compute.amazonaws.com:8000/gaddsDownload/',
                         json=params)

def combinations(choices):
    return [dict(zip(choices.keys(), choice_values))
            for choice_values in itertools.product(*choices.values())]

def template():
    return {
        'requestId': str(uuid.uuid4()),
        'emailAddress': 'umma.zannat@ga.gov.au',
        'extent': {
            'type': 'Feature',
            'geometry': {
                'type': 'Polygon',
                'coordinates': [[[148.422, -25.577],
                                 [148.422, -10.091],
                                 [123.992, -10.091],
                                 [123.992, -25.577]]],
            'crs': 'EPSG:4283'
            }
        },

        'datasets': [
            {
                'datasetId': 'http://dapds00.nci.org.au/thredds/fileServer/rr2/ground_gravity/NT/P201701/points/P201701_GNDGRAV/P201701_GNDGRAV.nc',
                'variables': None,
                'stride': 1
            }
        ],

        'formats': {'point': 'netCDF', 'line': 'netCDF', 'grid': 'netCDF'},
        'crs': 'EPSG:4283',
        'gridResolution': None,
        'gridResampling': 'cubic',
        'submitDateTime': datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
        'startDateTime': None,
        'endDateTime': None,
        'status': 'Pending',
        'zipFileLocation': None
    }

Alex_choices = OrderedDict([
    ('crs', ['EPSG:4283', 'EPSG:3577', 'EPSG:28353']),
    ('form', ['point', 'line', 'grid']),
    ('extent_geometry', ['rectangle', 'triangle', 'circle', 'concave_shape', 'MultiPolygon']),
    ('intersection', ['contained', 'intersecting', 'disjoint', 'exact_match']),
    ('resampling', [None, 'cubic', 'near', 'bilinear', 'cubicspline', 'lanczos', 'average', 'mode', 'min', 'max', 'med', 'Q1', 'Q3']),
    ('resolution', [None, 0.05, 1, 100, -5]), # These need to be CRS-appropriate, i.e. in degrees or metres
    ('format', ['netCDF', 'ASEG-GDF2', 'ERS', 'Gtiff']),
])
