import webbrowser
import time

totalBreaks  = 3
breakCount = 0
while breakCount < totalBreaks:   
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=x-Yi762sQTo&ab_channel=IvanVasconcelos")
    breakCount += 1
