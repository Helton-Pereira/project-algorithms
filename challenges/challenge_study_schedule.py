def study_schedule(permanence_period, target_time):
    result = 0
    if type(target_time) is not int:
        return None
    for i, j in permanence_period:
        if type(i) is not int or type(j) is not int:
            return None
        elif i <= target_time <= j:
            result += 1
    return result
