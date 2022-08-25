class AlarmClock:
    def __init__(self, current_time, alarm1):
        self.current_time = current_time
        self.alarm1 = alarm1
        self.alarm_state = True
    

    def setting_current_time(self):
        self.current_time = input(f'Previous time: {self.current_time}. Enter present time: ')
        print(self.current_time)
    
    def setting_current_time2(self, time_now):
        self.current_time = time_now
        print(self.current_time)

    def set_up_alarm(self):
        self.alarm1 = input(f'Previous alarm {self.alarm1}. Set an alarm: ')
        print(f'{self.alarm1}') 

    def toggle(self):
        if self.alarm_state == True:
            self.alarm_state = False
            print('the alarm is on')
        else:
            self.alarm_state = True
            print('alarm is off')