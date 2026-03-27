import numpy as np
#integration using trapezoidal rule
#Tk is the duration of the signal 
def integrate_sine(A, omega, phi, T_k):
    step_T=1/(100*(omega/(2*np.pi)))
    T0 = 0
    P = 0
    # Pre-calculate the starting point to avoid double-calculating sines
    y0 = A * np.sin(omega * T0 + phi)
    
    for i in range(int(T_k / step_T)):
        T = T0 + step_T
        y1 = A * np.sin(omega * T + phi)
        
        integral = (y0 + y1) * step_T / 2
        P += integral
        
        T0 = T
        y0 = y1 # Reuse the right side as the left side of the next trapezoid
        
    return P

if __name__ == "__main__":
    print(integrate_sine(1, 1, 0, 10))

