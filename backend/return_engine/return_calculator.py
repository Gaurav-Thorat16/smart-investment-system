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
