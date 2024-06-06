def solution(date1, date2):
    year1, month1, day1 = date1
    year2, month2, day2 = date2
    if year1 < year2:
        return 1
    elif year1 > year2:
        return 0
    else:
        if month1 < month2:
            return 1
        elif month1 > month2:
            return 0
        else:
            if day1 < day2:
                return 1
            elif day1 > day2:
                return 0
            else:
                return 0
    if date1[0] == date2[0]:
        if date1[1] == date2[1]:
            if date1[2] == date2[2]:
                return 0
            elif date1[2] < date2[2]:
                return 1
            else:
                return 0
        elif date1[1] < date2[1]:
            return 1
        else:
            return 0
    elif date1[0] < date2[0]:
        return 1
    
    
    if date1[0] != date2[0]:
        if date1[0] < date2[0]:
            return 1
        else:
            return 0
    else:
        if date1[1] != date2[1]:
            if date1[1] < date2[1]:
                return 1
            else:
                return 0
        else:
            if date1[2] != date2[2]:
                if date1[2] < date2[2]:
                    return 1
                else:
                    return 0
            else:
                return 0
    if year1 != year2:
        if year1 < year2:
            return 1
        else:
            return 0
    elif month1 != month2:
        if month1 < month2:
            return 1
        else:
            return 0
    else:
        return 0