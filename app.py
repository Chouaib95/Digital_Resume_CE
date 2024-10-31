from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Chouaib EDDARBALI"
PAGE_ICON = ":handshake:"
NAME = "Chouaib EDDARBALI"
DESCRIPTION = """
Ingénieur télécom 🛠️ | Developpeur Python 🐍 | Passionné d'IA & de Data Science 🤖.
"""
EMAIL = "ceddarbali@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/chouaib-eddarbali-95070py/",
    "GitHub": "https://github.com/Chouaib95",
}
PROJECTS = {
    "🏆 Développement d'Outils d'Automatisation des Processus Métiers avec Python 3": "",
    "🏆 Utilisation des Bandes Satellitaires (Landsat 8) pour l'Évaluation des Températures et l'Acquisition de Données Géographiques": "",
    "🏆 Exploitation des Plans d'Élévation Digitaux pour la Génération de Cartes Précises": "",
    "🏆 Développement d'un Programme de Traçage des Bornes de Recharge Électrique en Fonction des Régions Françaises": "",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
st.markdown(
    """
    <style>
        /* Applique un fond de page en dégradé */
        html, body, [data-testid="stAppViewContainer"] {
            height: 100%;
            background: linear-gradient(135deg, #400652, #0e3147);
        }
    </style>
    """,
    unsafe_allow_html=True
)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Télécharger mon CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Expériences & Qualifications")
st.write(
    """
- ✔️ 4 ans d'expérience en ingénierie télécom performant la résolution de problémes liés aux réseaux à fibres optiques
- ✔️ Solide expérience pratique et connaissance en Python et Excel
- ✔️ Bonne compréhension des principes statistiques et de leurs applications respectives
- ✔️ Excellent esprit d'équipe et affichant un fort sens de l'initiative dans les tâches
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Compétences Techniques")
st.write(
    """
- 👩‍💻 Programmation: Python (Scikit-learn, Pytorch, Keras, Pandas), SQL
- 🌍 SIG: Arcgis & Qgis
- 📊 Data Viz: Matplotlib, MS Excel, Plotly & Dash , Streamlit
- 📚 Modélisation: Apprentissage supervisé, Apprentissage non supervisé, Traitement du langage naturel (NLP), Machine Learning pour la santé
- 🗄️ Bases de données utilisées: Postgres, MongoDB, MySQL, deta
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Historique Professionnel")
st.write("---")

# --- JOB 1
st.write("🚧", "**Ingénieur d’études et conception | Axione**")
st.write("02/2021 - Aujourd'hui")
st.write(
    """
- ► Dimensionner les réseaux pour répondre au besoin de desserte
- ► Optimiser les infrastructures de l’entreprise
- ► Développer des outils informatiques pour automatiser des parties du processus métier
- ► Maitriser les règles d'utilisation des infrastructures mobilisables (Orange, ERDF)
- ► Produire des calculs de charge des supports aériens
- ► Etablir et publier les livrables nécessaires aux travaux
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projets et Réalisations")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
