import math
from aiogram import types
from utils.misc import show_on_gpams


from data.locations import Shops


def calc_distance(lat1, lon1, lat2, lon2):  # araliqti esaplaw
    R = 6371000
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)

    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + \
        math.cos(phi_1) * math.cos(phi_2) * \
        math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    meters = R * c  # output distance in metrs
    return meters / 1000.0  # output distance in kilometrs


def choose_shortest(location: types.Location):  #eng jaqinlarin tawip sorted qildiq
    distances = list()
    for shop_name, shop_location in Shops:
        distances.append((shop_name,
                         calc_distance(location.latitude, location.longitude,
                                       shop_location["lat"], shop_location["lon"]),
                         show_on_gpams.show(**shop_location),
                         shop_location
                         ))
    return sorted(distances, key=lambda x: x[1])[:2]  # [:2] eki eng jaqin locationdi qaytaradi

