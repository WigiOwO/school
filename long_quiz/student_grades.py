def calculate_grade(scores:list):
    info = {}
    info['average'] = sum(scores) / len(scores)
    if info['average'] >= 90:
        verdict = "A"
    elif info['average'] >= 80:
        verdict = "B"
    elif info['average'] >= 70:
        verdict = "C"
    elif info['average'] >= 60:
        verdict = "D"
    else:
        verdict = "F"
    info['grade'] = verdict
    return info
