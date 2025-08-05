# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st

st.write("""
    # Ad platform calculator
    
    This application gives the Target Return on Ad Spend (T-ROAS), Target Cost per Purchase (T-CPP),
    Break Even Return on Ad Spend (BE-ROAS), Break Even Cost per Purchase (BE-CPP), Revenue, Sales, Profit, 
    and Conversion Rate (CR) that an ecommerce store needs to achieve based on other input metrics about the store. 
    Just fill in the following information and click on the Calculate button.
    """)

# Old Text
### Please read the following blog before using this calculator: [link](https://rugwal.com/2022/06/09/chapter-4-ads-calculator/)

# The price your customer is paying
st.write("""### Product Price""")
product_price = st.number_input("Enter the price of the primary product (The price your customer is paying)",
                                min_value=0.0, value=0.01, step=0.01)

# The amount it cost to produce the product
st.write("""### Cost of Goods""")
product_cost = st.number_input("Enter the cost of the primary product (The amount it cost to produce the product, "
                               "including shipping to your warehouse)", min_value=0.0, step=0.01)
shipping_cost = st.number_input("Enter the cost to ship the primary product to the customer", min_value=0.0, step=0.01)
tax_cost = st.number_input("Enter any tax on the primary product", min_value=0.0, step=0.01)

cost_of_goods = product_cost + shipping_cost + tax_cost
tx_fees = product_price * 0.029 + 0.3  # transaction fees

# The amount of fixed (overhead) costs to run the business
st.write("""### Fixed Overhead Costs (Monthly)""")
fixed_costs = st.number_input("Enter the value of the fixed/overhead costs (The amount it costs to keep the business "
                              "running every month, not including variable costs)", min_value=0.00, step=0.01)

# Let the user choose to input dpm, roas, or cr
choice = st.radio('Select an input: ', ['Desired Profit Margins', 'T-ROAS', 'Target Conversion Rate'])

if choice == 'Desired Profit Margins':
    st.write("""### Desired Profit Margin""")
    dpm = st.number_input("Enter the desired profit margin on the primary product", min_value=0.0000,  # desired profit margin
                      max_value=1.0000, value=0.15, step=0.01)
elif choice == 'T-ROAS':
    st.write("""### Target Return on Ad Spend (ROAS)""")
    t_roas = st.number_input("Enter the desired return on ad spend on the primary product", min_value=0.00,
                          max_value=50.00, value=2.50, step=0.01)
else:
    st.write("""### Target Conversion Rate""")
    cv = st.number_input("Enter the desired conversion rate on the primary product", min_value=0.0000,
                          max_value=1.0000, value=0.03, step=0.01)


st.write("""### Cost per Click""")
cpc = st.number_input("Enter the estimated Cost per Click (CPC) the primary product", min_value=0.0, value=0.75,
                      step=0.01)

st.write("""### Adspend""")
adspend_per_day = st.number_input("Enter the amount of ad spend per day on the primary product", min_value=0, value=1,
                                  step=1)





#CALCULATIONS
if choice == 'Desired Profit Margins':
    t_cpp = product_price * (1 - dpm) - cost_of_goods - tx_fees
    t_roas = product_price / t_cpp
    target_revenue_per_day = adspend_per_day * t_roas
    target_sales_per_day = target_revenue_per_day / product_price
    cv = target_sales_per_day / (adspend_per_day / cpc)

if choice == 'T-ROAS':
    t_cpp = product_price / t_roas
    dpm = 1 - ((t_cpp + cost_of_goods + tx_fees) / product_price)
    target_revenue_per_day = adspend_per_day * t_roas
    target_sales_per_day = target_revenue_per_day / product_price
    cv = target_sales_per_day / (adspend_per_day / cpc)

if choice == 'Target Conversion Rate':
    target_sales_per_day = cv * (adspend_per_day / cpc)
    target_revenue_per_day = target_sales_per_day * product_price
    t_roas = target_revenue_per_day / adspend_per_day
    t_cpp = product_price / t_roas
    dpm = 1 - ((t_cpp + cost_of_goods + tx_fees) / product_price)

be_cpp = product_price - cost_of_goods - tx_fees
be_roas = product_price / be_cpp

target_revenue_per_month = target_revenue_per_day * 30
target_revenue_per_year = target_revenue_per_month * 12

be_revenue_per_day = adspend_per_day * be_roas
be_revenue_per_month = be_revenue_per_day * 30
be_revenue_per_year = be_revenue_per_month * 12

# The number of sales

target_sales_per_month = target_sales_per_day * 30
target_sales_per_year = target_sales_per_month * 12

be_sales_per_day = be_revenue_per_day / product_price
be_sales_per_month = be_sales_per_day * 30
be_sales_per_year = be_sales_per_month * 12

profit_per_day = target_revenue_per_day * dpm - (fixed_costs / 30)
profit_per_month = profit_per_day * 30
profit_per_year = profit_per_month * 12

visitors_per_day = adspend_per_day / cpc
visitors_per_month = visitors_per_day * 30
visitors_per_year = visitors_per_month * 12



st.write("""## Results""")
st.write("""#### CPP""")
st.write("Your Target Cost per Purchase (T-CPP) is ", round(t_cpp, 2))
st.write("Your Break Even Cost per Purchase (BE-CPP) is ", round(be_cpp, 2))

st.write("""#### ROAS""")

if choice == 'Desired Profit Margins' or choice == 'Target Conversion Rate':
    st.write("Your Target Return on Ad Spend (T-ROAS) is ", round(t_roas, 2))

st.write("Your Break Even Return on Ad Spend (BE-ROAS) is ", round(be_roas, 2))

st.write("""#### Revenue""")
st.write("Your Target Revenue per Day is ", round(target_revenue_per_day, 2))
st.write("Your Target Revenue per Month is ", round(target_revenue_per_month, 2))
st.write("Your Target Revenue per Year is ", round(target_revenue_per_year, 2))

st.write("Your Break-Even Revenue per Day is ", round(be_revenue_per_day, 2))
st.write("Your Break-Even Revenue per Month is ", round(be_revenue_per_month, 2))
st.write("Your Break-Even Revenue per Year is ", round(be_revenue_per_year, 2))

st.write("""#### Sales""")
st.write("Your Target Sales per Day is ", round(target_sales_per_day, 2))
st.write("Your Target Sales per Month is ", round(target_sales_per_month, 2))
st.write("Your Target Sales per Year is ", round(target_sales_per_year, 2))

st.write("Your Break-Even Sales per Day is ", round(be_sales_per_day, 2))
st.write("Your Break-Even Sales per Month is ", round(be_sales_per_month, 2))
st.write("Your Break-Even Sales per Year is ", round(be_sales_per_year, 2))

if choice == 'Target Conversion Rate' or choice == 'T-ROAS':
    st.write("""#### Desired Profit Margins""")
    st.write("Your Desired Profit Margins are ", round(dpm, 4))

st.write("""#### Profit""")
st.write("Your Target Profit per Day is ", round(profit_per_day, 2))
st.write("Your Target Profit per Month is ", round(profit_per_month, 2))
st.write("Your Target Profit per Year is ", round(profit_per_year, 2))

st.write("""#### Target Number of Visitors""")
st.write("Your Target Visitors per Day is ", round(visitors_per_day, 2))
st.write("Your Target Visitors per Month is ", round(visitors_per_month, 2))
st.write("Your Target Visitors per Year is ", round(visitors_per_year, 2))

if choice == 'Desired Profit Margins' or choice == 'T-ROAS':
    st.write("""#### Target Conversion Rate""")
    st.write("Your Target Conversion Rate is ", round(cv, 4))
