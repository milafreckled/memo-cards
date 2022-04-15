from math import radians, cos, sin, asin, sqrt
class Geopoint:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def __eq__(self, o):
        return haversine(self) == haversine(o)
    def __str__(self):
        return '{lat: ' +str(self.lat)+' , lon: '+str(self.lon)+' }'
    def getLat(self):
        return self.lat
    def getLon(self):
        return self.lon

"""Punkt fiksowany oraz funkcja kluczowa do sortowania"""
samplePoint = Geopoint(51.21167, 22.52222)

def haversine(o):
    lon2 = samplePoint.getLon()
    lat2 = samplePoint.getLat()
    lon = o.getLon()
    lat = o.getLat()
    # convert decimal degrees to radians
    lon, lat, lon2, lat2 = map(radians, [o.lon, o.lat, lon2, lat2])
    # haversine formula
    dlon = lon2 - o.lon
    dlat = lat2 - o.lat
    a = sin(dlat / 2)**2 + cos(o.lat) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    meters = 6371000*c
    return meters



if __name__=="__main__":
    number = int(input("Give the number of coordinates: "))
    counter = 0
    coordinates = []
    distances = []
    while counter<number:
        coords = input("Print coordinates, splitted by comma: ")
        coords = coords.split(',')
        testPoint = Geopoint(float(coords[0]), float(coords[1]))
        coordinates.append(testPoint)
        counter += 1
    #print(coordinates[0].__str__())
    coordinatesSorted =  sorted(coordinates, key = haversine)
    for coord in coordinates:
        print(coord.__str__())
