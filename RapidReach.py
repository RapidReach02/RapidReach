
import streamlit as st
from streamlit.components.v1 import html

# ---------- Styles ----------
st.markdown("""
    <style>
    .fixed-header {
        position: fixed;
        top: 0;
        width: 100%;
        background-color: black;
        color: white;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        padding: 20px 0;
        z-index: 1000;
    }

    .fixed-tabs {
        position: fixed;
        top: 70px;
        width: 100%;
        background-color: #111;
        display: flex;
        justify-content: center;
        gap: 30px;
        padding: 10px 0;
        z-index: 999;
    }

    .tab-button {
        background: none;
        border: none;
        color: white;
        font-size: 16px;
        cursor: pointer;
        padding: 6px 16px;
    }

    .tab-button.active {
        color: #00dd44;
        border-bottom: 2px solid #00dd44;
    }

    .content-wrapper {
        margin-top: 140px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Custom Header ----------
html("""<div class='fixed-header'>The RapidReach</div>""")

# ---------- Simulated Tabs ----------
if 'selected_tab' not in st.session_state:
    st.session_state.selected_tab = "About the Device"

tab_names = ["About the Device", "About the Team", "Market Size"]

buttons = []
tab_html = "<div class='fixed-tabs'>"
for name in tab_names:
    active_class = "active" if st.session_state.selected_tab == name else ""
    tab_html += f"""
        <form action="" method="post">
            <button name="tab" type="submit" value="{name}" class="tab-button {active_class}">{name}</button>
        </form>
    """
tab_html += "</div>"

html(tab_html)

# ---------- Handle Tab Switching ----------
tab = st.query_params().get("tab", [None])[0]
if st.session_state.get("tab"):
    st.session_state.selected_tab = st.session_state.tab
    del st.session_state.tab

# ---------- Main Content ----------
st.markdown("<div class='content-wrapper'>", unsafe_allow_html=True)

if st.session_state.selected_tab == "About the Device":
    st.subheader("About the Device")
    st.write("This is information about the device.")
elif st.session_state.selected_tab == "About the Team":
    st.subheader("About the Team")
    st.write("This is information about the team.")
elif st.session_state.selected_tab == "Market Size":
    st.subheader("Market Size")
    st.write("This is information about the market size.")

st.markdown("</div>", unsafe_allow_html=True)