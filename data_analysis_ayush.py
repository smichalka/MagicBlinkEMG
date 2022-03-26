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
    if stream['info']['name'] == 'Blinky':
        markers_data = y
        markers_time = stream['time_stamps']
    if stream['info']['name'] == ['obci_eeg1']:
        print("Here")
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
plt.plot(xf, np.abs(yf))
plt.xlim([0, 0.2])
plt.show()

# notch filter implementation
print(eeg_data)
for i in range(0, len(eeg_data)):
    eeg_data[i] = int(eeg_data[i])
filtered_data = filter.notch_filter(eeg_data, sampling_rate, 60)
plt.plot(eeg_time, filtered_data)
plt.show()