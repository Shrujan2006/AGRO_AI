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

# Ideal temperature ranges per crop
IDEAL_TEMPERATURE = {
    "tomato": (20, 30),
    "potato": (15, 25),
    "grapes": (18, 35),
    "apples": (10, 24),
    "strawberry": (15, 26),
    "corn": (18, 32)
}


def temperature_penalty(crop_type, temperature):
    temp_min, temp_max = IDEAL_TEMPERATURE[crop_type]
    if temperature < temp_min or temperature > temp_max:
        return 5  # +5% penalty
    return 0


def predict_yield(
    crop_type,
    severity,
    confidence,
    land_size_acres,
    temperature,
    affected_percentage
):
    try:
        crop_type = crop_type.lower()
        severity = severity.lower()

        if crop_type not in BASE_YIELD:
            return {"error": "Unsupported crop type"}

        if severity not in SEVERITY_IMPACT:
            return {"error": "Invalid severity level"}

        if affected_percentage < 0 or affected_percentage > 100:
            return {"error": "Affected percentage must be between 0 and 100"}

        # Step 1: Base total yield
        base_yield_per_acre = BASE_YIELD[crop_type]
        total_possible_yield = base_yield_per_acre * land_size_acres

        # Step 2: Split land
        affected_land = land_size_acres * (affected_percentage / 100)
        healthy_land = land_size_acres - affected_land

        affected_yield = affected_land * base_yield_per_acre
        healthy_yield = healthy_land * base_yield_per_acre

        # Step 3: Severity reduction
        severity_reduction = SEVERITY_IMPACT[severity]

        # Step 4: Confidence adjustment
        adjusted_reduction = severity_reduction * (confidence / 100)

        # Step 5: Temperature penalty
        temp_penalty = temperature_penalty(crop_type, temperature)

        final_reduction_percent = adjusted_reduction + temp_penalty
        final_reduction_percent = min(final_reduction_percent, 80)

        # Step 6: Loss only on affected land
        yield_loss = affected_yield * (final_reduction_percent / 100)

        # Step 7: Final yield
        estimated_yield = healthy_yield + (affected_yield - yield_loss)

        # Step 8: Economic loss
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
            "affected_land_acres": round(affected_land, 2),
            "final_reduction_percent": round(final_reduction_percent, 2),
            "yield_loss_tons": round(yield_loss, 2),
            "estimated_yield_tons": round(estimated_yield, 2),
            "economic_loss_inr": round(economic_loss, 2),
            "risk_level": risk_level
        }

    except Exception as e:
        return {"error": str(e)}
