import numpy as np
import matplotlib.pyplot as plt
import astropy.units as units

"""
Updates to be made:
    Trial runs with actual values of constants, and better plot visualization
    Generalize initialization conditions, with correct expressions
    Need to incorporate the orbital time period of the binary system
"""

#need to be replaced with actual values and scaled accordinglt for the right plots!!!
G=1.0
m_solar=1.0
au=10.0

#G=6.67e-11
#m_solar=units.solMass
#au=units.AU

class BinarySystem:
    """
    Simulates a Binary star system. Both the stars are considered as point masses. 
    Only the presence of gravitational force is considered. 
    NEED TO FIGURE OUT THE SCALING!!!

    Args:
        m1 (float): stellar mass 1
        m2 (float): stellar mass 2
        dt (float): timestep of the simulation (in seconds)

    Attributes:
        Following numpy attributes use Cartesian coordinates. 
        1st value is the x-coordinate, and the 2nd value is the y-coordinate. 
        
        pos1 (numpy,float): Coordinates of mass 1
        pos2 (numpy,float): Coordinates of mass 2
        vel1 (numpy,float): Velocity of mass 1
        vel2 (numpy,float): Velocity of mass 2
        acc1 (numpy,float): Acceleration of mass 1
        acc2 (numpy,float): Acceleration of mass 2

    Methods:
        __init__:
            Initialises the position, velocity, and acceleration of both masses.
            Also initializes the time step of the simulation
        
        force:
            Finds the force on mass1 due to mass2, and returns the force

        update_position:
            Updates the attributes of the object after each time step   
    """

    def __init__(self,m1,m2,dt=0.01):
        """
        Function run to initialize the BinarySystem class. The initial positions are taken along the x-axis.
        Initial velocities taken perpendicular to the line joining the centers.
        """
        self.m1=m1
        self.m2=m2
        self.dt=dt

        self.pos1=np.array([-1*au,0])
        self.pos2=np.array([1*au,0])
        self.vel1=np.array([0,0.3])
        self.vel2=np.array([0,-0.3])
        
        F=self.force()
        self.acc1=F/self.m1
        self.acc2=-F/self.m2

    def force(self):
        """
        Function to find the gravitational force on MASS1 due to mass2. 
        The force on MASS2 due to mass1 would be the negative of this value

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
m1=5*m_solar
m2=5*m_solar
bin_sys=BinarySystem(m1,m2)

n=int(2e4)
loc_mass1=np.zeros((n,2))
loc_mass2=np.zeros((n,2))
for i in range(n):
    bin_sys.update_position()
    loc_mass1[i,:]=bin_sys.pos1
    loc_mass2[i,:]=bin_sys.pos2

plt.plot(loc_mass1[:,0],loc_mass1[:,1],label='mass 1')
plt.plot(loc_mass2[:,0],loc_mass2[:,1],label='mass 2')
plt.legend()
plt.savefig("binary_orbits.png")


