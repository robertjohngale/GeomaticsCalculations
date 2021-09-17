# ---------------------------------------------------------------------------
# GeomaticsCalculationsModule.py
# Created on: 2018-03-12
# Description: A simple module for doing routine calculations
# These are very specific for western canada and based on GRS 1980 speriod and lat long based on NAD83 datum
# These might work for other datums/speroids but have not been tested

import math


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


if __name__ == '__main__':
    csf = get_combined_scale_factor()
    print('\nProcess Complete')
