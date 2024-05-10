# ETF_vs_FI_taxes
Script comparing taxation over an investment lifetime between a portfolio composed of ETFs versus a portfolio of mutual funds. Given the different conditions of Spanish taxation and fees between investment vehicles, the question may arise as to which vehicle optimizes the net return on our investments over the long term.

The program contains two main functions: calcular_patrimonio and start.

The calcular_patrimonio function calculates the final net amount of money after fees and taxes. It takes into account the initial capital, monthly contribution, annual return, annual commission, capital gains tax, investment period, and a boolean flag for tax exemption. The function iteratively calculates the wealth for each year, taking into account the annual return, commission, and monthly contributions. If there is no tax exemption, it also calculates and deducts the tax retention. The function finally returns the net wealth. This program does not take into account tax income brackets, instead it assumes a fixed effective rate.

The start function sets the initial parameters for the investment scenarios and calls the calcular_patrimonio function for both the ETF and mutual funds scenarios. It then prints the final net wealth for both scenarios.


This program provides a simple yet powerful tool for investors to understand the impact of different factors on their investment outcomes in the context of Spanish taxation. It can be further extended or modified to accommodate more complex scenarios or different tax regimes.

Disclaimer:
Please note that this is a simplified model and actual investment outcomes can be influenced by many other factors not considered in this program.
