def predict_job_role(score):
    if score <= 3:
        return "Intern / Beginner"
    elif score <= 6:
        return "Junior Developer"
    elif score <= 8:
        return "AI Engineer"
    else:
        return "Senior AI Engineer"