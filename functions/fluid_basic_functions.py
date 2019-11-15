import numpy as np

def get_meanvelocity(Re,nu,L):
    # Re -> Bulk flow reynolds number
    # nu -> laminar viscosity
    # L -> length scale (total channel height)
    U = (Re*nu)/(L)
    return U

def get_muSutherland(mu0,T,Tref,C1,S):
    mu = mu0*(T/Tref)**(3/2)*((Tref+S)/(T+S))
    return mu


def get_turbkineticenergy(U,I):
    # U -> bulk velocity
    # I -> turbulence intensity
    k = (3/2)*(U*I)**2
    return k

def get_epsilon(k,h):
    # Cmu -> coefficient ~ 0.09
    # k -> estimated turbulent kinetic energy
    # h-> length scale for friction
    Cmu = 0.09
    epsilon = Cmu**(3/4) * k**(3/2)/h
    return epsilon

def get_omega(k,epsilon):
    Cmu = 0.09
    omega = epsilon/(Cmu*k)
    return omega

def get_nutkOmega(k,omega):
    nut = k/omega
    return nut