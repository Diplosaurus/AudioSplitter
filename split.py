import scipy.io.wavfile as sc
import pydub
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

temp_folder = "/Users/derekphan/Desktop/AudioSplitter/"

input_song = input("Enter Song Name: \n")
song_counter = 0

destination_folder = ""
def read_file(file_name):
    assert ".mp3" in file_name
    global destination_folder


    """TESTS TO SEE OF THE USER INPUT FILE IS IN THE SAME DIRECTORY"""
    try:
        sound = pydub.AudioSegment.from_mp3(temp_folder + file_name)
        print("\nFile found! Please wait. This process can take several minutes.")

        """CREATES A NEW FOLDER TO STORE THE SONG CHUNKS"""
        destination_folder = file_name.replace(".mp3", "").capitalize()
        print(f"Creating new folder [{destination_folder}] to store chunks \n")
        create_folder(destination_folder)
    except FileNotFoundError:
        raise FileNotFoundError("\nFile name not found. Make sure the file is in the AudioSplitter folder")

    #convert to wav
    file_name = file_name.replace(".mp3", ".wav")
    sound.export(temp_folder + file_name, format="wav")

    #read wav file
    rate, audData = sc.read(temp_folder + file_name)
    return  sound, rate, audData

def create_folder(folder_name):
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        else:
            raise OSError("")
    except OSError:
        raise OSError(f"Folder [{folder_name}] already exists. Folder could not be created")


chunk_name = input_song.replace(".mp3", "")
for song in split_on_silence(read_file(input_song)[0], silence_thresh= -52):
    song_counter += 1
    song.export(temp_folder + f"{destination_folder}/{chunk_name}{song_counter}.mp3", format="mp3")
    print(f"Song added. Current number of chunks:{song_counter}")
