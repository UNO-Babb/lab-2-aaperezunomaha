#FutureTime.py
#Name:Antonio Perez
#Date:JAN 29 2025
#Assignment:LAB 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now. hour - 5) % 24
  currentMinute = now.minute


  
print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
userHours = int(input("hours"))
  #Ask user for minutes
userMinutes = int(input("minutes"))
moreMins = 70



futureMins = (currentMinute + moreMins ) % 60
extraHour = (currentMinute + moreMins ) // 60
print(extraHour)

futureHour = ( currentHour + extraHour ) % 24
  

  #Calculate the time after the user-supplied time has passed.
Minutes = (userMinutes + currentMinute)
Hours = (futureHour + userHours)
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
print(f"Future time: {futureHour:02}:{futureMins:02}")
if __name__ == '__main__':
  main()