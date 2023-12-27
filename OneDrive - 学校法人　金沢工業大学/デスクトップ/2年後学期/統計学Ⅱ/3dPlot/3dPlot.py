# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 20:25:33 2023

@author: rikutotomita
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

###ここのr"C:\"の部分を変更する###
path_csv = r"C:\Users\rikutotomita\OneDrive - 学校法人　金沢工業大学\デスクトップ\2年後学期\統計学Ⅱ\vegitable.csv"

# Load data from CSV
rows = []
with open(path_csv, encoding="shift-jis") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

# Check if data is empty
if not rows:
    print("Error: No data found in the CSV file.")
else:
    # Convert data to numpy array
    data = np.array(rows[1:], dtype=float)

    # Ensure data is 2-dimensional
    if data.ndim == 1:
        data = data.reshape((1, -1))

    # Extracting the three columns from the data
    x = data[:, 1]
    y = data[:, 2]
    z = data[:, 3]

    # Creating a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)

    # Setting labels for the axes
    ax.set_xlabel('Column 1')
    ax.set_ylabel('Column 2')
    ax.set_zlabel('Column 3')

    # Display the plot
    plt.show()
