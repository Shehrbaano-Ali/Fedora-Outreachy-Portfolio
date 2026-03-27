import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_gsheets import GSheetsConnection

# Page Config
st.set_page_config(page_title="RamaLama-Saurus Lab", page_icon="🦖", layout="wide")

# Navigation Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="LAB NAV", 
        options=["HOME", "ABOUT", "CONTRIBUTIONS", "PROJECT", "CONTACT"],
        icons=["house", "person-badge", "journal-code", "rocket-takeoff", "envelope"],
        menu_icon="cast", 
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#1a1c24"},
            "icon": {"color": "#00ff41", "font-size": "20px"}, 
            "nav-link-selected": {"background-color": "#2e7bcf"},
        }
    )

# Connect to Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

if selected == "HOME":
    st.title("🦖 RamaLama-Saurus Research Log")
    st.subheader("Official Outreachy 2026 Contribution Hub | Fedora Project")
    st.markdown("---")
    st.info("🧬 **Current Mission:** Developing SLM/LLM RAG Pipeline via RamaLama.")
    st.write("Welcome to the central research log for the Fedora LLM integration project.")

elif selected == "ABOUT":
    st.title("🧬 Principal Investigator Profile")
    st.write("### Specialized in Pattern Recognition")
    st.write("Self-taught Machine Learning builder transitioning from Medical Diagnostic Analysis to Open-Source LLM Architecture.")
    st.success("**Matrix:** @shehrbanoali6:matrix.org | **FAS ID:** shehrbano")

elif selected == "CONTRIBUTIONS":
    st.title("📋 Field Expedition Log")
    st.write("Syncing live from Google Sheets.")
    try:
        # NOTE: Make sure your Google Sheet tab is named "Contributions"
        df = conn.read(worksheet="Contributions", ttl="5m")
        st.dataframe(df, use_container_width=True, hide_index=True)
    except Exception as e:
        st.error("Connection pending. Please configure Secrets in Streamlit Cloud.")

elif selected == "PROJECT":
    st.title("🧪 Future Lab Experiments")
    st.markdown("**Project Title:** Enhancing Fedora Documentation RAG using RamaLama.")
    st.write("Final Proposal Status: *In Research Phase*")

elif selected == "CONTACT":
    st.title("📡 Signal Transmission")
    st.write("Reach out via Matrix: `@shehrbanoali6:matrix.org` or FAS.")
