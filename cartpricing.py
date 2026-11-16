"""
Corrected CodeTrace test fixture.

The discount is applied before tax is calculated.
"""

def calculate_cart_total(subtotal: float, discount_percent: float, tax_rate: float) -> float:
    """Return the final cart total after discount and tax."""
    if subtotal < 0:
        raise ValueError("subtotal cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    if not 0 <= tax_rate <= 1:
        raise ValueError("tax_rate must be between 0 and 1")

    discount = subtotal * (discount_percent / 100)
    discounted_subtotal = subtotal - discount
    tax = discounted_subtotal * tax_rate

    total = discounted_subtotal + tax
    return round(total, 2)


if __name__ == "__main__":
    # Expected result: 99.00
    print(calculate_cart_total(100.00, 10, 0.10))
