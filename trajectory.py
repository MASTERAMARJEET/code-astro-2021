import numpy as np
import matplotlib.pyplot as plt

G = 6.67e-11
m_solar=2e30
au=1.496e11

class BinarySystem:
    """[summary]
    pos1, pos2: positions in speherical coordinates (numpy array of three numbers)
    omega: orbital frequency
    e: eccentricity
    a: semi_major axis length
    acc1: acceleration of mass 1
    acc2: acceleration of mass 2
    vel1: velocity of mass 1
    vel2 : velocity of mass 2

    """

    def __init__(self, m1, m2, a, omega, e, dt=1) -> None:
        self.m1 = m1*m_solar
        self.m2 = m2*m_solar
        #self.omega = omega
        self.e = e
        self.p1 = np.array([-0.5*au, 0.0*au])
        self.p2 = np.array([0.5*au, 0.0*au])
        self.a = a
        self.dt = 1

        self.com = (self.m1 * self.p1 + self.m2 * self.p2) / (self.m1 + self.m2)
        self.pos1 = self.p1 - self.com
        self.pos2 = self.p2 - self.com
        
        #v1_init= -G*self.m2 * np.linalg.norm(self.pos1)*(1+self.e) / (np.linalg.norm(self.pos1 - self.pos2)**2)
        #v2_init= G*self.m1 * np.linalg.norm(self.pos2)*(1+self.e) / (np.linalg.norm(self.pos1 - self.pos2)**2)
        self.v1 = np.array([0.01, -0.01])*au
        self.v2 = np.array([0.01, 0.01])*au
         


    @property
    def force(self):
        r = self.pos2 - self.pos1
        r_norm = np.linalg.norm(r)
        r_unit = r / r_norm
        f = (G * self.m1 * self.m2 / r_norm ** 2) * r_unit
        return f

    def update_position(self):
        self.acc1 = self.force/self.m1
        self.acc2 = -self.force/self.m2
        self.pos1 += self.acc1 * (self.dt ** 2) + self.v1 * self.dt
        self.pos2 += self.acc2 * (self.dt ** 2) + self.v2 * self.dt
        self.v1 += self.acc1 * self.dt 
        self.v2 += self.acc2 * self.dt 
        return self.pos1, self.pos2, self.com


if __name__ == "__main__":
    binary = BinarySystem(1, 1, 0, 0, 2)
    star1_loc = np.zeros((100,2))
    star2_loc= np.zeros((100,2))
    c=np.zeros(2)
    for i in range(100):
        p1, p2,c = binary.update_position()
        star1_loc[i,:]=p1
        star2_loc[i,:]=p2
        #print(f"{p1=};{p2=}")
        
    

    plt.figure(1)
    plt.plot(star1_loc[:,0],star1_loc[:,1],'r.',label='mass1')
    plt.plot(star2_loc[:,0],star2_loc[:,0],'b.',label='mass2')
    plt.plot(c[0],c[1],'g*',label='center of mass')
    plt.legend()
    plt.savefig('traj.png')