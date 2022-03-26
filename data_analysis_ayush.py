import pyxdf
import matplotlib.pyplot as plt
import numpy as np
import mne
from scipy.fft import fft, fftfreq
import mne.filter as filter

#xdf reader to collect numpy arrays of markers and eeg data
streams, header = pyxdf.load_xdf("markersPlusEKG.xdf")
for stream in streams:
    y = stream['time_series']
    print(stream['info']['name'])
    print(np.shape(stream['time_series']))
    if stream['info']['name'] == ['Blinky']:
        markers_data = y
        markers_time = stream['time_stamps']
    if stream['info']['name'] == ['obci_eeg1']:
        eeg_data = y[:,0]
        eeg_time = stream['time_stamps']
    if isinstance(y, list):
        # list of strings, draw one vertical line for each marker
        for timestamp, marker in zip(stream['time_stamps'], y):
            plt.axvline(x=timestamp)
            #print(f'Marker "{marker[0]}" @ {timestamp:.2f}s')
        
    elif isinstance(y, np.ndarray):
        # numeric data, draw as lines
        print(stream['time_stamps'])
        plt.plot(stream['time_stamps'], y[:,0], 'o')
        # if multiple options for data, need to expand this to include selection by name
        if stream["info"]["type"]==['EEG']:
          data = stream["time_series"].T
          sfreq = float(stream["info"]["nominal_srate"][0])
          info = mne.create_info(int(stream["info"]['channel_count'][0]),sfreq,"eeg")
          first_samp = stream["time_stamps"][0]
    else:
        raise RuntimeError('Unknown stream format')
#plt.show()
plt.clf()


# fourier analysis
total_time = eeg_time[-1] - eeg_time[0]
sampling_rate = len(eeg_data)/total_time
print("total time: " + str(sampling_rate))
yf = fft(eeg_data)
xf = fftfreq(len(eeg_data), 1/sampling_rate)
# plt.plot(xf, np.abs(yf))
# plt.xlim([0, 0.2])
# plt.show()

# notch filter implementation
print(eeg_data)
eeg_data = np.float64(eeg_data)
print(type(eeg_data[0]))
filtered_data = filter.notch_filter(eeg_data, sampling_rate, 60)
# plt.plot(eeg_time, filtered_data)
# plt.show()

# mean centering the data
mean_centered_eeg_data = eeg_data - sum(eeg_data)/len(eeg_data)
# plt.plot(eeg_time, mean_centered_eeg_data)
# plt.show()

# segmentation according to each marker
upper_segment_threshold = 2
lower_segment_threshold = -1
# print(eeg_time)
# lower_time = markers_time[5] + lower_segment_threshold
# upper_time = markers_time[0] + upper_segment_threshold
# temp = np.abs(eeg_time - lower_time)
# print(markers_time[3])
# nearest_time = min(temp) + lower_time
# print(nearest_time)
# blah = np.where(eeg_time==nearest_time)
# print(blah)
# int_eeg_time = np.empty(0)
# for i in range(len(eeg_time)):
#     np.append(int_eeg_time, int(eeg_time[i]))
# blah = np.where(int_eeg_time==int(nearest_time))
# print(blah)
for i in range(len(markers_time)):
    lower_time = markers_time[i] + lower_segment_threshold
    upper_time = markers_time[i] + upper_segment_threshold
    print(lower_time, upper_time)
    lower_error = None
    upper_error = None
    lower_index = None
    upper_index = None
    for j in range(len(eeg_time)):
        if lower_error is None or lower_error > abs(lower_time-eeg_time[j]):
            lower_error = abs(lower_time - eeg_time[j])
            lower_index = j
        if upper_error is None or upper_error > abs(upper_time-eeg_time[j]):
            upper_error = abs(upper_time - eeg_time[j])
            upper_index = j
    print(lower_index, upper_index)
    print(eeg_time[lower_index], eeg_time[upper_index])
    plt.plot(eeg_time[lower_index:upper_index], eeg_data[lower_index:upper_index])
    plt.plot(markers_time, markers_data + 63000, 'ro')
    plt.ylim([60000, 70000])
    plt.xlim([eeg_time[lower_index], eeg_time[upper_index]])
    plt.show()