import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Vendor Payment Decision", page_icon="💰")

st.title("Vendor Payment Decision App")
st.markdown("### Advanced Corporate Finance Tool")

st.markdown("---")

# Inputs
st.subheader("Enter Invoice Details")

invoice_amount = st.number_input(
    "Invoice Amount (₹)",
    min_value=0.0,
    step=1000.0,
    format="%.2f"
)

discount_percent = st.number_input(
    "Discount (%) for Early Payment",
    min_value=0.0,
    max_value=100.0,
    step=0.5,
    format="%.2f"
)

payment_days = st.number_input(
    "Payment Due In (Days)",
    min_value=1,
    step=1
)

bank_interest_rate = st.number_input(
    "Bank Interest Rate (% per annum)",
    min_value=0.0,
    max_value=100.0,
    step=0.5,
    format="%.2f"
)

st.markdown("---")

if invoice_amount > 0 and discount_percent > 0 and payment_days > 0:

    discount = discount_percent / 100
    bank_rate = bank_interest_rate / 100

    discount_amount = invoice_amount * discount
    effective_return = (discount / (1 - discount)) * (365 / payment_days)

    st.subheader("Results")

    col1, col2 = st.columns(2)

    col1.metric("Discount Amount (₹)", f"{discount_amount:,.2f}")
    col2.metric("Effective Annual Return (%)", f"{effective_return*100:.2f}")

    st.markdown("### Break-Even Analysis")
    st.write(f"Break-even Bank Interest Rate: **{effective_return*100:.2f}%**")

    if bank_interest_rate > 0:
        if effective_return > bank_rate:
            st.success("✔ Pay Early and Take Discount")
        else:
            st.error("✖ Do NOT Pay Early")

    # Graph Section
    st.markdown("### Sensitivity Analysis (Bank Rate vs Decision)")

    rates = np.linspace(0, 50, 100)
    decision_line = [effective_return*100] * len(rates)

    plt.figure()
    plt.plot(rates, rates)
    plt.plot(rates, decision_line)
    plt.xlabel("Bank Interest Rate (%)")
    plt.ylabel("Effective Return (%)")
    plt.title("Decision Boundary Analysis")

    st.pyplot(plt)