def invoice_total(subtotal_minor, customer_tier="standard", coupon=None, delivery="pickup"):
    amount = subtotal_minor
    if customer_tier == "member":
        amount = amount - amount * 5 // 100
    if coupon == "WELCOME":
        if amount > 10000:
            amount = amount - 1000
        else:
            amount = amount - 500
    if delivery == "courier":
        if amount < 15000:
            amount = amount + 1500
    if amount < 0:
        amount = 0
    if amount >= 0:
        amount = amount + (amount * 75 + 500) // 1000
    return amount
