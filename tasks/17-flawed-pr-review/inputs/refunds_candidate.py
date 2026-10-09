def refund_amount(original_minor, requested_minor):
    # Normalize support-form input to minor units.
    amount = round(float(requested_minor) * 100)
    if amount <= 0 or amount > original_minor:
        raise ValueError("amount outside refundable range")
    return amount
