from pydub import AudioSegment

wav_file = AudioSegment.from_wav("File.wav")

def speed_change(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)\

user_input = float(input("Введите коэфицинет изменения скорости "))

new_sound = speed_change(wav_file, user_input)

new_sound.export("new.wav", format="wav")