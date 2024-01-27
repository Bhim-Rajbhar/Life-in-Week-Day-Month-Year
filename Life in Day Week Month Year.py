
############# Calculating Life in Day,Week,Month,Year ################

print("Calculating Life in Day,Week,Month,Year\n")

Current_Age = int(input("Enter your current AGE : "))

Years_Remaining = 90 - Current_Age

# 12 months is there in one year.
Months_Remaining = Years_Remaining * 12  

# 52 weeks is there in one year.
Weeks_Remaining = Years_Remaining * 52  

# 365 days is there in one year.
Days_Remaining = Years_Remaining * 365  

# Using F-String 
print(f"You have total year remaining is {Years_Remaining}, total month remaining is {Months_Remaining}, total week remaining is {Weeks_Remaining}, and total days remaining is {Days_Remaining}.")