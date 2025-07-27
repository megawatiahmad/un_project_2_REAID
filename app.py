import streamlit as st

st.set_page_config(page_title="Chatbot Offline")
st.title("🤖 Chatbot Sederhana (Tanpa API Key)")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Fungsi logika chatbot
def jawab_bot(pesan):
    pesan = pesan.lower()
    if "halo" in pesan or "hai" in pesan:
        return "Halo juga! Ada yang bisa saya bantu?"
    elif "siapa kamu" in pesan:
        return "Saya chatbot sederhana buatan Python untuk tugas sekolah 😊"
    elif "tugas" in pesan:
        return "Tenang, kita kerjakan tugasnya sama-sama ya!"
    elif "terima kasih" in pesan:
        return "Sama-sama! Semangat terus ya."
    else:
        return "Maaf, saya belum bisa menjawab itu."

# Tampilkan pesan sebelumnya
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input pengguna
if prompt := st.chat_input("Tulis pesan kamu di sini..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = jawab_bot(prompt)
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
