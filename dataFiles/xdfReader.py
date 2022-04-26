import pyxdf
import matplotlib.pyplot as plt
import numpy as np
import mne

streams, header = pyxdf.load_xdf("dataFiles/three_motion_seven.xdf")
print(streams)
for stream in streams:
    y = stream['time_series']
    print(stream['info']['name'])
    print(np.shape(stream['time_series']))

    if isinstance(y, list):
        # list of strings, draw one vertical line for each marker
        for timestamp, marker in zip(stream['time_stamps'], y):
            plt.axvline(x=timestamp)
            #print(f'Marker "{marker[0]}" @ {timestamp:.2f}s')
        
    elif isinstance(y, np.ndarray):
        # numeric data, draw as lines
        print("Here")
        plt.plot(stream['time_stamps'], y,)
        # if multiple options for data, need to expand this to include selection by name
        if stream["info"]["type"]==['EEG']:
          data = stream["time_series"].T
          sfreq = float(stream["info"]["nominal_srate"][0])
          info = mne.create_info(int(stream["info"]['channel_count'][0]),sfreq,"eeg")
          first_samp = stream["time_stamps"][0]
    else:
        raise RuntimeError('Unknown stream format')
# plt.axis([2600, 2900, -200, 200])
# plt.ylim([-200, 200])
plt.show()
