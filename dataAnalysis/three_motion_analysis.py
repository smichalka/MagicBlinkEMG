import pyxdf
import matplotlib.pyplot as plt
import numpy as np
import pdb
import scipy.signal as filter
from scipy.fft import rfft, rfftfreq
from sklearn import svm
import sklearn.model_selection as model_selection
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

data_file_paths = [
    "dataFiles/threeMotionData/three_motion_one.xdf",
    "dataFiles/threeMotionData/three_motion_two.xdf",
    "dataFiles/threeMotionData/three_motion_three.xdf",
    "dataFiles/threeMotionData/three_motion_four.xdf",
    "dataFiles/threeMotionData/three_motion_five.xdf",
    "dataFiles/threeMotionData/three_motion_six.xdf",
    "dataFiles/threeMotionData/three_motion_seven.xdf"
    ]

streams, _ = pyxdf.load_xdf("dataFiles/threeMotionData/three_motion_one.xdf")
for stream in streams:
    if stream['info']['name'] == ['MyMarkerStream']:
        markers_time = stream['time_stamps']
i=0
total_times = 0
while i+1 < len(markers_time):
    total_times += (markers_time[i+1]-markers_time[i])*250
    i += 2
average_time_index_window = total_times*2/i

epoched_eeg_values = []
epoched_eeg_time = []
epoched_markers_time = []
epoched_markers_values = []

for file_path in data_file_paths:
    streams, _ = pyxdf.load_xdf(file_path)
    for stream in streams:
        if stream['info']['name'] == ['MyMarkerStream']:
            markers_values = stream['time_series']
            markers_time = stream['time_stamps']
        if stream['info']['name'] == ['obci_eeg1']:
            eeg_values = stream['time_series']
            eeg_time = stream['time_stamps']
    for i in range(8):
        channel = eeg_values[:,i]
        # yf = rfft(channel)
        # xf = rfftfreq(len(channel),1/250)
        # plt.plot(xf, np.abs(yf))
        # plt.show()
        b, a = filter.iirnotch(60, 5, 250)
        channel = filter.filtfilt(b, a, channel)
        channel = channel - np.mean(channel)
        # plt.plot(eeg_time, channel)
        # plt.show()
        # yf = rfft(channel)
        # xf = rfftfreq(len(channel),1/250)
        # plt.plot(xf, np.abs(yf))
        # plt.show()
        eeg_values[:,i] = channel
    eeg_values = eeg_values - np.mean(eeg_values)
    i = 0
    while i+1 < len(markers_time):
        index_start = (np.abs(eeg_time-markers_time[i])).argmin()
        index_stop = index_start + int(average_time_index_window)
        epoched_eeg_values.append(eeg_values[index_start:index_stop])
        epoched_eeg_time.append(eeg_time[index_start:index_stop] - eeg_time[index_start])
        epoched_markers_time.append([markers_time[i], markers_time[i+1]])
        epoched_markers_values.append(markers_values[i])
        i+=2
for i in range(len(epoched_eeg_time)):
    plt.plot(epoched_eeg_time[i], epoched_eeg_values[i])
# plt.show()

features = []

for epoch in epoched_eeg_values:
    variances = np.var(epoch, axis=0)
    mins = np.amin(epoch, axis=0)
    max = np.amax(epoch, axis=0)
    features.append(np.concatenate((mins, max)))
processed_markers = []
for marker in epoched_markers_values:
    processed_markers.append(marker[0])

X_train, X_test, y_train, y_test = model_selection.train_test_split(features, processed_markers, train_size=0.80, test_size=0.20, random_state=101)
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)
neigh_pred = neigh.predict(X_test)
accuracy = 0
for i in range(130):
    if neigh_pred[i] == y_test[i]:
        accuracy += 1/130
print(accuracy)