from dateutil import parser
class Workout():
    cal_per_hr = 200
    def __init__(self, start, end , calories = None):
        self.start= parser.parse(start)
        self.end = parser.parse(end)
        self.calories = calories
        self.icon = 'Sweat'
        self.kind = 'Workout'
        
    def get_calories(self):
        if (calories == None):
            return Workout.cal_per_hr * (self.end-self.start).total_seconds()/3600
        else:
            self.calories
    def get_duration(self):
        return self.end-self.start
    
    def get_end(self):
        return self.end
    
    def get_calories(self):
        self.calories = calories
    
    def get_start(self, start):
        self.start = parser.parse(start)
    
    def Get_end(self, end):
        self.end = parser.parse(end)
        
    def get_kind(self):
        return self.kind
    
    def __eq__(self, other):
        return type(self) == type(other) and \
               self.start == other.start and \
               self.end == other.end and \
               self.kind == other.kind and \
               self.get_calories() == other.get_calories()
    
    def __str__(self):
        width = 16
        retstr = f"|{'-'*width}|\n"
        retstr += f"|{' '*width}|\n"
        iconLen = 0
        retstr += f"|{self.icon}{' '*(width-3)}\n"
        retstr += f"| {self.kind}{' '*(width-len(self.kind)-1)}|\n"
        retstr += f"|{' ' *width}|\n"
        duration_str = str(self.get_duration())
        retstr += f"| {duration_str}{' '*(width-len(duration_str)-1)}|\n"
        cal_str = f"|{self.get_calories():.0f}"
        retstr += f"| {cal_str} Calories {' '*(width-len(cal_str)-11)}|\n"
        retstr += f"|{' ' *width}|\n"
        retstr += f"|{'_' *width}|\n"
        
        return retstr
class SimpleWorkout(object):
    def __init__(self, start, end, calories):
        self.start = start
        self.end = end
        self.calories = calories
        self.icon = 'Phew'
        self.kind = 'Workout'
        
    def get_calories(self):
        return self.calories
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def set_calories(self, calories):
        self.calories = calories
    def set_start(self, start):
        self.start = start
    def set_end(self, end):
        self.end = end
        
class RunWorkout(Workout):
    cals_per_km = 100
    def __init__(self, start, end, elev=0, calories=None, route_gps_points=None):
        super().__init__(start,end,calories)				# super returns the properties of Workout
        self.icon='Run'
        self.kind='Running'
        self.elev=elev
        self.route_gps_points = route_gps_points
        
    def get_elev(self):
        return self.elev
    def set_elev(self,e ):
        self.elev =e
        
class SwimWorkout(Workout):
    cal_per_hr = 400
    def __init(self, start, end, pace, calories = None, width = None):
        super().__init__(start,end,calories)
        self.icon = 'Swim'
        self.kind = 'Swimming'
        self.pace = pace
    def get_pace(self):
        return self.pace
    def get_calories(self):
        if (self.calories == None):
            return Swimworkout.cal_per_hr * (self.end -self.start)*cal_per_hr
        else:
            return self.calories
        
w= Workout ('1/1/2025 12:00 pm', '1/1/2025 3:00 pm', 200)
print(w)
