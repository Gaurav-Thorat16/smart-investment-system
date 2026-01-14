def calculate_expected_return(allocation, years):
    # Average annual returns (assumptions)
    returns = {
        "equity": 0.12,   # 12%
        "debt": 0.06,     # 6%
        "gold": 0.07,     # 7%
        "cash": 0.03      # 3%
    }

    total_future_value = 0

    for asset, amount in allocation.items():
        rate = returns.get(asset, 0)
        future_value = amount * ((1 + rate) ** years)
        total_future_value += future_value

    return round(total_future_value, 2)

def calculate_sip_return(monthly_investment, years, annual_rate):
    months = years * 12
    monthly_rate = annual_rate / 12
    total_value = 0

    for i in range(1, months + 1):
        total_value += monthly_investment * ((1 + monthly_rate) ** (months - i))

    return round(total_value, 2)
    
    def adjust_for_inflation(nominal_return, inflation_rate, years):
    real_value = nominal_return / ((1 + inflation_rate) ** years)
    return round(real_value, 2)

