import streamlit as st
import ollama

st.set_page_config(page_title="CodeLlama Assistant", layout="wide")
st.title("🦙 CodeLlama Code Assistant")

task = st.selectbox(
    "Choose task",
    ["Generate Code", "Explain Code", "Debug Code", "Optimize Code"]
)

user_input = st.text_area("Enter code or prompt", height=250)

if st.button("Run"):
    if not user_input.strip():
        st.warning("Please enter some text")
    else:
        if task == "Generate Code":
            prompt = user_input
        elif task == "Explain Code":
            prompt = f"Explain the following code:\n{user_input}"
        elif task == "Debug Code":
            prompt = f"Debug the following code:\n{user_input}"
        else:
            prompt = f"Optimize the following code:\n{user_input}"

        with st.spinner("Thinking..."):
            response = ollama.chat(
                model="codellama:7b",
                messages=[{"role": "user", "content": prompt}]
            )

        st.subheader("💡 Output")
        st.code(response["message"]["content"])
