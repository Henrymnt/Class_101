import time

seconds=input("Enter the time (in seconds):")

def countdown_timer(seconds):
    while seconds>0:
        minutes=int(seconds/60)
        secs=int(seconds%60)
        timer=f'{minutes}:{secs}'
        print(timer,end='\r')
        time.sleep(1)
        seconds-=1
    print('Times up!')

countdown_timer(int(seconds))
