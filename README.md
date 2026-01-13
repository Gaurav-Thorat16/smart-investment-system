# Smart Investment Recommendation System

## Overview
This project is a backend system that recommends an optimized investment portfolio
based on a user's risk profile, investment amount, and time horizon.

## Features
- Risk profiling using age, income, duration, and risk appetite
- Rule-based asset allocation (Equity, Debt, Gold, Cash)
- Future portfolio value simulation using compound interest
- REST API built with FastAPI
- Interactive API documentation using Swagger UI

## Tech Stack
- Python
- FastAPI
- Pydantic
- Uvicorn

## API Endpoint
POST /recommend

## Sample Input
```json
{
  "age": 23,
  "monthly_income": 40000,
  "investment_amount": 100000,
  "investment_years": 5,
  "risk_appetite": "Medium"
}
