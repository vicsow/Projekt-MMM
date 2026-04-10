import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def oblicz_pochodna_numeryczna(sygnal, wektor_czasu):
    # 1. Obliczamy krok próbkowania (dt) - różnicę czasu między dwiema próbkami
    dt = wektor_czasu[1] - wektor_czasu[0]
    
    # 2. Obliczamy pochodną numeryczną przy użyciu gradientu
    # Gradient oblicza różnicę wartości sygnału i dzieli ją przez krok czasu (dt)
    pochodna = np.gradient(sygnal, dt)
    
    return pochodna

# Generujemy wektor czasu
#   t = np.linspace(0, 10, 1000)
# Generujemy sygnał trójkątny
#    czestotliwosc = 0.2
#    sygnal_trojkatny = signal.sawtooth(2 * np.pi * czestotliwosc * t, 0.5)

#    pochodna_sygnalu = oblicz_pochodna_numeryczna(sygnal_trojkatny, t)
