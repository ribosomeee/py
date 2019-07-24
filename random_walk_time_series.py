#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 22:38:33 2019

@author: tianjianhao
"""

import numpy as np

import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages





def random_walk(x, c, t):

    series = [x]

    for time in range(1, t):

        xx = x + np.random.choice([-1,1]) * c

        x = xx

        series.append(xx)

    return series





if __name__ == '__main__':

    t = 60; c = 0.1; x = 1

    times = np.arange(t)

    series = random_walk(x, c, t)

    plt.rcParams['pdf.fonttype'] = 42

    plt.rcParams['font.family'] = 'Calibri'

    with PdfPages('MITID_path.pdf') as pp:

        plt.plot(times, series)

        plt.title('Random walk example', fontsize=10)

        plt.xlabel('Time', fontsize=8)

        plt.ylabel('Value', fontsize=8)

        plt.grid(True)

        pp.savefig()

        plt.close()

