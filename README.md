# LoanApprovalProject

# 🏦 Loan Approval Analysis & Dashboard

This project analyzes customer and loan data for a fictional bank to understand trends in loan approvals and rejections. It combines **SQLite**, **Python (Pandas)**, and optionally **Power BI** for visual insights.

---

## 📌 Project Overview

- Built a mini loan management database using **SQLite**
- Inserted sample customer and loan records
- Performed data analysis using **Python & Pandas**
- (Optional) Built Power BI dashboard to visualize key insights

---

## 🛠️ Tools & Technologies Used

| Tool       | Purpose                  |
|------------|---------------------------|
| Python     | Data analysis & scripting |
| SQLite     | Backend database (loan data) |
| Pandas     | Data manipulation          |
| Power BI   | Data visualization (optional) |
| Git & GitHub | Version control, hosting  |

---

## 🗂️ Folder Structure

LoanApprovalProject/
├── loan_project.db # SQLite database
├── loan_analysis.py # Python script for analysis
├── loan_report.csv # (Generated) CSV file with merged data
├── README.md # This file


---

## 📊 Sample Data

### 👥 Customers Table

| customer_id | name   | age | gender | income | credit_score |
|-------------|--------|-----|--------|--------|---------------|
| 1           | Amit   | 30  | Male   | 45000  | 720           |
| ...         | ...    | ... | ...    | ...    | ...           |

### 📝 LoanApplications Table

| loan_id | customer_id | loan_amount | purpose     | status    | date       |
|---------|--------------|--------------|-------------|-----------|------------|
| 101     | 1            | 200000       | Home Loan   | Approved  | 2024-05-01 |
| ...     | ...          | ...          | ...         | ...       | ...        |

---

## 📈 Analysis Performed

- Joined customer and loan data using `customer_id`
- Filtered **approved** vs **rejected** loans
- Exported final dataset to CSV
- (Optional) Built a Power BI dashboard with:
  - Loan approval rate
  - Loan amounts per purpose
  - Credit score patterns

---

## 💡 Key Learnings

- How to create and manage databases using **DB Browser for SQLite**
- How to read, filter, and analyze data using **Python & Pandas**
- How to visualize insights using **Power BI**

---

## 🚀 How to Run This Project

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/loan-approval-analysis
