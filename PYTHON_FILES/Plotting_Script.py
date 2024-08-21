#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:52:07 2024

@author: user287
"""


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import scienceplots
import numpy as np
from scipy.optimize import curve_fit

# # Plotting single cluster size vs. angle plot for one bias voltage

# # Load CSV file
# file_path = '/home/user287/Summer_Project_2024/CSV_DATA/Telescope_Y_6.csv'
# data = pd.read_csv(file_path)

# # Extract columns
# angles = data['Angle']
# average_cluster_size = data['Average Cluster Size']
# standard_deviation = data['Standard Deviation']
# error_on_average = data['Error on Average']

# # Plotting average cluster size

# with plt.style.context(['science', 'no-latex']):
#     plt.rcParams['figure.dpi'] = 500
#     plt.errorbar(angles, average_cluster_size, yerr=error_on_average, fmt='o', ecolor='k', capthick=1, capsize=3, markersize=3, label='Data')
#     plt.xlabel(r'Angle (degrees)', fontsize=10)
#     plt.ylabel(r'Average Cluster Size', fontsize=10)
#     plt.title(r'Average Cluster Size vs. Angle for V$_{bias}$ = -6V', fontsize=12)
#     plt.show()




# Plotting average cluster size for all bias voltages

voltages = [0, 6, 9, 15, 20, 25, 30, 40, 50, 60]
plotting_voltages = [0, 6, 20, 30, 40, 50, 60]
#voltages = [25]
angles = []
average_cluster_size = []
standard_deviation = []
error_on_average = []

for voltage in voltages:
    # Load CSV file
    file_path = f'/home/user287/Summer_Project_2024/60V_Delpetion_TEST/RUN_3/CSV_DATA/Telescope_Y_{voltage}.csv'
    data = pd.read_csv(file_path)

    # Extract columns

    angles.append(data['Angle'])
    average_cluster_size.append(data['Average Cluster Size'])
    standard_deviation.append(data['Standard Deviation'])
    error_on_average.append(data['Error on Average'])

# # Plotting the data

# with plt.style.context(['science', 'no-latex']):
#     plt.rcParams['figure.dpi'] = 500
    
#     #plt.errorbar(angles[0], np.zeros(13), yerr=np.zeros(13), fmt='o', ecolor='k', capthick=1, capsize=3, markersize=3, label= 'V$_{bias}$ = ' + f'-0V')
#     #plt.errorbar(np.tan(angles[0]*np.pi/180), np.zeros(13), yerr=np.zeros(13), fmt='o', ecolor='k', capthick=1, capsize=3, markersize=3, label= 'V$_{bias}$ = ' + f'-0V')

#     for i, voltage in enumerate(voltages):
#         #plt.errorbar(angles[i], average_cluster_size[i], yerr=error_on_average[i], fmt='o', ecolor='k', capthick=1, capsize=3, markersize=3, label= 'V$_{bias}$ = ' + f'-{voltage}V')
#         plt.errorbar(np.tan(np.pi*angles[i]/180), average_cluster_size[i], yerr=error_on_average[i], fmt='o', ecolor='k', capthick=1, capsize=3, markersize=3, label= 'V$_{bias}$ = ' + f'-{voltage}V')
#     #plt.xlabel(r'Angle (degrees)', fontsize=10)
#     plt.xlabel(r'Angle tan(degrees)', fontsize=10)
#     #plt.ylabel('Average Cluster Size', fontsize=10)
#     plt.ylabel('Average Cluster Size', fontsize=10)
#     plt.title(r'Average Cluster Size vs. Angle for increasing V$_{bias}$', fontsize=12)
#     plt.legend(fontsize = 7)
#     plt.show()


# # Plotting average cluster size for all bias voltages at 0 degrees

# voltages = [6, 9, 15, 20, 25]
# angles = []
# average_cluster_size = []
# standard_deviation = []
# error_on_average = []

# for voltage in voltages:
#     # Load CSV file
#     file_path = f'/home/user287/Summer_Project_2024/Cluster_Size_1_TEST/CSV_DATA/Telescope_X_{voltage}.csv'
#     data = pd.read_csv(file_path)

#     # Extract columns

#     angles.append(data['Angle'])
#     average_cluster_size.append(data['Average Cluster Size'])
#     standard_deviation.append(data['Standard Deviation'])
#     error_on_average.append(data['Error on Average'])

# # Plotting the data

# with plt.style.context(['science', 'no-latex']):
#     plt.rcParams['figure.dpi'] = 500
    
#     cluster_0deg = []
#     cluster_0deg_error = []
#     for i in range(len(average_cluster_size)):
#         cluster_0deg.append(average_cluster_size[i][0])
#         cluster_0deg_error.append(average_cluster_size[i][0])
        
        
#     plt.errorbar(voltages, cluster_0deg)
#     plt.xlabel(r'V$_{bias}$', fontsize=10)
#     plt.ylabel('Cluster size at 0 deg', fontsize=10)
#     plt.title(r'Average Cluster Size vs.V$_{bias}$ for 0 degrees', fontsize=12)
#     plt.legend(fontsize = 7)
#     plt.show()


# Fitting the data to determine depletion depth

def linear_model(x, m, c):
    return m*x + c

slopes = []
intercepts = []
depletion = []
depletion_error = []
calculated_depletion_width = []

for voltage in voltages:
    width = 100/np.sqrt(60)*np.sqrt(voltage)
    calculated_depletion_width.append(width)

for i, voltage in enumerate(voltages):
    popt, pcov = curve_fit(linear_model, xdata=np.tan(angles[i][6:]*np.pi/180), ydata=average_cluster_size[i][6:], sigma=error_on_average[i][6:], absolute_sigma=True)
        
    slope, intercept = popt
        
    slope_error = np.sqrt(np.diag(pcov))[1]
        
    #slope, intercept = np.polyfit(np.tan(angles[i][6:]*np.pi/180), (average_cluster_size[i][6:]-average_cluster_size[i][0]), 1)
    depletion.append(slope*36.4)
    slopes.append(slope)
    intercepts.append(intercept)
    depletion_error.append(36.4*slope_error)
    


# Plotting the cluster size data

tan_points = np.linspace(0, 60, num=100)
colours = ['#1F77B4',
           '#2CA02C',
           '#FF7F0E',
           '#D62728',
           '#9467BD',
           '#4D4D4D',
           '#A9A9A9',
           '#964B00']

with plt.style.context(['science', 'no-latex']):
    plt.rcParams['figure.dpi'] = 500
    
    #plt.errorbar(angles[0], np.zeros(13), yerr=np.zeros(13), fmt='o', ecolor='k', capthick=1, capsize=3, markersize=3, label= 'V$_{bias}$ = ' + f'-0V')
    #plt.errorbar(np.tan(angles[0]*np.pi/180), np.zeros(13), yerr=np.zeros(13), fmt='o', ecolor='k', capthick=1, capsize=3, markersize=3, label= 'V$_{bias}$ = ' + f'-0V')

    for i, voltage in enumerate(plotting_voltages):
        #plt.errorbar(angles[i], average_cluster_size[i], yerr=error_on_average[i], fmt='o', ecolor='k', capthick=1, capsize=3, markersize=3, label= 'V$_{bias}$ = ' + f'-{voltage}V')
        
        y_fit = slopes[i] * np.tan(tan_points*np.pi/180) + intercepts[i]
        
        plt.errorbar(np.tan(tan_points*np.pi/180), y_fit, fmt='--', color=colours[i])
        plt.errorbar(np.tan(np.pi*angles[i]/180), average_cluster_size[i], yerr=error_on_average[i],
                     fmt='o', ecolor='k', capthick=1, capsize=3, markersize=3, label= 'V$_{bias}$ = ' + f'-{voltage}V', color = colours[i])
    plt.axvline(0.5, label='Fitting cut-off')
    #plt.xlabel(r'Angle (degrees)', fontsize=10)
    plt.xlabel(r'Angle tan(degrees)', fontsize=10)
    #plt.ylabel('Average Cluster Size', fontsize=10)
    plt.ylabel('Average Cluster Size', fontsize=10)
    plt.title(r'Average Cluster Size vs. Angle for increasing V$_{bias}$', fontsize=12)
    plt.legend(fontsize = 7)
    plt.show()



# Plotting the fitted depletion depth data

x_points = np.linspace(0, 60, num=100)
y_points = 100*np.sqrt(x_points/60)

with plt.style.context(['science', 'no-latex']):
    plt.rcParams['figure.dpi'] = 500 
    plt.errorbar(voltages, depletion, yerr = depletion_error,  fmt='o', ecolor='k', capthick=1, capsize=3, markersize=3, label='Fitted depletion depth')
    #plt.plot(voltages, calculated_depletion_width, 'r', label='Calculated depletion depth')
    plt.plot(x_points, y_points, 'r', label='Calculated depletion depth')
    plt.xlabel(r'V$_{bias}$', fontsize=10)
    plt.ylabel(r'Depletion depth ($\mu$m)', fontsize=10)
    plt.title(r'Depletion depth vs. V$_{bias}$', fontsize=12)
    plt.legend(fontsize = 7)
    plt.show()

    
# # Plotting depletion depth

# depletion_depth = 36.4*(average_cluster_size-average_cluster_size[0])/np.tan(angles*np.pi/180)
# depletion_depth_error = (36.4*error_on_average)/np.tan(angles*np.pi/180)

# with plt.style.context(['science', 'no-latex']):
#     plt.rcParams['figure.dpi'] = 500
#     plt.errorbar(angles, depletion_depth, yerr=depletion_depth_error, fmt='o', ecolor='k', capthick=1, capsize=3, markersize=3, label='Data')
#     plt.xlabel(r'Angle (degrees)', fontsize=10)
#     plt.ylabel(r'Depletion depth ($\mu$m)', fontsize=10)
#     plt.title(r'Depletion depth vs. Angle for V$_{bias}$ = -6V', fontsize=12)
#     plt.legend()
#     plt.show()


# # Plotting depletion depth for all bias voltages
    
# voltages = [0, 6, 9, 15, 20, 25, 30]
# angles = np.linspace(0, 60, 13)
# average_cluster_size = []
# standard_deviation = []
# error_on_average = []
# depletion_depth = []
# depletion_depth_error = []

# for voltage in voltages:
#     # Load CSV file
#     file_path = f'/home/user287/Summer_Project_2024/CSV_DATA/Telescope_Y_{voltage}.csv'
#     data = pd.read_csv(file_path)

#     # Extract columns

#     average = data['Average Cluster Size'].to_numpy()
#     standard_deviation = data['Standard Deviation'].to_numpy()
#     error = data['Error on Average'].to_numpy()
    
#     average_cluster_size.append(average)
#     error_on_average.append(error)
    
#     # Calculate depletion depths
    
#    #depletion = 
#    # d_error = 
#     depletion_depth.append(36.4*(average-average[0])/np.tan(angles*np.pi/180))
#     depletion_depth_error.append((36.4*error)/np.tan(angles*np.pi/180))
        
#     #depletion_depth.append()
#     #depletion_depth_error.append()

# with plt.style.context(['science', 'no-latex']):
#     plt.rcParams['figure.dpi'] = 500
#     for i, voltage in enumerate(voltages):
#         plt.errorbar(angles, depletion_depth[i], yerr=depletion_depth_error[i], fmt='o', ecolor='k', capthick=1, capsize=3, markersize=3,label= 'V$_{bias}$ = ' + f'-{voltage}V')
#     plt.xlabel(r'Angle (degrees)', fontsize=10)
#     plt.ylabel(r'Depletion depth ($\mu$m)', fontsize=10)
#     plt.title(r'Depletion depth vs. Angle for increasing V$_{bias}$', fontsize=12)
#     plt.legend(fontsize = 7)
#     plt.show()
    
    
    
    
    
# # Overlay plot of cluster size histograms for a single bias voltage for each angle

# BinCentre = []
# content = []
# Error = []
 
# for angle in range(0, 65, 5):
#     hist_file = f'/home/user287/Summer_Project_2024/CSV_DATA/Telescope_Y_30_{angle}deg_Hist.csv'
#     hist_data = pd.read_csv(hist_file)
#     BinCentre.append(hist_data['BinCentre'])
#     content.append(hist_data['Content'])
#     Error.append(hist_data['Error'])

# with plt.style.context(['science', 'no-latex']):
#     plt.rcParams['figure.dpi'] = 500
    
#     for i, angle in enumerate(range(0, 65, 5)):
#         if i!=12:
#             continue
#         plt.hist(BinCentre[i], weights=content[i], bins=len(BinCentre[i]), label=f'{angle} degrees', histtype='step')
    
#     #plt.hist(BinCentre[0], weights=content[0], bins=len(BinCentre[0]), label=f'0 degrees', histtype='step')
#     #plt.hist(BinCentre[1], weights=content[1], bins=len(BinCentre[1]), label=f'5 degrees', histtype='step')
#     plt.xlim([0, 10])
#     plt.xlabel(r'Cluster size', fontsize=10)
#     plt.ylabel(r'Cluster', fontsize=10)
#     plt.yscale('log')
#     plt.title(r'Cluster size histograms for increasing incident angle', fontsize=12)
#     plt.legend(title='Incident Angle')
#     plt.show()
    