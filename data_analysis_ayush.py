import pyxdf
import matplotlib.pyplot as plt
import numpy as np

streams, header = pyxdf.load_xdf("sub-P001_ses-S001_task-Default_run-001_eeg.xdf")
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
        plt.plot(stream['time_stamps'], y, 'o')
        
        # if multiple options for data, need to expand this to include selection by name
        if stream["info"]["type"]==['EEG']:
          data = stream["time_series"].T
          sfreq = float(stream["info"]["nominal_srate"][0])
          info = mne.create_info(int(stream["info"]['channel_count'][0]),sfreq,"eeg")
          first_samp = stream["time_stamps"][0]
    else:
        raise RuntimeError('Unknown stream format')

plt.show()
