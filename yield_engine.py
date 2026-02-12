# yield_engine.py

# Base yield in tons per acre
BASE_YIELD = {
    "tomato": 25,
    "potato": 20,
    "grapes": 10,
    "apples": 12,
    "strawberry": 15,
    "corn": 4
}

# Market price per ton (INR)
MARKET_PRICE = {
    "tomato": 8000,
    "potato": 15000,
    "grapes": 30000,
    "apples": 40000,
    "strawberry": 50000,
    "corn": 18000
}

# Severity reduction %
SEVERITY_IMPACT = {
    "mild": 8,
    "moderate": 20,
    "severe": 40
}

# Ideal weather ranges per crop
IDEAL_CONDITIONS = {
    "tomato": {"temp": (20, 30), "rain": (400, 800)},
    "potato": {"temp": (15, 25), "rain": (500, 1000)},
    "grapes": {"temp": (18, 35), "rain": (500, 900)},
    "apples": {"temp": (10, 24), "rain": (800, 1200)},
    "strawberry": {"temp": (15, 26), "rain": (600, 1000)},
    "corn": {"temp": (18, 32), "rain": (500, 900)}
}


def calculate_weather_penalty(crop_type, temperature, rainfall):
    ideal = IDEAL_CONDITIONS[crop_type]
    temp_min, temp_max = ideal["temp"]
    rain_min, rain_max = ideal["rain"]

    penalty = 0

    if temperature < temp_min or temperature > temp_max:
        penalty += 5

    if rainfall < rain_min or rainfall > rain_max:
        penalty += 5

    return penalty


def predict_yield(
    crop_type,
    severity,
    confidence,
    land_size_acres,
    temperature,
    rainfall
):
    try:
        crop_type = crop_type.lower()
        severity = severity.lower()

        if crop_type not in BASE_YIELD:
            return {"error": "Unsupported crop type"}

        if severity not in SEVERITY_IMPACT:
            return {"error": "Invalid severity level"}

        # Step 1: Base total yield
        base_yield_per_acre = BASE_YIELD[crop_type]
        total_possible_yield = base_yield_per_acre * land_size_acres

        # Step 2: Severity reduction
        severity_reduction = SEVERITY_IMPACT[severity]

        # Step 3: Confidence adjustment
        adjusted_reduction = severity_reduction * (confidence / 100)

        # Step 4: Weather penalty
        weather_penalty = calculate_weather_penalty(
            crop_type,
            temperature,
            rainfall
        )

        final_reduction_percent = adjusted_reduction + weather_penalty

        # Cap reduction to avoid unrealistic outputs
        final_reduction_percent = min(final_reduction_percent, 80)

        # Step 5: Yield calculations
        yield_loss = total_possible_yield * (final_reduction_percent / 100)
        estimated_yield = total_possible_yield - yield_loss

        # Step 6: Economic loss
        price_per_ton = MARKET_PRICE[crop_type]
        economic_loss = yield_loss * price_per_ton

        # Risk level
        if final_reduction_percent > 35:
            risk_level = "High"
        elif final_reduction_percent > 15:
            risk_level = "Medium"
        else:
            risk_level = "Low"

        return {
            "total_possible_yield_tons": round(total_possible_yield, 2),
            "final_reduction_percent": round(final_reduction_percent, 2),
            "yield_loss_tons": round(yield_loss, 2),
            "estimated_yield_tons": round(estimated_yield, 2),
            "economic_loss_inr": round(economic_loss, 2),
            "risk_level": risk_level
        }

    except Exception as e:
        return {"error": str(e)}