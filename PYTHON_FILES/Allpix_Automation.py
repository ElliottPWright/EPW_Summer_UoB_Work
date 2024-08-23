#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:57:38 2024

@author: user287
"""

import os
import subprocess
import ROOT
import csv
import shutil

# Function to update the detector configuration file
def update_orientation_config(detector_file, angle):
    with open(detector_file, 'r') as file:
        lines = file.readlines()
   
    with open(detector_file, 'w') as file:
        i = 0
        for line in lines:
            if 'orientation' in line:
                i+=1
                if i == 1:
                    file.write(f'orientation = {angle}deg 0deg 0deg\n')
                else:
                    file.write(line)
            else:
                file.write(line)

                
                
# Function to run the simulation
def run_simulation(simulation_config_file):
    subprocess.run(['allpix', '-c', simulation_config_file], check=True, cwd = '/home/user287/allpix-squared/Summe_Internship/')
    

# Function to extract cluster size data from the TTree
def extract_cluster_size_data(output_file, raw_filename_x, raw_filename_y):
    file = ROOT.TFile(output_file)
    hist_x = file.Get("DetectorHistogrammer/detector4/cluster_size/cluster_size_x")
    hist_y = file.Get("DetectorHistogrammer/detector4/cluster_size/cluster_size_y")
    
    mean_x = hist_x.GetMean()
    sigma_x = hist_x.GetRMS()
    
    mean_y = hist_y.GetMean()
    sigma_y = hist_y.GetRMS()
    
    mean_error_x = hist_x.GetMeanError()
    mean_error_y = hist_y.GetMeanError()
    
    with open(raw_filename_x, 'w', newline='') as rawfile:
        writer = csv.writer(rawfile, delimiter=',')
        writer.writerow(['Bin','BinCentre','Content', 'Error'])
        
        for bin in range(1, hist_x.GetNbinsX() + 1):
            bin_centre = hist_x.GetBinCenter(bin)
            content = hist_x.GetBinContent(bin)
            error = hist_x.GetBinError(bin)
            writer.writerow([bin, bin_centre, content, error])
    
    with open(raw_filename_y, 'w', newline='') as rawfile:
        writer = csv.writer(rawfile, delimiter=',')
        writer.writerow(['Bin','BinCentre','Content', 'Error'])
        
        for bin in range(1, hist_y.GetNbinsX() + 1):
            bin_centre = hist_y.GetBinCenter(bin)
            content = hist_y.GetBinContent(bin)
            error = hist_y.GetBinError(bin)
            writer.writerow([bin, bin_centre, content, error])

    file.Close()
    return mean_x, sigma_x, mean_error_x, mean_y, sigma_y, mean_error_y

# Function to save cluster size data to CSV
def save_to_csv(filename, mean_data, standard_deviation_data, mean_error):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Angle','Average Cluster Size', 'Standard Deviation', 'Error on Average'])
        angle = 0
        for mean, standard_deviation, mean_error in zip(mean_data, standard_deviation_data, mean_error):
            writer.writerow([angle, mean, standard_deviation, mean_error])
            angle+=5
            
# def raw_data_saver(raw_filename, hist):
#     with open(raw_filename, 'w', newline='') as rawfile:
#         writer = csv.writer(rawfile, delimiter=',')
#         writer.writerow(['Bin','BinCentre','Content', 'Error'])
        
#         for bin in range(1, hist.GetNbinsX() + 1):
#             bin_centre = hist.GetBinCenter(bin)
#             content = hist.GetBinContent(bin)
#             error = hist.GetBinError(bin)
#             writer.writerow([bin, bin_centre, content, error])


# Main function to run the automation
def main():
    bias_voltage = 30
    detector_file = '/home/user287/allpix-squared/Summe_Internship/Detector.conf'
    simulation_config_file = 'FullSim.conf'
    output_dir = f'/home/user287/Summer_Project_2024/ROOT_FILES/{bias_voltage}V'  # Specify the directory to save the ROOT files

    x_csv_file = f'/home/user287/Summer_Project_2024/CSV_DATA/Telescope_X_{bias_voltage}.csv'
    y_csv_file = f'/home/user287/Summer_Project_2024/CSV_DATA/Telescope_Y_{bias_voltage}.csv'
   
    x_mean_data = []
    y_mean_data = []
    x_standard_deviation_data = []
    y_standard_deviation_data = []
    x_error_data = []
    y_error_data = []

    for angle in range(0, 65, 5):
        print(f'Running simulation with orientation angle: {angle} degrees')
       
        # Update the configuration file
        update_orientation_config(detector_file, angle)
       
        # Run the simulation
        run_simulation(simulation_config_file)
        
        # Save the ROOT file
        input_file = '/home/user287/allpix-squared/Summe_Internship/output/modules.root'
        output_file = os.path.join(output_dir, f'Telescope_{bias_voltage}_{angle}Deg.root')
        shutil.copy(input_file, output_file) 
       
        # Extract cluster size data
        raw_filename_x = f'/home/user287/Summer_Project_2024/CSV_DATA/Telescope_X_{bias_voltage}_{angle}deg_Hist.csv'
        raw_filename_y = f'/home/user287/Summer_Project_2024/CSV_DATA/Telescope_Y_{bias_voltage}_{angle}deg_Hist.csv'
        
        mean_x, sigma_x, mean_error_x, mean_y, sigma_y, mean_error_y = extract_cluster_size_data(output_file, raw_filename_x, raw_filename_y)
        print(f'X-axis cluster sizes for angle {angle}: Mean = {mean_x}, RMS = {sigma_x}')
        print(f'Y-axis cluster sizes for angle {angle}: Mean = {mean_y}, RMS = {sigma_y}')
       
        # raw_data_saver(raw_filename_x, hist_x) 
        # raw_data_saver(raw_filename_y, hist_y)
        
        x_mean_data.append(mean_x)
        x_standard_deviation_data.append(sigma_x)
        x_error_data.append(mean_error_x)
        
        y_mean_data.append(mean_y)
        y_standard_deviation_data.append(sigma_y)
        y_error_data.append(mean_error_y)
   
    # Save the cluster size data to CSV files
    save_to_csv(x_csv_file, x_mean_data, x_standard_deviation_data, x_error_data)
    save_to_csv(y_csv_file, y_mean_data, y_standard_deviation_data, y_error_data)

if __name__ == '__main__':
    main()