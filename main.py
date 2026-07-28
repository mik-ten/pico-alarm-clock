# 'time' is a library with functions for time | 'ticks_ms' = increasing number in ms | 'ticks_diff' = calculates the difference between two such numbers
# 'machine' is a MicroPython library dedicated to controlling hardware on the Pico, 'Pin' is used to control or  read a physical GPIO-pin


from time import ticks_ms, ticks_diff
from machine import Pin, PWM
from I2C_LCD import I2CLcd
from machine import Pin, PWM, I2C

# time variables


hour = int(input("Hour: "))
minute = int(input("Minute: "))
second = int(input("Second: "))

# display



i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=100000)

lcd = I2CLcd(i2c, 0x27, 2, 16)


print(i2c.scan())


# alarm variables

buzzer = PWM(Pin(15))
buzzer.freq(2000)
buzzer.duty_u16(0)

alarm_hour = int(input("Alarm hour: "))
alarm_minute = int(input("Alarm minute: "))

# Save the millisecond value when the clock starts

last_second = ticks_ms()

# loops

while True:
    
    now = ticks_ms()
    if ticks_diff(now, last_second) >= 1000:
        last_second += 1000
        second += 1
        
        if second == 60:
            second = 0
            minute += 1
            
        if minute == 60:
            minute = 0
            hour += 1
        
        if hour == 24:
            hour = 0
        
        if hour == alarm_hour and minute == alarm_minute and second < 10:
            print("ALARM!")
            buzzer.duty_u16(32768)
        else:
            buzzer.duty_u16(0)
            
        print(f"\r{hour:02d}:{minute:02d}:{second:02d}", end="")
        
        lcd.move_to(0, 0)
        lcd.putstr(f"{hour:02d}:{minute:02d}:{second:02d}")
            




