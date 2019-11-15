class Fluid:

    def __init__(self, mu, rho, alpha, Pr):
        self.mu = mu
        self.rho = rho
        self.alpha = alpha
        self.Pr = Pr
        self.nu = mu/rho
        self.phi = mu/alpha


