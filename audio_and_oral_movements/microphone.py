import speech_recognition as sr
import pyaudio
import wave
import threading
import os
import nltk

nltk.download('stopwords')


def recorder():
    def read_audio(stream, filename):
        chunk = 1024  # Record in chunks of 1024 samples
        sample_format = pyaudio.paInt16  # 16 bits per sample
        channels = 2
        fs = 44100  # Record at 44100 samples per second
        seconds = 10  # Number of seconds to record at once
        filename = filename
        frames = []  # Initialize array to store frames

        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Save the recorded data as a WAV file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()
        # Stop and close the stream
        stream.stop_stream()
        stream.close()

    def convert(i):
        if i >= 0:
            sound = 'record' + str(i) + '.wav'
            r = sr.Recognizer()

            with sr.AudioFile(sound) as source:
                r.adjust_for_ambient_noise(source)
                print("Converting Audio To Text and saving to file..... ")
                audio = r.listen(source)
            try:
                value = r.recognize_google(audio)  ##### API call to google for speech recognition
                os.remove(sound)
                if str is bytes:
                    result = u"{}".format(value).encode("utf-8")
                else:
                    result = "{}".format(value)

                with open("test.txt", "a") as f:
                    f.write(result)
                    f.write(" ")
                    f.close()

            except sr.UnknownValueError:
                print("")
            except sr.RequestError as e:
                print("{0}".format(e))
            except KeyboardInterrupt:
                pass

    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100

    def save_audios(i):
        stream = p.open(format=sample_format, channels=channels, rate=fs,
                        frames_per_buffer=chunk, input=True)
        filename = 'record' + str(i) + '.wav'
        read_audio(stream, filename)

    flag = False
    for i in range(100 // 50):  # Number of total seconds to record/ Number of seconds per recording
        t1 = threading.Thread(target=save_audios, args=[i])
        x = i - 1
        t2 = threading.Thread(target=convert, args=[x])  # send one earlier than being recorded
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        if i == 2:
            flag = True
    if flag:
        convert(i)
        p.terminate()
