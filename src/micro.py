import speech_recognition as sr
for i, n in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone with name {n} found for `Microphone(device_index={i})`")
