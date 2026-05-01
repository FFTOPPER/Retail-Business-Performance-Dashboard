import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- CONFIG ----------
st.set_page_config(page_title="Retail Analytics System", layout="wide")

# ---------- UI STYLE ----------
st.markdown("""
<style>
.kpi-card {
    background: #111827;
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #1f2937;
}

.kpi-value {
    font-size: 26px;
    font-weight: bold;
    color: #22c55e;
}

.kpi-title {
    font-size: 13px;
    color: #9ca3af;
}

.section {
    margin-top: 25px;
}
</style>
""", unsafe_allow_html=True)

# ---------- DATA ----------
@st.cache_data
def load_data():
    df = pd.read_csv("data/customer_shopping_data.csv")
    df["Revenue"] = df["price"] * df["quantity"]
    df["invoice_date"] = pd.to_datetime(df["invoice_date"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["invoice_date"])
    df["Month"] = df["invoice_date"].dt.to_period("M").astype(str)
    df["Year"] = df["invoice_date"].dt.year
    return df

df = load_data()

# ---------- FILTERS ----------
st.sidebar.header("Filters")

category = st.sidebar.multiselect(
    "Category",
    df["category"].unique(),
    default=df["category"].unique()
)

gender = st.sidebar.multiselect(
    "Gender",
    df["gender"].unique(),
    default=df["gender"].unique()
)

year = st.sidebar.multiselect(
    "Year",
    df["Year"].unique(),
    default=df["Year"].unique()
)

filtered_df = df[
    (df["category"].isin(category)) &
    (df["gender"].isin(gender)) &
    (df["Year"].isin(year))
]

# ---------- KPI ----------
total_revenue = filtered_df["Revenue"].sum()
orders = filtered_df["invoice_no"].nunique()
aov = total_revenue / orders if orders else 0

# ---------- TABS ----------
tab1, tab2, tab3 = st.tabs([
    "Executive Overview",
    "Deep Dive Analysis",
    "Insights & Strategy"
])

# =========================================================
# 🟢 TAB 1
# =========================================================
with tab1:

    st.title("Retail Business Performance Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-value">₹ {total_revenue/1e6:.1f}M</div>
    <div class="kpi-title">Total Revenue</div>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-value">{orders:,}</div>
    <div class="kpi-title">Total Orders</div>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
    <div class="kpi-card">
    <div class="kpi-value">₹ {aov:,.0f}</div>
    <div class="kpi-title">Avg Order Value</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Category Revenue Distribution")

    cat = filtered_df.groupby("category", as_index=False)["Revenue"].sum().sort_values("Revenue", ascending=False)

    fig_bar = px.bar(cat, x="category", y="Revenue", color="category")
    st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("### Revenue Trend")

    trend = filtered_df.groupby("Month", as_index=False)["Revenue"].sum().sort_values("Month")

    fig_line = px.line(trend, x="Month", y="Revenue", markers=True)
    st.plotly_chart(fig_line, use_container_width=True)

# =========================================================
# 🔵 TAB 2
# =========================================================
with tab2:

    col4, col5 = st.columns(2)

    with col4:
        st.subheader("Revenue Contribution")
        fig_pie = px.pie(cat, names="category", values="Revenue", hole=0.3)
        st.plotly_chart(fig_pie, use_container_width=True)

    with col5:
        st.subheader("Revenue by Gender")
        gender_df = filtered_df.groupby("gender", as_index=False)["Revenue"].sum()
        fig_donut = px.pie(gender_df, names="gender", values="Revenue", hole=0.5)
        st.plotly_chart(fig_donut, use_container_width=True)

    # ---------- DRILL ----------
    st.markdown("### Dynamic Breakdown")

    option = st.selectbox(
        "Breakdown Level",
        ["Category", "Gender", "Payment Method"]
    )

    mapping = {
        "Category": "category",
        "Gender": "gender",
        "Payment Method": "payment_method"
    }

    drill_df = filtered_df.groupby(mapping[option], as_index=False)["Revenue"].sum()

    fig_drill = px.bar(drill_df, x=mapping[option], y="Revenue", color=mapping[option])
    st.plotly_chart(fig_drill, use_container_width=True)

# =========================================================
# 🟣 TAB 3 (SMART SYSTEM)
# =========================================================
# =========================================================
# 🟣 TAB 3 (SMART SYSTEM)
# =========================================================
with tab3:

    st.markdown("### Key Insights")

    st.write("""
Clothing contributes the largest share of revenue, indicating strong dependency.

Technology operates as a premium segment with high-value transactions.

Food & Beverage shows high volume but lower revenue, indicating margin limitations.

Female customers contribute a larger portion of revenue.

Revenue stabilizes after early peaks, indicating seasonal behavior.
""")

    # ---------- SMART QUERY DROPDOWN ----------
    st.markdown("### Ask Your Data")

    questions = [
        "Total Revenue",
        "Total Orders",
        "Average Order Value",
        "Top Category",
        "Revenue by Category",
        "Revenue by Gender",
        "Revenue by Payment Method",
        "Monthly Revenue Trend",
        "Highest Revenue Category",
        "Lowest Revenue Category"
    ]

    selected_q = st.selectbox("Select a question", questions)

    # ---------- EXECUTION ----------
    if selected_q:

        try:
            if selected_q == "Total Revenue":
                st.success(f"Total Revenue: ₹ {total_revenue:,.0f}")

            elif selected_q == "Total Orders":
                st.success(f"Total Orders: {orders:,}")

            elif selected_q == "Average Order Value":
                st.success(f"Average Order Value: ₹ {aov:,.0f}")

            elif selected_q == "Top Category":
                top_cat = cat.iloc[0]
                st.success(f"Top Category: {top_cat['category']} (₹ {top_cat['Revenue']:,.0f})")

            elif selected_q == "Revenue by Category":
                st.dataframe(cat)

            elif selected_q == "Revenue by Gender":
                gender_df = filtered_df.groupby("gender", as_index=False)["Revenue"].sum()
                st.dataframe(gender_df)

            elif selected_q == "Revenue by Payment Method":
                pay_df = filtered_df.groupby("payment_method", as_index=False)["Revenue"].sum()
                st.dataframe(pay_df)

            elif selected_q == "Monthly Revenue Trend":
                st.dataframe(trend)

            elif selected_q == "Highest Revenue Category":
                max_row = cat.iloc[0]
                st.success(f"{max_row['category']}")

            elif selected_q == "Lowest Revenue Category":
                min_row = cat.iloc[-1]
                st.success(f"{min_row['category']}")

        except Exception:
            st.error("Error processing query")