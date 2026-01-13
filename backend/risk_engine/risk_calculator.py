def calculate_risk_score(user):
    score = 0

    # Age factor
    if user.age < 30:
        score += 25
    elif user.age < 45:
        score += 15
    else:
        score += 5

    # Income factor
    if user.monthly_income > 50000:
        score += 20
    else:
        score += 10

    # Investment duration factor
    if user.investment_years >= 5:
        score += 30
    else:
        score += 15

    # Risk appetite factor
    if user.risk_appetite.lower() == "high":
        score += 25
    elif user.risk_appetite.lower() == "medium":
        score += 15
    else:
        score += 5

    return score


def get_risk_type(score):
    if score <= 35:
        return "Low"
    elif score <= 65:
        return "Medium"
    else:
        return "High"
