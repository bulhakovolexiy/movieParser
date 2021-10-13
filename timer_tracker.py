

class TimerTracker(object):
    def __init__(self):
        pass

# def find_main_beep_freq(source):
#     fft_spectrum = np.fft.rfft(source)
#
#     freq = np.fft.rfftfreq(source.size, d=1. / sampFreq)
#
#     freq_coords = [int(x) for x in range(0, len(freq)) if 1500 <= freq[x] <= 3250]
#     fft_spectrum = fft_spectrum[freq_coords]
#
#     fft_spectrum_abs = np.abs(fft_spectrum)
#
#     max_amplitude = max(fft_spectrum_abs)
#     max_amplitude_coord = fft_spectrum_abs.tolist().index(max_amplitude)
#     return freq[freq_coords[max_amplitude_coord]]
#
# def find_highest_peak(source):
#     main_beep_freq = find_main_beep_freq(source)
#     butter_filter = signal.butter(10, [main_beep_freq - 40, main_beep_freq + 40], btype='bandpass', output='sos',
#                                   fs=sampFreq)
#     source = signal.sosfilt(butter_filter, source)
#
#     return max(source)
#
# def find_highest_peak_coord(source, time_window, offset, samp_freq):
#     practical_time_window = int(time_window*samp_freq)
#     practical_offset = int(offset*samp_freq)
#     source_len = len(source)
#     highest_peak = 0
#     highest_peak_coord = 0
#     i = 0
#     while i < source_len:
#         j = i+practical_time_window
#         if j > source_len:
#             break
#
#         peak = find_highest_peak(source[i:j])
#
#         if peak > highest_peak:
#             highest_peak = peak
#             highest_peak_coord = i;
#         i += practical_offset
#     return highest_peak_coord, highest_peak

