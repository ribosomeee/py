#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 18:56:23 2019

@author: tianjianhao
"""
import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

from matplotlib.backends.backend_pdf import PdfPages



plt.rcParams['pdf.fonttype'] = 42

plt.rcParams['font.family'] = 'Calibri'



if __name__ == '__main__':

    data = pd.read_csv('CPIAUCSL.csv')



    # Compute monthly inflation

    print('PART 1')

    data['inflation'] = (data['CPIAUCSL'] - data['CPIAUCSL'].shift(1).fillna(0)) / data['CPIAUCSL'].shift(1).fillna(0)

    print(data['inflation'].iloc[1:].head())


    # Split and compute mean and std

    print('--------------------')

    print('PART 2')

    half1 = data.iloc[1:int(data.shape[0] / 2), :]
    print(half1)

    half2 = data.iloc[int(data.shape[0] / 2):, :]

    print('Mean {}, std {} for first part'.format(half1['inflation'].mean(), half1['inflation'].std()))

    print('Mean {}, std {} for first part'.format(half2['inflation'].mean(), half2['inflation'].std()))

    print('--------------------')

    print('PART 3')

    with PdfPages('MITID_inflation.pdf') as pp:

        plt.plot(data['DATE'], data['inflation'], label = 'Inflation')

        plt.plot(data['DATE'], np.ones(data['DATE'].shape[0]) * half1['inflation'].mean(), c='r', label = 'First half mean')

        plt.plot(data['DATE'], np.ones(data['DATE'].shape[0]) * half2['inflation'].mean(), c='c', label = 'Second half mean')

        plt.xticks(data['DATE'][::100], rotation=30)

        plt.title('Inflation graph', fontsize=10)

        plt.xlabel('Time', fontsize=8)

        plt.ylabel('Inflation', fontsize=8)

        plt.legend()

        plt.grid(True)

        pp.savefig()

    print('Saved plot to MITID_inflation.pdf')
    
   