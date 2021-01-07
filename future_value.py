def future_value(present_value, annual_rate, periods_per_year, years):
    """
When investing money, an important concept to know is compound interest.  

The equation   FV = PV(1 + rate)**periods
  Where:
    The present value (PV) of your money is how much money you have now. 
    The future value (FV) of your money is how much money you will have in the future.
    The nominal interest rate per period (rate) is how much interest you earn during a 
    particular length of time, before accounting for compounding.  This is typically 
    expressed as a percentage.
    The number of periods (periods) is how many periods in the future this calculation is for.
"""
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    return (present_value * (1 + rate_per_period) ** periods)

print ("$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3))


