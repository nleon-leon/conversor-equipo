import streamlit as st
from pypdf import PdfWriter
import io

st.set_page_config(page_title="Conversor Maestro", page_icon="🛠️", layout="centered")

# Límite de carga para archivos grandes (1 GB)
if 'config_configurado' not in st.session_state:
    st._config.set_option("server.maxUploadSize", 1024)
    st.session_state['config_configurado'] = True

st.title("🛠️ Navaja Suiza de Archivos")
st.write("Convierte audio, edita PDFs y genera formatos para tu e-Reader en segundos.")

# --- MENSAJE PARA EL EQUIPO ---
st.info("✉️ **Estimado colega, esta aplicación tiene solo disponible para ti la opción de unir PDF, para tu tarea. Atte. Coordinador zona Norte**")
# ------------------------------

tab1, tab2, tab3 = st.tabs(["🎵 Audio", "📄 Editar PDF", "📚 E-Books"])

# ==========================================
# PESTAÑA 1: AUDIO (BLOQUEADA POR ESTRATEGIA)
# ==========================================
with tab1:
    st.header("Conversor de Audio")
    st.caption("Ideal para convertir notas de voz de WhatsApp (.ogg) a .mp3 para NotebookLM")
    
    # Simulación visual para generar curiosidad
    st.file_uploader("Sube tu audio", type=["mp3", "ogg", "wav", "opus"], key="audio_block")
    st.selectbox("Formato de salida", ["mp3", "ogg"], key="format_block")
    
    if st.button("Convertir Audio"):
        st.warning("🔒 **Función bloqueada.** Esta herramienta es de uso exclusivo para el Coordinador de la Zona Norte.")

# ==========================================
# PESTAÑA 2: EDITAR PDF (ÚNICA DISPONIBLE)
# ==========================================
with tab2:
    st.header("Unir Archivos PDF")
    archivos_pdf = st.file_uploader("Selecciona 2 o más PDFs (puedes arrastrar los archivos aquí)", type=["pdf"], accept_multiple_files=True)
    
    if len(archivos_pdf) >= 2 and st.button("Unir PDFs"):
        with st.spinner("Uniendo documentos..."):
            try:
                escritor = PdfWriter()
                for pdf in archivos_pdf:
                    escritor.append(io.BytesIO(pdf.read()))
                
                buffer_pdf = io.BytesIO()
                escritor.write(buffer_pdf)
                
                st.success("¡PDFs unidos con éxito!")
                st.download_button(
                    label="Descargar PDF Unido",
                    data=buffer_pdf.getvalue(),
                    file_name="documento_unido.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"Error al unir los archivos: {e}")

# ==========================================
# PESTAÑA 3: E-BOOKS (BLOQUEADA POR ESTRATEGIA)
# ==========================================
with tab3:
    st.header("Conversor para e-Reader")
    st.caption("Convierte novelas o informes de PDF a formatos EPUB, MOBI o AZW3.")
    
    # Simulación visual para generar curiosidad
    st.file_uploader("Sube tu documento (PDF, EPUB, etc.)", type=["pdf", "epub", "mobi", "azw3"], key="ebook_block")
    st.selectbox("Convertir a:", ["epub", "mobi", "azw3", "pdf"], key="ebook_format_block")
    
    if st.button("Convertir e-Book"):
        st.warning("🔒 **Función bloqueada.** Esta herramienta es de uso exclusivo para el Coordinador de la Zona Norte.")

# ==========================================
# PIE DE PÁGINA (FIRMA)
# ==========================================
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #888888; font-size: 14px;'>"
    "Desarrollado por <strong>Nelson León Carrasco</strong>"
    "</p>", 
    unsafe_allow_html=True
)