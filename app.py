import random
import streamlit as st

# Pagina-instellingen voor de browser (mag maar 1x bovenaan!)
st.set_page_config(page_title="Voor Jildou 🦙", page_icon="🔒")

verberg_streamlit_stijl = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            [data-testid="stToolbar"] {visibility: hidden;}
            
            /* Dit verwijdert specifiek de balk rechtsonderin (Streamlit Cloud badge) */
            div[data-testid="stStatusWidget"] {display: none !important;}
            footer {display: none !important;}
            .viewerBadge_link__jUW_as {display: none !important;}
            iframe[title="Sign in with Google Button"] {display: none !important;}
            </style>
            """
st.markdown(verberg_streamlit_stijl, unsafe_allow_html=True)

# 1. Onthouden of Jildou al is ingelogd
if "ingelogd" not in st.session_state:
    st.session_state.ingelogd = False

# 1. Onthouden of Jildou al is ingelogd
if "ingelogd" not in st.session_state:
    st.session_state.ingelogd = False

# =====================================================================
# PAGINA 1: De Wachtwoordpoort
# =====================================================================
if st.session_state.ingelogd == False:
    st.title("🔒 Geheime toegang...")
    
    # Invoerveld voor het favoriete dier
    antwoord = st.text_input("Hoi Jildou eerst een wachtwoord, wat is je favo dier?").lower().strip()
    
    if st.button("Controleren"):
        if antwoord == "alpaca":
            st.success("GOED, je bent het echt! Je wordt nu doorgestuurd naar de volgende pagina.")
            st.session_state.ingelogd = True
            st.rerun() # Ververs de pagina om direct naar pagina 2 te gaan
        else:
            st.error("Jij bent een imposter")

# =====================================================================
# PAGINA 2: Het Hoofdmenu (als ze is ingelogd)
# =====================================================================
else:
    # Als ze net binnenkomt, vliegen er ballonnen over het scherm!
    if "ballonnen_getoond" not in st.session_state:
        st.balloons()
        st.session_state.ballonnen_getoond = True

    st.title("🎉 Welkom op de volgende pagina!")
    st.write("Je bent succesvol ingelogd, Jildou. Kies hieronder wat je wilt doen:")
    
    st.markdown("---")
    st.subheader("📋 HOOFDMENU")

    # Kolommen maken zodat de knoppen netjes naast elkaar staan
    kol1, kol2, kol3 = st.columns(3)

    with kol1:
        if st.button("🥰 Complimentje krijgen"):
            st.session_state.actie = "compliment"

    with kol2:
        if st.button("🤫 Een geheim horen"):
            st.session_state.actie = "geheim"

    with kol3:
        if st.button("🚪 Uitloggen / Afsluiten"):
            st.session_state.ingelogd = False
            # We wissen de status voor de volgende keer
            del st.session_state.ballonnen_getoond
            if "actie" in st.session_state:
                del st.session_state.actie
            st.rerun()

    # Controleren welke knop is ingedrukt en het bericht tonen
    if "actie" in st.session_state:
        st.markdown("---")
        
        if st.session_state.actie == "compliment":
            st.write("### 🥰 Complimentje!")
            st.write("Je bent de allerknapste vrouw allertijden!! ✨")

        elif st.session_state.actie == "geheim":
            st.write("### 🤫 Geheimpje.")
            st.write("Ik heb een tijdje terug een ijsje van de mac gehad zonder jou maar ik ga het goed maken jildoutje 🍦")
