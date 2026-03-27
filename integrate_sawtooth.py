import numpy as np
from scipy import signal
#integration using trapezoidal rule

#Tk is the duration of the signal 
def integrate_sawtooth(A, f, width, T_k):
    step_T=1/(100*f)
    T0 = 0
    P = 0
    # Pre-calculate the starting point
    y0 = A * signal.sawtooth(2 * np.pi * f * T0, width=width)
    
    for i in range(int(T_k / step_T)):
        T = T0 + step_T
        y1 = A * signal.sawtooth(2 * np.pi * f * T, width=width)
        
        integral = (y0 + y1) * step_T / 2
        P += integral
        
        T0 = T
        y0 = y1
        
    return P

#debug
if __name__ == "__main__":
    result = integrate_sawtooth(1, 1, 1.0, 10)
    print(result)


