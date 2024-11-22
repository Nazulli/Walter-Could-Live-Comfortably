MoneyLeft = 11000000
SpentPerMonth = 10000
MoneyPaidOverall = 0
MonthsPaidOverall = 0
CurrentMonthOfYear = 0
CurrentYear = 0


hasEnoughMoney = True

while hasEnoughMoney == True:
    
    print(f"It is year {CurrentYear}.")
    print(f"{MonthsPaidOverall} months have passed since you began living out here, Walter.")
    print(f"So far, you have spent ${MoneyPaidOverall} during your isolation.\n\n")
    if MoneyLeft >= 10000:
        CurrentMonthOfYear = CurrentMonthOfYear + 1
        MonthsPaidOverall += 1
        MoneyLeft -= SpentPerMonth
        MoneyPaidOverall = MonthsPaidOverall * SpentPerMonth
            
        if CurrentMonthOfYear == 12:
            CurrentMonthOfYear = 0
            CurrentYear += 1
   
            
            
    else:
        hasEnoughMoney = False
        print(f"It's the end of the line. It is year {CurrentYear}. Goodbye Walter.")


# After Walter talks to Ed to become a new man with a new identity, he reveals during an episode each resupply costs 10,000 dollars per run.
# I wondered, how long could Walter live while relying on these resupplies?
# The answer might be higher than you think. I guess we all need at least 11,000,000 dollars lying around.
