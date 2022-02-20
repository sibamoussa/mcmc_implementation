import numpy as np
import matplotlib.pyplot as plt

def target(theta):
    return (-0.5*theta**2+0.25*theta**4)   #potential energy

def boltzman(theta,beta):
    return np.exp(-beta*target(theta))    
# prob proportional to e^(-energy(i)/kt) beta=1/kt
def main():
    n_iterations = 10000
    theta = np.arange(n_iterations,dtype=np.float)
    target_theta = np.arange(n_iterations,dtype=np.float)
    k=8.617*10**-5
    t=273+20000
    beta=5/(k*t)
    theta[0] = 0 #initial guess
    target_theta[0]=target(theta[0])
    counter = 0 
    for i in range(1, n_iterations-1):
        #theta_next =theta[i]+0.5*(np.random.normal()-0.5)
        theta_next =theta[i]+np.random.uniform(-1,1)
        if np.random.uniform(0,1) < min(1, boltzman(theta_next,beta)/boltzman(theta[i],beta)):
    
    #    if np.random.uniform(0,1) < min(1, target(theta_next)/target(theta[i])):
            theta[i+1] = theta_next
            target_theta[i+1]=target(theta[i+1])
            counter = counter + 1
        else:
            theta[i+1] = theta[i]
            target_theta[i+1]=target(theta[i])

    print("acceptance fraction is ", counter/float(n_iterations))
    x = np.linspace(-2,5,10000)
    #plt.hist(theta, bins=100, color='blue')
    # plt.hist(target_theta, bins=100, color='red')
    #plt.plot(np.array(range(0,n_iterations)),theta)
    plot1=plt.figure(1)
    plt.scatter(theta,target(theta),color='black',label='sim')
  #  plt.scatter(x,target(x),color='blue',label='eqn')
    plt.xlabel('x or theta')
    plt.ylabel('V(x)')

    plt.legend()
    plot2=plt.figure(2)
    plt.scatter(theta,boltzman(theta,beta),color='red',label='sim')
    #plt.scatter(x,boltzman(x,beta),color='green',label='eqn')
    plt.xlabel('x or theta')
    plt.ylabel('Probability of finding system as a function of x')
    plt.legend()

    plot3=plt.figure(3)
    expectedvalue=np.mean(theta)
    print(expectedvalue)
    plt.plot(np.array(range(0,n_iterations)),theta)
    plt.scatter(n_iterations,expectedvalue)
    plt.ylabel('x or theta')
    plt.xlabel('Iteration')
    plt.show()

if __name__ == '__main__':
    main()