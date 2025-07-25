
---

## Objective

- Analyze customer churn behavior using the telecom dataset.
- Identify key drivers contributing to customer churn.
- Visualize trends and relationships using a dynamic Power BI dashboard.
- Develop a machine learning model to predict churn probability.

---

## Power BI Dashboard Highlights

![Dashboard Screenshot](./visuals/churn_dashboard.png)

**Key Visuals:**
- 📌 **Overall Churn Rate**: 26.4% churn across 7043 customers.
- 📊 **Monthly Charges vs Churn**: Higher monthly charges correlate with churn risk.
- 📉 **Churn by Contract Type**: Month-to-month contracts show the highest churn.
- 🧠 **Key Influencer Visual**: Identifies top churn contributors like contract type and internet service.
- 🌲 **Decomposition Tree**: Visual drill-down into features like payment method, gender, and service type.
- 🔗 **Churn by Payment Method**: Mailed check and electronic check users show higher churn.
- 📶 **Internet Service vs Churn**: Fiber optic customers churn more than DSL and non-users.
- 📈 **Monthly Charges vs Tenure**: Customers with longer tenure tend to have lower churn.

---

## Data Overview

- **Source**: [IBM Sample Dataset – Telco Customer Churn](https://www.ibm.com/communities/analytics/watson-analytics-blog/guide-to-sample-datasets/)
- **Records**: 7043
- **Features**: Customer demographics, service usage, billing info, and churn flag.

---

## Tools & Technologies

- **Power BI**: Interactive dashboard
- **Python (pandas, matplotlib, seaborn, scikit-learn)**: Data cleaning, EDA, modeling
- **Jupyter Notebook**: Code documentation
- **Git/GitHub**: Version control

---

## Machine Learning

A logistic regression model was built to predict churn using:
- Demographics (gender, senior citizen)
- Tenure, monthly charges
- Internet service, contract type, etc.

**Top Features (by importance):**
- Contract Type
- Tenure
- Monthly Charges
- Internet Service

---

##  How to Run

### Power BI Dashboard
1. Open `churn_dashboard.pbix` in Power BI Desktop.
2. Interact with filters (contract, gender, payment method).
3. Explore decomposition tree and key influencers.

### Python Environment
```bash
# Clone repository
git clone https://github.com/yourusername/telecom-customer-churn.git
cd telecom-customer-churn

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the model
python churn_prediction.py
