import streamlit as st

from src.rag_chain import answer_question
from src.retriever import CHUNKS_PATH, EMBEDDINGS_PATH


st.set_page_config(
    page_title="DataBridge BI Assistant",
    page_icon="📊",
    layout="wide",
)


st.title("📊 DataBridge BI Assistant")
st.caption(
    "Asistente inteligente para consultar documentación corporativa "
    "de Business Intelligence."
)


if not CHUNKS_PATH.exists() or not EMBEDDINGS_PATH.exists():
    st.warning(
        "El índice vectorial no existe todavía. "
        "Ejecuta primero: python build_index.py"
    )
    st.stop()


with st.sidebar:
    st.header("Base documental")
    st.markdown(
        """
        Este agente consulta documentos internos de DataBridge BI Solutions:

        1. Manual de Onboarding  
        2. Guía de Modelado Semántico y Power BI  
        3. Guía de Ingeniería de Datos  
        4. Arquitectura BI y Dominios Analíticos  
        5. Protocolo de Incidentes BI  
        6. Catálogo de Servicios y SLAs BI  
        """
    )

    st.divider()

    st.markdown(
        """
        **Ejemplos de preguntas:**

        - ¿Cómo deben nombrarse las medidas DAX?
        - ¿Qué se considera un incidente SEV-1?
        - ¿Qué incluye el plan Enterprise BI?
        - ¿Qué debe hacer un consultor en sus primeros 30 días?
        - ¿Cuáles son las capas de la arquitectura BI?
        """
    )


question = st.text_area(
    "Escribe tu pregunta",
    placeholder="Ejemplo: ¿Cómo deben nombrarse las medidas DAX?",
    height=100,
)


if st.button("Consultar documentación", type="primary"):
    if not question.strip():
        st.error("Por favor, escribe una pregunta.")
        st.stop()

    with st.spinner("Buscando en la documentación y generando respuesta..."):
        result = answer_question(question)

    st.subheader("Respuesta")
    st.write(result["answer"])

    if result["sources"]:
        st.subheader("Fuentes recuperadas")
        for source in result["sources"]:
            st.markdown(
                f"- **{source['source']}**, página {source['page']} "
                f"(score: {source['score']})"
        )
    else:
        st.info("No se consultaron fuentes documentales para esta respuesta.")

