import math 

#TODO: dodac generowanie prosotkata obiektowo z parametrami:
# amplituda, okres, czas trwania, krok probkowania
#ale idk czy nie bedzie on wyliczany z czestotliwosci z tego rowniania co na sygnalach bylo 
#offset, faza poczatkowa(phi)

class signal:
    def __init__(self, A, f, Ts, phi):
        self.A = A
        self.f = f
        self.Ts = Ts
        self.phi = phi

    def value(self, t):
        return self.A * math.sin(2 * math.pi * self.f * t + self.phi)

sinus=signal(1, 50, 0.01, 0)
print(sinus.value(0))
