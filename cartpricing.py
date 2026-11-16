
"""
Intentional CodeTrace test fixture.

BUG: Tax is calculated on the original subtotal before the discount is applied.
Expected behavior: apply the discount first, then calculate tax on the discounted amount.
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

    # INTENTIONAL BUG: tax should use the discounted subtotal.
    tax = subtotal * tax_rate

    total = subtotal - discount + tax
    return round(total, 2)


if __name__ == "__main__":
    # Expected: 99.00; actual buggy result: 100.00
    print(calculate_cart_total(100.00, 10, 0.10))






