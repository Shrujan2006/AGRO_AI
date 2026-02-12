def predict_yield(
    crop_type,
    severity,
    confidence,
    land_size_acres,
    temperature
):

    crop_base_yield = {
        "tomato": 25,
        "potato": 20,
        "grapes": 15,
        "apples": 18,
        "strawberry": 12,
        "corn": 10
    }

    if crop_type not in crop_base_yield:
        return {"error": "Unsupported crop type"}

    base_yield_per_acre = crop_base_yield[crop_type]
    total_possible_yield = base_yield_per_acre * land_size_acres

    # Severity impact
    severity_map = {
        "mild": 10,
        "moderate": 25,
        "severe": 45
    }

    if severity not in severity_map:
        return {"error": "Invalid severity level"}

    severity_factor = severity_map[severity]

    # Temperature impact
    weather_factor = 0
    if temperature > 35 or temperature < 10:
        weather_factor += 10

    final_reduction_percent = (severity_factor + weather_factor) * (confidence / 100)

    yield_loss_tons = total_possible_yield * (final_reduction_percent / 100)
    estimated_yield = total_possible_yield - yield_loss_tons

    price_per_ton = 20000
    economic_loss = yield_loss_tons * price_per_ton

    if final_reduction_percent >= 40:
        risk_level = "High"
    elif final_reduction_percent >= 20:
        risk_level = "Moderate"
    else:
        risk_level = "Low"

    return {
        "total_possible_yield_tons": round(total_possible_yield, 2),
        "final_reduction_percent": round(final_reduction_percent, 2),
        "yield_loss_tons": round(yield_loss_tons, 2),
        "estimated_yield_tons": round(estimated_yield, 2),
        "economic_loss_inr": round(economic_loss, 2),
        "risk_level": risk_level
    }