import numpy as np
import matplotlib.pyplot as plt

"""
Updates to be made:
    Trial runs with actual values of constants, and better plot visualization
    Generalize initialization conditions, with correct expressions
    Need to incorporate the orbital time period of the binary system

    NEED TO FIGURE OUT THE SCALING!!!
"""

#need to be replaced with actual values and scaled accordinglt for the right plots!!!
G=1.0
m_solar=1.0
au=10.0

#G=6.67e-11
#m_solar=2e30
#au=1.5e11

class BinarySystem:
    """
    Simulates a Binary star system. Both the stars are considered as point masses. 
    Only the presence of gravitational force is considered. 
    Following numpy attributes use Cartesian coordinates. 1st value is the x-coordinate, and the 2nd value is the y-coordinate. 
    The initial positions are taken along the x-axis. Initial velocities taken perpendicular to the line joining the centers.

    Args:
        m1 (float): stellar mass 1
        m2 (float): stellar mass 2
        dt (float): timestep of the simulation (in seconds)
        
        pos1 (numpy,float): Coordinates of mass 1
        pos2 (numpy,float): Coordinates of mass 2
        vel1 (numpy,float): Velocity of mass 1
        vel2 (numpy,float): Velocity of mass 2
        acc1 (numpy,float): Acceleration of mass 1
        acc2 (numpy,float): Acceleration of mass 2

    """

    def __init__(self,m1,m2,dt=0.01):
        self.m1=m1*m_solar
        self.m2=m2*m_solar
        self.dt=dt

        L=1*au
        self.pos1=np.array([-(m2/(m1+m2))*L,0])
        self.pos2=np.array([(m1/(m1+m2))*L,0])
        
        self.vel1=np.array([0, self.m2*np.sqrt(G/((self.m1+self.m2)*L))])
        self.vel2=np.array([0,-self.m1*np.sqrt(G/((self.m1+self.m2)*L))])
        #self.vel1=np.array([0, 0.3])
        #self.vel2=np.array([0,-0.3])
        
        F=self.force()
        self.acc1=F/self.m1
        self.acc2=-F/self.m2

    def force(self):
        """
        Function to find the gravitational force on MASS1 due to mass2. The force on MASS2 due to mass1 would be the negative of this value

        Returns:
            F (float): force on mass1 due to mass2
        """
        r=self.pos1-self.pos2
        r_mag=np.linalg.norm(r)
        r_unit=r/r_mag
        F= -G*self.m1*self.m2/(r_mag**2) * r_unit
        return F

    def update_position(self):
        """
        Function updates the positions of mass1 and mass2 at each time step dt.
        It calls the force() function to update the acceleration, and hence velocity as well.

        Returns:
            None
        """
        self.pos1+=self.vel1*self.dt
        self.pos2+=self.vel2*self.dt
        self.vel1+=self.acc1*self.dt
        self.vel2+=self.acc2*self.dt
        F=self.force()
        self.acc1=F/self.m1
        self.acc2=-F/self.m2


#we create a binary system object, and call the methods to simulate their orbits here
def orbit_plot(m1,m2,time,dt=0.01):
    """
    Plots the orbit of a binary star system, with a constant separation.
    
    Args:
        m1 (float): Stellar mass 1 (in units of solar mass)
        m2 (float): Stellar mass 2 (in units of solar mass)
        time (float): Time to run the simulation
        dt (float): Time step of the simulation

    """
    bin_sys=BinarySystem(m1,m2)

    n=int(time/dt)
    loc_mass1=np.zeros((n,2))
    loc_mass2=np.zeros((n,2))
    for i in range(n):
        bin_sys.update_position()
        loc_mass1[i,:]=bin_sys.pos1
        loc_mass2[i,:]=bin_sys.pos2

    plt.style.use('dark_background')
    plt.plot(loc_mass1[:,0]/au,loc_mass1[:,1]/au,linewidth=2,label='mass 1')
    plt.plot(loc_mass2[:,0]/au,loc_mass2[:,1]/au,linewidth=2,ls='--',label='mass 2')
    plt.legend()
    plt.show()
    


#orbit_plot(5,10,100)