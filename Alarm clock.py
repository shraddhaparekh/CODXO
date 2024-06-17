import datetime
import os
import time

def set_alarm(alarm_time,sound_file):
  alarm_hour = int(alarm_time.split(":")[0])
  alarm_minute = int(alarm_time.split(":")[1])
  alarm_period = alarm_time.split(":")[2].upper()
  print("Alarm is set for {}:{}:{}".format(alarm_hour,alarm_minute,alarm_period))

  while True:
    now = datetime.datetime.now()
    if(now.hour == alarm_hour and 
       now.minute == alarm_minute and   
       now.strftime("%p") == alarm_period):
       print("wake up!")
       os.system("start"+ sound_file)
       break
     time.sleep(1)
  
def main():
    alarm_time = input("Enter the time for alarm(HH:MM:AM/PM): ")
    sound_file = "alarm_sound.mp3" #replace with your own sound file
    set_alarm(alarm_time,sound_file)
if __name__ == "__main__":
  main()
