def allocate_assets(risk_type, investment_amount):
    if risk_type == "Low":
        equity_pct = 0.20
        debt_pct = 0.50
        gold_pct = 0.20
        cash_pct = 0.10
    elif risk_type == "Medium":
        equity_pct = 0.40
        debt_pct = 0.35
        gold_pct = 0.15
        cash_pct = 0.10
    else:  # High Risk
        equity_pct = 0.65
        debt_pct = 0.20
        gold_pct = 0.10
        cash_pct = 0.05

    return {
        "equity": investment_amount * equity_pct,
        "debt": investment_amount * debt_pct,
        "gold": investment_amount * gold_pct,
        "cash": investment_amount * cash_pct
    }
