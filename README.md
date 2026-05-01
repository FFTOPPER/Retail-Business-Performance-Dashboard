# Retail Business Performance & Revenue Strategy Dashboard

## Live Application

The interactive version of this dashboard is deployed and accessible below:

https://retaildashboardforbusiness.streamlit.app/

---

## Overview

This project presents an end-to-end retail analytics solution designed to evaluate business performance, identify revenue drivers, uncover hidden patterns, and deliver actionable strategic insights.

The workflow follows a structured analytical pipeline:

Excel-based Data Exploration → Power BI Dashboard Development → Streamlit Deployment → Business Insight Generation

---

## Problem Statement

The objective of this project is to analyze multi-category retail transaction data in order to:

* Evaluate overall business performance
* Identify high-performing and underperforming categories
* Analyze revenue trends and seasonality
* Understand customer segments and purchasing behavior
* Detect hidden patterns influencing revenue
* Provide actionable, data-driven business recommendations

---

## Tools and Technologies

* Microsoft Excel (Exploratory Data Analysis)
* Power BI (Dashboard development, DAX modeling)
* DAX (Custom measures and KPIs)
* Python (Pandas, Plotly)
* Streamlit (Interactive web deployment)

---

## Project Architecture

```text
Retail-Business-Performance-Dashboard/
 ┣ streamlit-retail-dashboard/
 ┃ ┣ data/
 ┃ ┃ ┗ customer_shopping_data.csv
 ┃ ┣ app.py
 ┃ ┗ requirements.txt
 ┣ images/
 ┃ ┣ dashboard.png
 ┃ ┣ deep_dive.png
 ┃ ┣ insights.png
 ┣ data.xlsx
 ┣ Retail_Analysis.pbix
 ┗ README.md
```

---

## Data Exploration (Excel)

Initial analysis was conducted in Excel to validate the dataset and identify early business patterns.

Key exploration areas included:

* Category-wise revenue distribution
* Quantity analysis across product categories
* Pricing behavior and average price trends
* Monthly revenue trends
* Initial hypothesis generation

### Excel Analysis

<img width="1872" height="769" src="https://github.com/user-attachments/assets/fa8f83c7-fcbf-40e5-9868-0858e6fce353" />

----

<img width="540" height="476" src="https://github.com/user-attachments/assets/6412aa9b-32c1-4513-9e95-59994933c6da" />

----

<img width="1378" height="364" src="https://github.com/user-attachments/assets/e4b287d2-021b-48c3-a4d9-dd8f5694de61" />

----

<img width="410" height="301" src="https://github.com/user-attachments/assets/71667e06-8f4e-431e-b84f-b5ede7936bdd" />

----

<img width="857" height="271" src="https://github.com/user-attachments/assets/b19d4691-80d1-446a-b92e-faa45dd25836" />

---

## Dashboard Design (Power BI)

### Page 1: Executive Overview

This page provides a high-level summary of business performance.

* Total Revenue
* Total Orders
* Average Order Value
* Category-wise revenue distribution
* Monthly revenue trend and seasonality

![Executive Overview](images/dashboard.png)

---

### Page 2: Deep Dive Analysis

This page enables detailed and interactive exploration of business drivers.

* Category-based filtering (slicers)
* Revenue contribution by category (with grouped minor categories)
* Revenue breakdown by gender
* Decomposition Tree for root cause analysis

Revenue flow analyzed as:

Total Revenue → Category → Gender → Payment Method

![Deep Dive Analysis](images/deep_dive.png)

---

### Page 3: Insights and Recommendations

This page translates analysis into business-level understanding and strategy.

![Insights and Recommendations](images/insights.png)

---

## Key Performance Indicators

* Total Revenue: 251.5 Million
* Total Orders: 99,457
* Average Order Value: 2,529

---

## Key Business Insights

### Revenue Concentration

The top three categories contribute approximately 95 percent of total revenue, with Clothing alone contributing around 45 percent. This indicates strong dependency on a single category.

---

### Premium Segment Behavior

Technology generates high revenue with relatively low quantity, indicating a premium pricing model and high-value transactions.

---

### Volume vs Revenue Imbalance

Food and Beverage shows high transaction volume but lower revenue contribution, indicating low-margin product behavior.

---

### Customer Segment Dominance

Female customers contribute approximately 60 percent of total revenue, indicating a key target segment.

---

### Payment Preferences

Cash transactions dominate over credit card usage, indicating customer preference for traditional payment methods.

---

### Seasonal Trends

Revenue peaks in early months and stabilizes over time, indicating seasonal purchasing patterns and limited growth acceleration.

---

## Hidden Insights

### Dependency Risk

Heavy reliance on the Clothing category creates vulnerability in revenue stability.

---

### Growth Limitation

Stable revenue trends suggest limited scalability without strategic intervention.

---

### High-Value Opportunity

Technology category offers strong expansion potential due to higher revenue per transaction.

---

### Pricing Optimization Potential

Low-value categories provide opportunities for pricing adjustments, bundling, and margin improvement strategies.

---

## Revenue Drivers Analysis

A decomposition tree was implemented to analyze revenue across multiple dimensions:

* Category
* Gender
* Payment Method

This enables:

* Root cause identification
* Multi-level revenue analysis
* Deeper business understanding beyond surface metrics

---

## Streamlit Deployment (Interactive System)

To enhance accessibility and interactivity, the dashboard was rebuilt using Streamlit.

<img width="1828" height="887" alt="image" src="https://github.com/user-attachments/assets/2a12405b-724a-4781-85b1-4abd67c00e07" />

----

<img width="1888" height="1027" alt="image" src="https://github.com/user-attachments/assets/2c181ed9-a93e-4b57-801b-56851e10070c" />

----

<img width="1862" height="965" alt="image" src="https://github.com/user-attachments/assets/ede237e5-867f-4a7f-b0cd-2018cabd8cc9" />

Key features:

* Dynamic filters (category, gender, year)
* Interactive visualizations using Plotly
* Multi-tab navigation (Executive, Deep Dive, Insights)
* Real-time KPI updates
* Smart query system for data exploration
* Drill-down analysis capability

---

## Strategic Recommendations

* Expand premium segments such as Technology
* Reduce dependency on Clothing to mitigate risk
* Improve margins in low-value categories
* Leverage seasonal peaks for targeted marketing campaigns
* Encourage digital payment adoption
* Diversify category portfolio for sustainable growth

---

## Key Learnings

* End-to-end data analytics workflow implementation
* Business-focused dashboard design and storytelling
* Advanced Power BI features (decomposition tree, slicers)
* Translating raw data into actionable insights
* Deploying analytics solutions as interactive web applications

---

## Author

Adheje B
