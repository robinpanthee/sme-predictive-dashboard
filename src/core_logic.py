def generate_forecast(df, quantity_col='quantity'):
    quantities = df[quantity_col].dropna().tolist()
    if len(quantities) < 3:
        return {'forecast_7day': 0, 'forecast_30day': 0}
    avg = sum(quantities[-7:]) / min(7, len(quantities))
    return {
        'forecast_7day': round(avg * 7, 1),
        'forecast_30day': round(avg * 30, 1)
    }

def calculate_anomaly_score(df, quantity_col='quantity'):
    quantities = df[quantity_col].dropna().tolist()
    if len(quantities) < 5:
        return 0.0
    mean = sum(quantities) / len(quantities)
    variance = sum((x - mean)**2 for x in quantities) / len(quantities)
    std = variance ** 0.5
    if std == 0:
        return 0.0
    latest = quantities[-1]
    z_score = abs(latest - mean) / std
    score = min(z_score / 3.0, 1.0)
    return round(score, 2)