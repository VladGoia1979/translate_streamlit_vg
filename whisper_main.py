import streamlit as st
import whisper

st.title("Aplicație de translatare (voce în text)")

fisier_audio = st.file_uploader("Încărcare fișier audio", type=["wav", "mp3"])

model = whisper.load_model("large")  # pentru română
#model = whisper.load_model("base")   # pentru engleză

st.text("Modelul Whisper a fost încărcat")

if st.sidebar.button("Transcriere fișier audio"):
    if fisier_audio is not None:
        st.sidebar.success("Se transcrie fișierul audio")

        #if 0==1:
        beam_size=5
        best_of=5
        temperature=(0.0, 0.2, 0.4, 0.6, 0.8, 1.0)
        decode_options = dict(language="ro", best_of=best_of, beam_size=beam_size, temperature=temperature, fp16=False)
        transcribe_options = dict(task="transcribe", **decode_options)
        transcriptie = model.transcribe(fisier_audio.name, **transcribe_options)  # pentru română (inclusiv cu cele 5 linii de mai sus)
        #transcriptie = model.transcribe(fisier_audio.name)                        # pentru engleză

        st.sidebar.success("Transcriere fișier audio completă")
        st.markdown(transcriptie["text"])
    else:
        st.sidebar.error("Vă rugăm să încărcați un fișier audio")

st.sidebar.header("Ascultați fișierul audio original")
st.sidebar.audio(fisier_audio)
