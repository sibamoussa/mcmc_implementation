import numpy as np
import matplotlib.pyplot as plt
import math
from flask import Flask

    
def target(theta):
    return (-0.5*theta**2+0.25*theta**4)   # double well potential

def prob_density(theta,beta):
    return np.exp(-beta*target(theta))    #partition function 
# prob proportional to e^(-energy(i)/kt) beta=1/kt
def main():
    n_iterations = 20000
    k=8.617*10**-5
    deg_C=0
    constant=1

    theta = np.arange(n_iterations,dtype=np.float)
    t=273+deg_C
    barrier_height=k*t
    beta=constant/barrier_height
    theta[0] = 0 #initial guess
    counter = 0 

    for i in range(1, n_iterations-1):
        theta_next =theta[i]+np.random.uniform(-1,1)
        if np.random.uniform(0,1) < min(1, prob_density(theta_next,beta)/prob_density(theta[i],beta)):
            theta[i+1] = theta_next

            counter = counter + 1
        else:
            theta[i+1] = theta[i]
 
    print("acceptance fraction is ", counter/float(n_iterations))
  
    plt.subplot(1, 3, 1)
    plt.scatter(theta,target(theta),color='black')
    plt.xlabel('Position (x)')
    plt.ylabel('V(x) / Potential Energy of the Mean Force')

    plt.subplot(1, 3, 2)
    plt.scatter(np.array(range(0,n_iterations)),theta,label='x')
    plt.title('MCMC Sampled Values at '+ str(t) + ' Kelvin and ' +str(constant) + '/barrier height (kt)')
    plt.ylabel(' Position (x)')
    plt.xlabel('Iteration #')
    
    plt.subplot(1, 3, 3)
    plt.hist(theta, bins=int(math.sqrt(len(theta))), color='blue')
    plt.ylabel('Probability Density')
    plt.xlabel('Position (x)')
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.show()



if __name__ == '__main__':
    main()
