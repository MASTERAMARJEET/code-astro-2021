import numpy as np
import matplotlib.pyplot as plt

G = 1


class BinarySystem:
    """[summary]
    p1, p2: positions in speherical coordinates (numpy array of three numbers)
    omega: orbital frequency
    e: eccentricity
    """

    def __init__(self, m1, m2, semi_major, omega, e, dt=1) -> None:
        self.m1 = m1
        self.m2 = m2
        self.omega = omega
        self.e = e
        self.v1 = np.array([0, 0])
        self.v2 = np.array([0, 0])
        self.p = np.array([1, 2])
        self.q = np.array([3, 2])
        self.com = (self.m1 * self.p + self.m2 * self.q) / (self.m1 + self.m2)
        self.p1 = self.p - self.com
        self.p2 = self.q - self.com
        self.semi_major = semi_major
        self.dt = 1

    @property
    def force(self):
        r = self.p2 - self.p1
        r_norm = np.linalg.norm(r)
        r_unit = r / r_norm
        f = G * self.m1 * self.m2 / r_norm ** 2 * r_unit
        return f

    def update_position(self):
        self.p1 += (self.force / self.m1) * (self.dt ** 2) + self.v1 * self.dt
        self.p2 += (self.force / self.m2) * (self.dt ** 2) + self.v2 * self.dt
        return self.p1, self.p2


if __name__ == "__main__":
    binary = BinarySystem(1, 2, 0, 0, 2)
    # star1 = []
    # star2 = []
    for i in range(10):
        p1, p2 = binary.update_position()
        print(f"{p1=};{p2=}")
        plt.scatter(*p1)
        plt.scatter(*p2)
    # plt.legend()
    plt.show()
