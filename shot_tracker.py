import numpy as np


class ShotTracker(object):

    def __init__(self):
        pass

    def __prepare_peaks(self, wave):
        wave = np.array(wave[:, 0], dtype='float')
        wave = abs(wave)
        max_value = np.amax(wave) * 0.98
        return np.where(wave >= max_value)[0].tolist()

    def __cluster_peaks(self, source, margin, samp_freq):
        list_iterable = 0
        current_peak = source.pop(0)
        result_list = [current_peak / samp_freq]
        for peak in source:
            if peak >= (current_peak + margin * samp_freq):
                list_iterable = list_iterable + 1
                result_list.append(peak / samp_freq)
            current_peak = peak
        return result_list;

    def get_shot_timings_list(self, soundarray, samp_freq):
        return self.__cluster_peaks(self.__prepare_peaks(soundarray), 0.09, samp_freq)
