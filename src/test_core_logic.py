import pandas as pd
from core_logic import generate_forecast, calculate_anomaly_score

def test_forecast_normal():
    df = pd.DataFrame({'quantity': [10, 12, 11, 13, 12, 14, 15]})
    result = generate_forecast(df)
    assert result['forecast_7day'] > 0
    assert result['forecast_30day'] > 0

def test_forecast_short_data():
    df = pd.DataFrame({'quantity': [10, 12]})
    result = generate_forecast(df)
    assert result['forecast_7day'] == 0

def test_anomaly_normal():
    df = pd.DataFrame({'quantity': [10, 12, 11, 13, 12, 14, 30]})
    score = calculate_anomaly_score(df)
    assert 0 <= score <= 1

def test_anomaly_constant():
    df = pd.DataFrame({'quantity': [10, 10, 10, 10, 10]})
    score = calculate_anomaly_score(df)
    assert score == 0.0