employer_number = int(input())
worked_hours = int(input())
amount_received_per_hour = float(input())
salary_total = worked_hours * amount_received_per_hour
print("NUMBER =", employer_number)
print("SALARY = U$ %.2f" % salary_total)