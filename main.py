# ---------------------------------------------------------------------------
# GeomaticsCalculationsModule.py
# Created on: 2018-03-12
# Description: A simple module for doing routine calculations
# These are very specific for western canada and based on GRS 1980 speriod and lat long based on NAD83 datum
# These might work for other datums/speroids but have not been tested

import math
def get_UTMconvergence(lat,lng,zone):

    #a = 6378137; // semi - major axis for GRS 1980
    e2 = 0.00669438 # 'eccentricity for GRS 1980
    eccPrimeSquared = (e2) / (1 - e2)
    utmConv = 0
    latRad = lat * math.pi / 180
    lngRad = lng * math.pi / 180

    CM = (zone - 1) * 6 - 180 + 3
    CMRad = CM * math.pi / 180

    dlng = lngRad - CMRad
    cosSqLat = math.pow(math.cos(latRad), 2)

    etaSq = eccPrimeSquared * cosSqLat
    utmConv = dlng * (1 + (math.pow(dlng, 2) / 3 * (1 + 3 * etaSq) * cosSqLat)) * math.sin(latRad);
    utmConv = utmConv * (180 / math.pi);
    return utmConv;

def UTMToLatLong():
    return "NOT IMPLEMENTED"

def latlongto3TM(lat,lng):
    return "NOT EMPLMENTED"

def get_combined_scale_factor(lat, lng, ellipsoid_height, a, e2, zone):
    k0 = 0.9996  # scale factor at the central meridian

    if a == 0:
        a = 6378137  # semi-major axis for GRS 1980

    if e2 == 0:
        e2 = 0.00669438  # 'eccentricity for GRS 1980
    ecc_prime_squared = e2 / (1 - e2)

    cm = (zone - 1) * 6 - 180 + 3
    cm_rad = cm * math.pi / 180

    lat_rad = lat * math.pi / 180
    lng_rad = lng * math.pi / 180
    t = math.tan(lat_rad) * math.tan(lat_rad)
    c = ecc_prime_squared * math.cos(lat_rad) * math.cos(lat_rad)
    a_cap = math.cos(lat_rad) * (lng_rad - cm_rad)
    vertical_factor = a / (math.sqrt((1 - e2 * math.sin(lat_rad) * math.sin(lat_rad))))
    horizontal_factor = k0 * (1 + (1 + c) * math.pow(a_cap, 2) / 2 + (
                5 - 4 * t + 42 * c + 13 * math.pow(c, 2) - 28 * ecc_prime_squared) * math.pow(a_cap, 4) / 24 +
              (61 - 148 * t + 167 * math.pow(t, 2)) * math.pow(a_cap, 6) / 720)
    elev_factor = vertical_factor / (vertical_factor + ellipsoid_height)
    scale_factor = horizontal_factor * elev_factor

    return scale_factor

def getzonefromlongitude(lng):
    lng = abs(lng)
    zone = 0
    if (lng <= 126 and lng > 120):
        zone = 10
    elif (lng <= 120 and lng > 114):
        zone = 11
    elif (lng <= 114 and lng > 108):
        zone = 12
    elif (lng <= 108 and lng > 102):
        zone = 13
    elif (lng <= 102 and lng > 96):
        zone = 14
    elif (lng <= 96 and lng > 90):
        zone = 15
    return zone



        

if __name__ == '__main__':
    lng = -117.3454
    lat = 55.234
    zone = getzonefromlongitude(lng)
    print (zone)
    csf = get_combined_scale_factor(lat,lng,800,0,0,zone)
    convergence = get_UTMconvergence(lat,lng,zone)
    print (csf)
    print (convergence)
    print('\nProcess Complete')
