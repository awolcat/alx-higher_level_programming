#!/usr/bin/python3
def weight_average(my_list=[]):
    total_vw, total_w, weighted_mean = 0, 0, 0
    if len(my_list) == 0 or my_list is None:
        return 0
    else:
        for duo in my_list:
            value, weight = duo
            vw = value * weight
            total_vw += vw
            total_w += weight
        weighted_mean = total_vw / total_w
        return weighted_mean
