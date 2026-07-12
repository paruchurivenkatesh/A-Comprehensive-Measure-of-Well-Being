def format_currency(value):
    """Format a number as currency."""
    return f"${value:,.2f}"

def format_percentage(value):
    """Format a float as percentage."""
    return f"{value * 100:.1f}%"
