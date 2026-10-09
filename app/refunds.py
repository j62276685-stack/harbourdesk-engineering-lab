def refund_amount(original_minor, requested_minor):
    if isinstance(requested_minor,bool) or not isinstance(requested_minor,int):
        raise ValueError("amount must be an integer in minor units")
    if requested_minor <= 0 or requested_minor > original_minor:
        raise ValueError("amount outside refundable range")
    return requested_minor
