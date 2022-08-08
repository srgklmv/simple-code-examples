def format_hours(hours, period):

    if hours == 12:
        formatted_hours = 0
    else:
        formatted_hours = hours

    if period == "PM":
        formatted_hours += 12

    return formatted_hours


def reverse_format(hours, minutes):
    
    period = "AM"
    
    if hours >= 12:
        period = "PM"
        hours -= 12
    
    if hours == 0:
        formatted_hours = 12
    else:
        formatted_hours = hours

    if minutes < 10:
        minutes = "0" + str(minutes)
    
    formatted_time = f"{formatted_hours}:{minutes} {period}"

    return formatted_time


def add_time(start, duration, start_day=False):

    days = (
        "Monday", "Tuesday", "Wednesday", "Thursday", 
        "Friday", "Saturday", "Sunday"
    )
    days_counter = 0
    end_time = []

    start_hours = format_hours(int(start.split()[0].split(":")[0]), start.split()[1]) # 24-hours format starts here
    start_minutes = int(start.split()[0].split(":")[1])
    start_period = start.split()[1]
    duration_hours = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])    
    
    end_minutes = start_minutes + duration_minutes
    while end_minutes >= 60:
        end_minutes -= 60
        duration_hours += 1

    end_hours = start_hours + duration_hours
    while end_hours >= 24:
        end_hours -= 24
        days_counter += 1

    end_time.append(reverse_format(end_hours, end_minutes)) # 24-hours format ends here

    if days_counter == 1:
        end_time.append("(next day)")
    elif days_counter > 1:
        end_time.append(f"({days_counter} days later)")

    if start_day:
        day_index = days.index(start_day.capitalize()) + days_counter
        while day_index >= 7:
            day_index -= 7
        end_time[0] += f", {days[day_index]}"

    new_time = " ".join(end_time)
    
    return new_time
    