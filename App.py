import streamlit as st

st.set_page_config(page_title="Vendor Payment Decision", page_icon="💰")

st.title("Vendor Payment Decision App")
st.markdown("### Corporate Finance Decision Tool")

st.markdown("---")

# Input Section
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

# Calculation Section
if invoice_amount > 0 and discount_percent > 0 and payment_days > 0:

    discount = discount_percent / 100
    bank_rate = bank_interest_rate / 100
    
    discount_amount = invoice_amount * discount
    effective_return = (discount / (1 - discount)) * (365 / payment_days)

    st.subheader("Results")

    col1, col2 = st.columns(2)

    col1.metric("Discount Amount (₹)", f"{discount_amount:,.2f}")
    col2.metric("Effective Annual Return (%)", f"{effective_return*100:.2f}")

    st.markdown("### Final Decision")

    if bank_interest_rate > 0:
        if effective_return > bank_rate:
            st.success("✔ Pay Early and Take Discount")
            st.write(
                "The effective annual return from early payment is higher than the bank interest rate. "
                "Financially, it is beneficial to pay early."
            )
        else:
            st.error("✖ Do NOT Pay Early")
            st.write(
                "The bank interest rate is higher than the effective return from early payment. "
                "It is better to keep the cash invested."
            )