import matplotlib.pyplot as plt
import numpy as np

# returnerer alle verdier for tid og fart for forsøket.
def eks_speed():
    t_A = np.linspace(0,1.0723,200)
    t_B = np.linspace(0,0.81,200)
    t_C = np.linspace(0,1.6192,200)
    # funksjonene er funnet ved regresjonsanalyse i tracker.
    v_A = 2.20703*t_A
    v_B = 667.47*t_B**6-1410.85*t_B**5+1011.61*t_B**4-286.43*t_B**3+30.87*t_B**2+2.52*t_B
    v_C = 0.25*t_C**2+0.79*t_C
    return v_A, v_B, v_C, t_A, t_B, t_C