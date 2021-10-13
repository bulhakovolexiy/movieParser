# Import everything needed to edit video clips
from moviepy.editor import *
from shot_tracker import *

def shot_text_data(shot_timings):
    result_list = []
    prev_shot = shot_timings[0]
    for shot_timing_val in shot_timings:
        result_list.append([shot_timing_val, shot_timing_val - prev_shot])
        prev_shot = shot_timing_val

    shot_timings.pop(0)
    result_list[len(shot_timings)].append(0)

    for i in range(0, len(shot_timings)):
        result_list[i].append(shot_timings[i])

    return result_list

input_clip = VideoFileClip("D:\movie\stage2.mp4")

shot_timings = ShotTracker().get_shot_timings_list(input_clip.audio.to_soundarray(), input_clip.audio.fps)

txt_clips = [input_clip]

for shot_timing in shot_text_data(shot_timings):
    txt_clip = TextClip("{:.2f}   {:.2f}".format(shot_timing[0], shot_timing[1]), fontsize=70, color='white')
    txt_clip = txt_clip.set_pos(('right', 'top')).set_start(shot_timing[0])
    if shot_timing[2]==0 :
        txt_clip = txt_clip.set_duration(10)
    else:
        txt_clip = txt_clip.set_end(shot_timing[2])
    txt_clips.append(txt_clip)

output_clip = CompositeVideoClip(txt_clips)

output_clip.write_videofile("myHolidays_edited.mp4")