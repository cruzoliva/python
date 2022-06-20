def add_time(start_time, duration, day =""):
    #Separo las horas y minutos iniciales
    start_hor_min, am_pm = start_time.split(" ")
    start_hor, start_min = start_hor_min.split(":")

    if am_pm == "PM":
        start_hor = int(start_hor) + 12

    #Serparo las horas y minutos de la duración 
    dur_hor, dur_min = duration.split(":")
    #print(start_hor, start_min, am_pm, dur_hor, dur_min)

    
    minutes = int(start_min) + int(dur_min)
    
    if minutes >= 60:
        minutes = minutes - 60
        dur_hor = int(dur_hor) + 1

    hours = int(start_hor) + int(dur_hor)
    days = 0
    if hours >= 24:
        days = hours // 24
        hours = hours % 24
    
    tot_days = ""
    if days == 1:
        tot_days = "Next day"
    elif days > 1:
        tot_days = str(days) + " Days after"
    
    
    if hours > 12:
        tot_am_pm = "PM"
        hours = hours - 12
    else:
        tot_am_pm = "AM"

    tot_hours = str(hours)
    tot_minutes = str(minutes)
    if len(str(hours)) == 1:
        tot_hours = "0" + str(hours)
    if len(str(minutes)) == 1:
        tot_minutes = "0" + str(minutes)

    if day != "":
        wday = week_day(day, days)
    else:
        wday = ""

    print(f"{tot_hours}:{tot_minutes} {tot_am_pm} {tot_days} {wday}")


def week_day(day, add_days):
    week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    if day.lower() == "monday":
        index = 0
    elif day.lower() == "tuesday":
        index = 1
    elif day.lower() == "wednesday":
        index = 2
    elif day.lower() == "thursday":
        index = 3
    elif day.lower() == "friday":
        index = 4
    elif day.lower() == "saturday":
        index = 5
    elif day.lower() == "sunday":
        index = 6
    else:
        return "Error day"
        
    tot_index = index + add_days
    if tot_index > 6:
        tot_index = tot_index % 6

    return week[tot_index]
    

