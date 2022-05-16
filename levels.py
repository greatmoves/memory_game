def generate_level(prev_level):
    
    if(prev_level == 1):
        frequency = 1
        amount = 3
        level = 1
        time_to_press = 3
    else:
        if(prev_level["level"] < 3):
            amount = prev_level["amount"] + 1
            frequency = 1
            time_to_press = 3
        elif(prev_level["level"] < 8):
            amount = 5
            frequency = prev_level["frequency"] - 0.1
            time_to_press = prev_level["time_to_press"] - 0.1
        elif(prev_level["level"] < 10):
            amount = prev_level["amount"] + 1
            frequency = 0.5
            time_to_press = 2.5
        else:
            amount = prev_level["amount"] + 1
            frequency = 0.5
            time_to_press = 2.5
        level = prev_level["level"] + 1
            
    return {
        "frequency": round(frequency, 1),
        "amount": amount,
        "level" : level,
        "time_to_press" : round(time_to_press, 1)
    }
