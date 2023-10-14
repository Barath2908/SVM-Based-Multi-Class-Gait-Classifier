import pandas as pd
import matplotlib.pyplot as plt

# load data from csv file
df = pd.read_csv('C:/Users/ibra5/Desktop/EMG data 1.5/gait cycle classifier/Gait-Cycle-Classifier-master/datasets/walkData1.csv',skiprows=1, header=0)

# extract 'Timestamp (ms)' and 'gyro.y' columns
time_data = df['gyro.y']
gyro_data = df['Timestamp2']

# plot the data
plt.plot(gyro_data, time_data)

# set title and labels for the plot
plt.title('Gyro.y data')
plt.xlabel('Time (ms)')
plt.ylabel('Gyro.y')

marker_times = [978, 2167, 3347, 4507, 5646, 6957]
labels = ['HS', 'HS', 'HS', 'HS', 'HS', 'HS']
for i, time in enumerate(marker_times):
    plt.axvline(x=time, color='orange', linestyle='--')
    plt.text(time, plt.ylim()[1] * 0.9, labels[i], ha='center')
    
# add marker lines at specified time values
marker_times = [1097, 2277, 3446, 4596, 5757, 7018]  # specify the times where you want to place markers
labels = ['FF', 'FF', 'FF', 'FF', 'FF', 'FF']
for i, time in enumerate(marker_times):
    plt.axvline(x=time, color='green', linestyle='--')
    plt.text(time, plt.ylim()[1] * 0.9, labels[i], ha='center')
    
# add marker lines at specified time values
marker_times = [1296, 2447, 3627, 4768, 5927, 7177]  # specify the times where you want to place markers
labels = ['MST', 'MST', 'MST', 'MST', 'MST', 'MST']
for i, time in enumerate(marker_times):
    plt.axvline(x=time, color='blue', linestyle='--')
    plt.text(time, plt.ylim()[1] * 0.9, labels[i], ha='center')
    
# add marker lines at specified time values
marker_times = [1526, 2696, 3887, 5037, 6257]  # specify the times where you want to place markers
labels = ['HO', 'HO', 'HO', 'HO', 'HO', 'HO']
for i, time in enumerate(marker_times):
    plt.axvline(x=time, color='yellow', linestyle='--')
    plt.text(time, plt.ylim()[1] * 0.9, labels[i], ha='center')
    
# add marker lines at specified time values
marker_times = [1707, 2887, 4057, 5226, 6407]  # specify the times where you want to place markers
labels = ['TO', 'TO', 'TO', 'TO', 'TO', 'TO']
for i, time in enumerate(marker_times):
    plt.axvline(x=time, color='brown', linestyle='--')
    plt.text(time, plt.ylim()[1] * 0.9, labels[i], ha='center')
    
# add marker lines at specified time values
marker_times = [1887, 3067, 4227, 5387, 6577]  # specify the times where you want to place markers
labels = ['MS', 'MS', 'MS', 'MS', 'MS', 'MS']
for i, time in enumerate(marker_times):
    plt.axvline(x=time, color='pink', linestyle='--')
    plt.text(time, plt.ylim()[1] * 0.9, labels[i], ha='center')

# show the plot
plt.show()
