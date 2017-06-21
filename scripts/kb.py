import numpy as np
from helpers import *


def read_kb(fname):
    lines = []
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    items = {}
    for line in lines:
        name, attribute = line.split(' ')[1:]
        attribute, value = attribute[:-1].split('\t')
        if name in items.keys():
            items[name][attribute] = value
        else:
            items[name] = {attribute : value}
    return items


def modify_kb(kb, specialities):
    new_kb = {}
    for restaurant in kb.keys():
        new_restaurant = restaurant+'_2'
        old_restaurant = restaurant+'_1'

        new_kb[old_restaurant] = kb[restaurant].copy()
        new_kb[old_restaurant]['R_address'] = old_restaurant+'_address'
        new_kb[old_restaurant]['R_phone'] = old_restaurant+'_phone'
        new_kb[old_restaurant]['R_type'] = 'veg'
        new_kb[old_restaurant]['R_speciality'] = np.random.choice(specialities[new_kb[old_restaurant]['R_cuisine']])
        new_kb[old_restaurant]['R_social_media'] = old_restaurant+'_social_media'
        new_kb[old_restaurant]['R_parking'] = old_restaurant+'_parking'
        new_kb[old_restaurant]['R_public_transport'] = old_restaurant+'_public_transport'

        new_kb[new_restaurant] = kb[restaurant].copy()
        new_kb[new_restaurant]['R_address'] = new_restaurant+'_address'
        new_kb[new_restaurant]['R_phone'] = new_restaurant+'_phone'
        #new_kb[new_restaurant]['R_number'] = np.random.choice(['two', 'four', 'six', 'eight'])
        new_kb[new_restaurant]['R_type'] = 'non-veg'
        new_kb[new_restaurant]['R_speciality'] = np.random.choice(specialities[new_kb[new_restaurant]['R_cuisine']])
        new_kb[new_restaurant]['R_social_media'] = new_restaurant+'_social_media'
        new_kb[new_restaurant]['R_parking'] = new_restaurant+'_parking'
        new_kb[new_restaurant]['R_public_transport'] = new_restaurant+'_public_transport'
    return new_kb


def save_kb(kb, fname):
    attrib_list = ['R_cuisine', 'R_location', 'R_price', 'R_rating', 'R_phone', 'R_address', 'R_number', 'R_type', 'R_speciality', 'R_social_media', 'R_parking', 'R_public_transport']
    with open(fname, 'w', encoding='utf-8') as f:
        restaurants = list(kb.keys())
        restaurants.sort()
        for restaurant in restaurants:
            for attrib in attrib_list:
                f.write('1 '+ restaurant + ' ' + attrib + '\t' + kb[restaurant][attrib] + '\n')


if __name__ == '__main__':
    specialities = load_specialities()
    kb = read_kb('../data/dialog-bAbI-tasks/dialog-babi-kb-all.txt')
    new_kb = modify_kb(kb, specialities)
    save_kb(new_kb, '../data/personalized-dialog-dataset/personalized-dialog-kb-all.txt')
