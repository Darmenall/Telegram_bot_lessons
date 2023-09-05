
URL = "http://maps.google.com/map?q={lat},{lon}"


def show(lat, lon):   # Urlg'a lat, lon qosip qoydiq, buni f-string jatdemindeda qosiwg'a bolatin edi
    return URL.format(lat=lat, lon=lon)


