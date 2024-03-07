import os
import csv

budget_file_path = os.path.join('Resources', 'budget_data.csv')
output_file_path = os.path.join('Resources', 'budget_data_with_changes.csv')
output_file_path = os.path.join('Resources', 'financial_analysis.txt')

# Initialize a set to store unique months
unique_months = set()
net_profit_loss = 0
previous_profit = 0
profit_changes = []

rows_with_changes = []

with open(budget_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    rows = list(csvreader)
    header = rows[0]
    header.append('Changes')  # Add 'Changes' to the header

    # Iterate through rows and extract month information
    for row in rows[1:]:
        # Assuming the column index for 'Date' is 0 and 'Profit/Losses' is 1, adjust if needed
        month = row[0]
        unique_months.add(month)
        profit_loss = int(row[1])

        change = profit_loss - previous_profit
        row.append(change)
        profit_changes.append(change)

        previous_profit = profit_loss

        net_profit_loss += profit_loss

        rows_with_changes.append(row)

# Calculate the total number of unique months
total_months = len(unique_months)
average_change = 0
change_column = [int(row[-1]) for row in rows_with_changes[1:]]
average_change = sum(change_column) / len(change_column)
greatest_increase_amount = 0
greatest_decrease_amount =0
for row in rows_with_changes[2:]:  # Exclude the first two rows since 'Changes' starts from the third row
    date = row[0]
    increase_amount = row[-1]

    if increase_amount > greatest_increase_amount:
        greatest_increase_amount = increase_amount
        greatest_increase_date = date
for row in rows_with_changes[2:]:  # Exclude the first two rows since 'Changes' starts from the third row
    date1 = row[0]
    decrease_amount = row[-1]

    if decrease_amount < greatest_decrease_amount:
        greatest_decrease_amount = decrease_amount
        greatest_decrease_date = date1
# Write the rows with changes back to the same CSV file
with open(output_file_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the modified header
    csvwriter.writerow(header)
    
    # Write the rows with changes
    csvwriter.writerows(rows_with_changes)

print("Financial Analysis")
print("-------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_profit_loss}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})')


with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-------------------\n")
    output_file.write(f'Total Months: {total_months}\n')
    output_file.write(f'Total: ${net_profit_loss}\n')
    output_file.write(f'Average Change: ${average_change}\n')
    output_file.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n')
    output_file.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n')
print(f'Results exported to: {output_file_path}')