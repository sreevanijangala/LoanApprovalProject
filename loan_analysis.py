import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('loan_project.db')

# Load data into pandas DataFrames
customers_df = pd.read_sql_query("SELECT * FROM Customers", conn)
loans_df = pd.read_sql_query("SELECT * FROM LoanApplications", conn)

# Merge data
merged_df = pd.merge(loans_df, customers_df, on='customer_id')

# Basic analysis
print("All Loan Applications:\n", merged_df)
print("\nApproved Loans:\n", merged_df[merged_df['application_status'] == 'Approved'])
print("\nRejected Loans:\n", merged_df[merged_df['application_status'] == 'Rejected'])

# Save merged data to CSV (optional)
merged_df.to_csv("loan_report.csv", index=False)

# Close connection
conn.close()
