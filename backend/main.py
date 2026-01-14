from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from backend.models.user import UserProfile
from backend.risk_engine.risk_calculator import calculate_risk_score, get_risk_type
from backend.allocation_engine.allocator import allocate_assets
from backend.return_engine.return_calculator import calculate_expected_return

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (safe for demo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/recommend")
def recommend_portfolio(user: UserProfile):
    risk_score = calculate_risk_score(user)
    risk_type = get_risk_type(risk_score)

    allocation = allocate_assets(risk_type, user.investment_amount)

    expected_return = calculate_expected_return(
        allocation,
        user.investment_years
    )

    sip_return = calculate_sip_return(
        monthly_investment=user.monthly_income * 0.2,
        years=user.investment_years,
        annual_rate=0.12
    )

    real_return = adjust_for_inflation(
        nominal_return=expected_return,
        inflation_rate=0.06,
        years=user.investment_years
    )

    return {
        "risk_score": risk_score,
        "risk_type": risk_type,
        "allocation": allocation,
        "expected_return": expected_return,
        "sip_return": sip_return,
        "inflation_adjusted_return": real_return
    }
