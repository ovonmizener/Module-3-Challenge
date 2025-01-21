# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
net_changes = [] 
greatest_increase = {"date": "", "amount": float("-inf")} 
greatest_decrease = {"date": "", "amount": float("inf")}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    # Track the total and net change
    first_row = next(reader)
    total_months += 1
    total_net += float(first_row[1])
    previous_profit = float(first_row[1])


    # Process each row of data
    for row in reader:
        month = row[0] 
        profit = float(row[1])

        # Track the total
        total_months += 1 
        total_net += profit


        # Track the net change
        net_change = profit - previous_profit 
        net_changes.append(net_change) 
        net_change_sum = sum(net_changes)


        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase["amount"]: 
            greatest_increase["date"] = month 
            greatest_increase["amount"] = net_change 
        if net_change < greatest_decrease["amount"]: 
            greatest_decrease["date"] = month 
            greatest_decrease["amount"] = net_change 
            
        previous_profit = profit


        # Calculate the greatest decrease in losses (month and amount)
        average_change = sum(net_changes) / len(net_changes)
        


# Calculate the average net change across the months
average_change = net_change_sum / total_months


# Generate the output summary
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net:,.2f}
Average Change: ${average_change:,.2f}
Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]:.2f})
Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]:.2f})
"""

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
