# QAP 5 Program for ONE STOP INSURANCE COMPANY to show all reports on files and totals
# Author: Tanner Jones
# Written: March 28th,2023


import datetime

# Setting up beginning of report

today = datetime.date.today()
print()
print("ONE STOP INSURANCE COMPANY")
print(f"POLICY LISTING AS OF {today}")
print()
print("POLICY CUSTOMER              INSURANCE    EXTRA      TOTAL")
print("NUMBER NAME                   PREMIUM     COSTS     PREMIUM")
print("============================================================")

# starting counters

PolicyCrt = 0
Insupremiumacc = 0
Extraacc = 0
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

    # Determining what extra costs are

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

    # Main Calculations

    ExtraCost = extra_insurancecost + glass_coveragecost + loaner_carcost
    totalpremium = ExtraCost + insurance_premium

    insurance_premiumdsp = "${:,.2f}".format(insurance_premium)
    ExtraCostdsp = "${:,.2f}".format(ExtraCost)
    totalpremiumdsp = "${:,.2f}".format(totalpremium)

    # Printing body of Report

    print(f' {PolicyNum:<5s} {FirstName + LastName:<20s}  {insurance_premiumdsp:<8s}   {ExtraCostdsp:<8s}  {totalpremiumdsp:<8s}')

    # Adding to counters

    PolicyCrt += 1
    Insupremiumacc += insurance_premium
    Extraacc += ExtraCost
    TotPremiumacc += totalpremium

# Formatting and printing end statements

Insupremiumaccdsp = "${:,.2f}".format(Insupremiumacc)
Extraaccdsp = "${:,.2f}".format(Extraacc)
TotPremiumaccdsp = "${:,.2f}".format(TotPremiumacc)

print("============================================================")
print(f'Total policies: {PolicyCrt:<3d}          {Insupremiumaccdsp:<9s} {Extraaccdsp:<9s} {TotPremiumaccdsp:<9s}')
f.close()
