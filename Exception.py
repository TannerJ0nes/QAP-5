# QAP 5 Program for ONE STOP INSURANCE COMPANY to display monthly policies in report
# Author: Tanner Jones
# Written: March 29th,2023


import datetime

# Setting up beginning of report

today = datetime.date.today()
print()
print("ONE STOP INSURANCE COMPANY")
print(f"POLICY LISTING AS OF {today}")
print()
print("POLICY CUSTOMER              TOTAL                 TOTAL      MONTHLY")
print("NUMBER NAME                 PREMIUM      HST       COST       PAYMENT")
print("======================================================================")

# starting counters

PolicyCrt = 0
HSTacc = 0
Totcostacc = 0
monthlyacc= 0
TotPremiumacc = 0

# opening file in read mode

f = open("Policies.dat", "r")

# Starting main loop to read data from file and assign variables

for PoliciesDataLine in f:

    PoliciesLine = PoliciesDataLine.split(",")


    PolicyNum = PoliciesLine[0].strip()
    FirstName = PoliciesLine[1].strip()
    LastName = PoliciesLine[2]
    number_cars = int(PoliciesLine[8].strip())
    extra_insurance = PoliciesLine[9].strip()
    glass_coverage = PoliciesLine[10].strip()
    loaner_car = PoliciesLine[11].strip()
    pay_method = PoliciesLine[12].strip()
    insurance_premium = float(PoliciesLine[13].strip())

    # Determing which file lines to print to report

    if pay_method == "M":
        if extra_insurance == "Y":
            extra_insurancecost = 130 * number_cars
        else:
            extra_insurancecost = 0
        if glass_coverage == "Y":
            glass_coveragecost = 86 * number_cars
        else:
            glass_coveragecost = 0
        if loaner_car == "Y":
            loaner_carcost = 58 * number_cars
        else:
            loaner_carcost = 0

        # main calculations

        ExtraCost = extra_insurancecost + glass_coveragecost + loaner_carcost
        totalpremium = ExtraCost + insurance_premium
        HST = totalpremium * 0.15
        TotalCost = totalpremium + HST
        MonthlyPayment = (TotalCost + 39.99)/12

        # Formatting and printing report body

        insurance_premiumdsp = "${:,.2f}".format(insurance_premium)
        ExtraCostdsp = "${:,.2f}".format(ExtraCost)
        totalpremiumdsp = "${:,.2f}".format(totalpremium)
        HSTdsp = "${:,.2f}".format(HST)
        TotalCostdsp = "${:,.2f}".format(TotalCost)
        MonthlyPaymentdsp = "${:,.2f}".format(MonthlyPayment)

        print(f'{PolicyNum:<5s} {FirstName + LastName:<20s}  {totalpremiumdsp:<8s}   {HSTdsp:<6s}   {TotalCostdsp:<8s}  {MonthlyPaymentdsp:<8s}')

        # adding to counters

        PolicyCrt += 1
        HSTacc += HST
        Totcostacc += TotalCost
        monthlyacc += MonthlyPayment
        TotPremiumacc += totalpremium
    else:
        pass

# Formatting and printing end of report

HSTaccdsp = "${:,.2f}".format(HSTacc)
Totcostaccdsp = "${:,.2f}".format(Totcostacc)
monthlyaccdsp = "${:,.2f}".format(monthlyacc)
TotPremiumaccdsp = "${:,.2f}".format(TotPremiumacc)

print("======================================================================")
print(f'Total policies: {PolicyCrt:<3d}        {TotPremiumaccdsp:<9s} {HSTaccdsp:<8s}  {TotalCostdsp:<9s}  {monthlyaccdsp:<9s}')
f.close()
