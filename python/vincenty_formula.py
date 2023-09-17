import math
import sys

def vincenty(lat1, long1, lat2, long2, r):
    phi1 = lat1 * math.pi/180
    phi2 = lat2 * math.pi/180
    lambda1 = long1 * math.pi/180
    lambda2 = long2 * math.pi/180
    delta_lambda = lambda2 - lambda1

    relationship1 = (math.cos(phi2) * math.sin(delta_lambda))**2
    relationship2 = (math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(delta_lambda))**2
    relationship3 = math.sin(phi1) * math.sin(phi2) + math.cos(phi1) * math.cos(phi2) * math.cos(delta_lambda)

    delta_sigma = math.atan2(math.sqrt(relationship1 + relationship2), relationship3)
    d = r * delta_sigma

    return int(d)
