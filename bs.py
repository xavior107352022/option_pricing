import numpy as np
from scipy.stats import norm


def cal_d1(s, k, t, r, sigma):
    return (np.log(s / k) + (r + 0.5 * (sigma ** 2) * t)) / (sigma * np.sqrt(t))


def cal_d2(s, k, t, r, sigma):
    return cal_d1(s, k, t, r, sigma) - sigma * np.sqrt(t)


def cal_bs(s, k, t, r, sigma, o_type='c'):
    d1 = cal_d1(s, k, t, r, sigma)
    d2 = cal_d2(s, k, t, r, sigma)
    if o_type == 'c':
        return s * norm.cdf(d1) - k * np.exp(-r * t) * norm.cdf(d2)
    if o_type == 'p':
        return k * np.exp(-r * t) * norm.cdf(-d2) - s * norm.cdf(-d1)


def cal_delta(s, k, t, r, sigma, o_type='c'):
    d1 = cal_d1(s, k, t, r, sigma)
    if o_type == 'c':
        return norm.cdf(d1)
    if o_type == 'p':
        return -norm.cdf(-d1)


def cal_gamma(s, k, t, r, sigma, o_type='c'):
    d1 = cal_d1(s, k, t, r, sigma)
    return norm.pdf(d1) / (s * sigma * np.sqrt(t))


def cal_vega(s, k, t, r, sigma, o_type='c'):
    d1 = cal_d1(s, k, t, r, sigma)
    return s * norm.pdf(d1) * np.sqrt(t) / 100


def cal_theta(s, k, t, r, sigma, o_type='c'):
    d1 = cal_d1(s, k, t, r, sigma)
    d2 = cal_d2(s, k, t, r, sigma)
    if o_type == 'c':
        return (-s * norm.pdf(d1) * sigma / (2 * np.sqrt(t)) - r * k * np.exp(-r * t) * norm.cdf(d2)) / 365
    if o_type == 'p':
        return (-s * norm.pdf(d1) * sigma / (2 * np.sqrt(t)) + r * k * np.exp(-r * t) * norm.cdf(-d2)) / 365


def cal_rho(s, k, t, r, sigma, o_type='c'):
    d2 = cal_d2(s, k, t, r, sigma)
    if o_type == 'c':
        return k * t * np.exp(-r * t) * norm.cdf(d2) / 100
    if o_type == 'p':
        return -k * t * np.exp(-r * t) * norm.cdf(-d2) / 100
