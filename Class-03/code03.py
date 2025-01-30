class Time:
    #constructor method
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    #getter and second for hour
    @property
    def hour(self):
        return self._hour   
    @hour.setter
    def hour(self, value):
        if not(0 <= value < 24):
            raise ValueError("Hour must be 0 - 23")
        self._hour = value
    
    #getter and setter for minute
    @property
    def minute(self):
        return self._minute 
    @minute.setter
    def minute(self, value):
        if not(0 <= value < 60):
            raise ValueError("Minute must be 0-59")
        self._minute = value
    
    #getter and setter for second
    @property
    def second(self):
        return self._second  
    @second.setter
    def second(self, value):
        if not(0 <= value <60):
            raise ValueError("Second must be 0-59")
        self._second = value
    
    #custom value updater method
    def setTime(self, h = 0, m = 0, s = 0):
        self.hour = h
        self.minute = m
        self.second = s
    
    def __str__(self):
        return (f"{self.hour%12 if self.hour > 0 else 12}:{self.minute}:{self.second} {'AM' if self.hour<12 else 'PM'}")

t = Time(14, 15, 30)

print(f"t.hour: {t.hour}")
print(f"t.minute: {t.minute}")
print(f"t.second: {t.second}")

print(t)

t.setTime(21, 13, 56) 
print(t)


