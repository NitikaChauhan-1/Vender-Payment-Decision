# Vendor Payment Decision App

## 📌 Project Overview
This application helps businesses decide whether to pay suppliers early to avail a cash discount.

It calculates:
- Discount Amount
- Effective Annual Return from Early Payment
- Final Financial Decision

## 📊 Problem Statement
If a supplier offers a discount for early payment (e.g., 3% discount if paid within 30 days), should the company pay early or keep the money in the bank earning interest?

## 🧮 Financial Logic Used
Effective Annual Return Formula:

Effective Return = (Discount / (1 - Discount)) × (365 / Payment Days)

The app compares:
- Effective Return from Early Payment
- Bank Interest Rate

Then provides a financial decision.

## 🚀 Technologies Used
- Python
- Streamlit

## ✅ Example Case
Invoice Amount: ₹100,000  
Discount: 3%  
Payment Days: 30  
Bank Interest Rate: 5%

Effective Return ≈ 37.63%  

Decision: Pay Early and Take Discount
