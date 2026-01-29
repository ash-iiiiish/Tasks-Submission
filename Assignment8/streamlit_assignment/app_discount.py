import streamlit as st

st.title("Price Calculator")

price = st.number_input("Enter product price", min_value=0.0)
discount = st.slider("Select discount percentage", 0, 50)

if st.button("Calculate"):
    final_price = price - (price * discount / 100)
    
    st.success(f"Final Price: {final_price}")

    # Optional comparison table
    st.table([
        ["Before", price],
        ["After", final_price]
    ])
