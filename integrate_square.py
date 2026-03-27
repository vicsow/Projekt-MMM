import numpy as np
from scipy import signal
#integration using trapezoidal rule

#Tk is the duration of the signal 
def integrate_square(A, f, duty_cycle, T_k):
    step_T=1/(100*f)
    T0 = 0
    P = 0
    # Pre-calculate the starting point
    y0 = A * signal.square(2 * np.pi * f * T0, duty=duty_cycle)
    
    for i in range(round(int(T_k / step_T))):
        T = T0 + step_T
        y1 = A * signal.square(2 * np.pi * f * T, duty=duty_cycle)
        
        integral = (y0 + y1) * step_T / 2
        P += integral
        
        T0 = T
        y0 = y1
        
    return P

#debug
if __name__ == "__main__":
    print(integrate_square(1, 1, 0.5, 10))


