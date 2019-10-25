import matplotlib.pyplot as plt
import numpy as np
from eksternlab import height, slope, curvature
import csv

def comma(arr):
    arr_rtn = []
    for elm in arr:
        if elm == '':
            break
        else:
            arr_rtn.append(float(elm.replace(",",".")))
    return arr_rtn


def eksp_data(filnavn):
    reader = csv.reader(
        open(filnavn), delimiter=";")
    t_A = []
    x_A = []
    t_B = []
    x_B = []
    t_C = []
    x_C = []
    teller = 0
    for row in reader:
        if teller > 1:
            t_A.append(row[0])
            x_A.append(row[1])
            t_B.append(row[3])
            x_B.append(row[4])
            t_C.append(row[6])
            x_C.append(row[7])
        teller = teller + 1
    return comma(t_A), comma(x_A), comma(t_B), comma(x_B), comma(t_C), comma(x_C)