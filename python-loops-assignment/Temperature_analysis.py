# Name: [Your Name]
# Roll Number: [Your Roll Number]
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
# Write your code here
if not temperatures:
    print("List is empty")
else:
    max_temp = temperatures[0]
    min_temp = temperatures[0]

    for temp in temperatures:
        if temp > max_temp:
            max_temp = temp
        if temp < min_temp:
            min_temp = temp

    print(f"Highest Temperature: {max_temp}°C")
    print(f"Lowest Temperature: {min_temp}°C")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
# Write your code here
hot_days = 0
for temp in temperatures:
    if temp <= 30:
        continue
    hot_days += 1

print(f"Hot Days (>30°C): {hot_days}")


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
# Write your code here
hot_days_alert = 0
day_counter = 0

for temp in temperatures:
    day_counter += 1
    if temp >= 40:
        # According to requirements, stop immediately.
        # But we must output 'Hot Days before alert' BEFORE 'Alert!' to match expected output.
        print(f"Hot Days before alert: {hot_days_alert}")  
        print(f"Alert! Extreme temperature {temp}°C detected on Day {day_counter}")
        break
    if temp > 30:
        hot_days_alert += 1
else:
    # If loop completes without break
    print(f"Hot Days before alert: {hot_days_alert}")
