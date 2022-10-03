from py_vollib.black_scholes import black_scholes as bs
from py_vollib.black_scholes.greeks.analytical import delta, gamma, vega, theta, rho
from bs import *


S = 30
K = 40
T = 240 / 365
SIGMA = 0.3
R = 0.01
for Type in ['c', 'p']:
    print(Type)
    print(cal_bs(S, K, T, R, SIGMA, 'c'))
    print(bs('c', S, K, T, R, SIGMA))

    print(cal_delta(S, K, T, R, SIGMA, 'c'))
    print(delta('c', S, K, T, R, SIGMA))

    print(cal_gamma(S, K, T, R, SIGMA, 'c'))
    print(gamma('c', S, K, T, R, SIGMA))

    print(cal_vega(S, K, T, R, SIGMA, 'c'))
    print(vega('c', S, K, T, R, SIGMA))

    print(cal_theta(S, K, T, R, SIGMA, 'c'))
    print(theta('c', S, K, T, R, SIGMA))

    print(cal_rho(S, K, T, R, SIGMA, 'c'))
    print(rho('c', S, K, T, R, SIGMA))
