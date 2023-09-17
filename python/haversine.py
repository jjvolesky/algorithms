import math
import sys

def haversine(lat1, long1, lat2, long2, r):
    phi1 = lat1 * math.pi / 180
    phi2 = lat2 * math.pi /180
    lambda1 = long1 * math.pi /180
    lambda2 = long2 * math.pi /180
    
    relationship1 = (math.sin((phi2 - phi1)/2))**2
    relationship2 = (math.sin((lambda2 - lambda1)/2))**2
    relationship3 = relationship1 + math.cos(phi1) * math.cos(phi2) * relationship2

    d = 2*r * math.asin(math.sqrt(relationship3))
    return int(d)
