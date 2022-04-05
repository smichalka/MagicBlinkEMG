from pyrsistent import thaw
import pyxdf
import matplotlib.pyplot as plt
import numpy as np
import mne
from scipy.fft import rfft, rfftfreq
import scipy.signal as filter
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

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
plt.title("Pre-Filtered Data")
# plt.show()
plt.clf()


# fourier analysis
total_time = eeg_time[-1] - eeg_time[0]
yf = rfft(eeg_data)
xf = rfftfreq(len(eeg_data), 1/500)
plt.plot(xf, np.abs(yf))
plt.xlim([0, 200])
plt.ylim([-1, 5000])
plt.title("Pre-Filtered FFT")
plt.show()
plt.clf()

# notch filter implementation
eeg_data = np.float64(eeg_data)
b, a = filter.iirnotch(120, 30, 500)
filtered_data_1 = filter.filtfilt(b, a, eeg_data)
b, a = filter.iirnotch(60, 30, 500)
filtered_data = filter.filtfilt(b, a, filtered_data_1)
plt.plot(eeg_time, filtered_data)
plt.title("Filtered Data")
plt.show()

yf_filt = rfft(filtered_data)
xf_filt = rfftfreq(len(filtered_data), d=1/500)
plt.plot(xf_filt, np.abs(yf_filt))
plt.xlim([0, 200])
plt.ylim([-1, 5000])
plt.title("Filtered FFT")
plt.show()

# plt.plot(eeg_time, mean_centered_eeg_data)
# plt.show()

# segmentation according to each marker
upper_segment_threshold = .2
lower_segment_threshold = -.2

times = []
clean_data = []

#for i in range(len(markers_time)):
for i in range(1, 29):
    lower_time = markers_time[i] + lower_segment_threshold
    upper_time = markers_time[i] + upper_segment_threshold
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
    plt.plot(eeg_time[lower_index:upper_index] - eeg_time[lower_index], filtered_data[lower_index:upper_index] - sum(filtered_data[lower_index:upper_index])/len(filtered_data[lower_index:upper_index]))
    plt.plot(markers_time[i] - eeg_time[lower_index], markers_data[i], 'ro')
    clean_data.append(filtered_data[lower_index:upper_index] - sum(filtered_data[lower_index:upper_index])/len(filtered_data[lower_index:upper_index]))
    times.append(eeg_time[lower_index:upper_index] - eeg_time[lower_index])
    print(upper_index-lower_index)
plt.xlim([0, .6])
# plt.show()
print(eeg_time[1700])
print(len(markers_data))

data_none = []
for i in range(1, 29):
    data_none.append(filtered_data[1700+10*i:1850*10*i] - sum(filtered_data[1700+10*i:1850*10*i])/len(filtered_data[1700+10*i:1850*10*i]))



data = []
blink_state = []
for i in range(len(clean_data)):
    data.append([max(clean_data[i]), 0])
    blink_state.append(1)
    data.append([max(data_none[i]), 0])
    blink_state.append(0)

training_threshold = int(.75 * len(data))

training_x = data[:training_threshold]
training_y = blink_state[:training_threshold]
testing_x = data[training_threshold:]
testing_y = blink_state[:training_threshold]

clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
clf.fit(training_x, training_y)

predictions = clf.predict(testing_x)

accuracy = 0
for i in range(len(predictions)):
    if predictions[i] == testing_y[i]:
        accuracy += 1/len(predictions)

print(accuracy)