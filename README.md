# kpi-calculator-streamlit
Interactive Streamlit app to calculate ideal KPIs for any e-commerce product

# KPI Calculator – Streamlit App

An interactive Streamlit web app that calculates ideal KPIs like Target ROAS, Target CPP, Break-Even ROAS, and Profit for any e-commerce product. Built to help paid media specialists, e-commerce founders, and marketers determine whether their product is profitable before launching ads.

**🔗 Live App:** [https://ads-calc4.herokuapp.com/](https://ads-calc4.herokuapp.com/)

---

## 📌 Features

- Choose one of 3 inputs:  
  - Desired Profit Margin  
  - Target ROAS  
  - Target Conversion Rate  

- Automatically calculates:
  - **T-ROAS**: Target Return on Ad Spend
  - **T-CPP**: Target Cost per Purchase
  - **BE-ROAS**: Break-Even ROAS
  - **BE-CPP**: Break-Even CPP
  - **Daily, Monthly, and Yearly Revenue, Sales, and Profit**
  - **Target Visitors & Conversion Rate**

- Designed for performance marketing analysis and forecasting

---

## 📊 Example Inputs

- Product price
- Cost of goods sold (including shipping/tax)
- Ad spend per day
- CPC (Cost per Click)
- Overhead costs

---

## 🧠 Calculations Used

- ROAS = Revenue / Ad Spend  
- CPP = Product Price × (1 - Margin) - Costs  
- BE-CPP = Price - Total Costs  
- Visitors = Ad Spend / CPC  
- Profit = Revenue × Margin - Overhead

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Heroku (for deployment)

---

## 🚀 Getting Started Locally

### 1. Clone the repository

```bash
git clone https://github.com/rugvedwal/kpi-calculator-streamlit.git
cd kpi-calculator-streamlit
