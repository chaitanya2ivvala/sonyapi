import multiprocessing
import time
import os
from pynput.keyboard import Key, Controller
from mutagen.mp3 import MP3
audio = MP3("dhruva.mp3")
mp3len = audio.info.length
#print mp3len
keyboard = Controller()


# Your foo function
def foo(n):
    os.system('dlnast -l dhruva.mp3')
    #for i in range(10000 * n):
     #   print "Tick"
      #  time.sleep(1)

if __name__ == '__main__':
    # Start foo as a process
    p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
    p.start()
    time.sleep(4)
    audio = MP3("dhruva.mp3")
    mp3len = audio.info.length

    # Wait 10 seconds for foo
    time.sleep(mp3len)
    #print ("q")
    keyboard.press('q')
    time.sleep(4)

    # Terminate foo
    p.terminate()

    # Cleanup
    p.join()
