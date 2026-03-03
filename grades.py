def compute_average(scores):
    return sum(scores) / len(scores)


def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def generate_remark(grade):
    remarks = {
        "A": "Excellent Performance",
        "B": "Good Performance",
        "C": "Satisfactory Performance",
        "D": "Needs Improvement",
        "F": "Failing Status"
    }
    return remarks.get(grade, "Invalid Grade")