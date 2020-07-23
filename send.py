from time import sleep
from twilio.rest import Client
from num import num
import playsound
import threading
import aifc

# Get words from lyrics text
#twilio api key and token
client = Client("ACCOUNT SID", "AUTH TOKEN")

# Song filename
file2 = "ShrekSongFull.aiff"


def get_lyrics():
    with open('lyrics.txt') as file:
        list = [line.strip() for line in file]
        string = " ".join(list)
        return string

# Turn text into list of words
def get_words(lyrics_str):
    return lyrics_str.split()


# Loop through words
# open song file
song2 = aifc.open(file2)
markers = song2.getmarkers()
markers.sort()


def send_messages(phone_number, messages):
    words_list2 = get_words( get_lyrics())
    # gather times for markers
    pre_times = []
    for i in markers:
        element = i[1]
        word = i[2]
        # do stuff with element
        pre_times.append((float(element) / 44100.0) - sum(pre_times))
        x = str(sum(pre_times))


    # Adjust times for markers
    times = []
    dif = []
    accumulation = 0.0
    for index in range(len(pre_times)):

        # Adjust time difference
        difference = pre_times[index]
        difference -= 0.044
        difference -= (0.018 * len(words_list2[index]))
        difference += accumulation
        if difference < 0.0:
            accumulation = difference
            times.append(0.0)
        else:
            times.append(difference)
            accumulation = 0.0
        print(accumulation)
        dif.append(difference)


    print(markers)
    #print(element)
   # print(times)
    # play music on another threade


    def playmusic():
        playsound.playsound(file2)

    #loop and print the lryics on beat has some lag because of th api
    threading.Thread(target=playmusic).start()
    for index in range(len(times)):
        sleep((times[index] + pre_times[index]) - dif[index] - 0.01)
        print(words_list2[index])
        print(times[index])
        send_message(phone_number, words_list2[index])

# Function to Send message
# Open iMessage Client (or use SMS API)


def send_message(phone_number, message):
    client.messages.create(to=phone_number, 
                       from_="+12544002851", 
                       body=message)


def get_lyrics_and_send_messages(phone_number, lyrics):
    words_list = get_words(lyrics)
    send_messages(phone_number, words_list)


get_lyrics_and_send_messages(num, get_lyrics())
