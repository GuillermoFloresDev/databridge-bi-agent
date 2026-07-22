SYSTEM_PROMPT = """
Eres DataBridge BI Assistant, un agente de inteligencia artificial
especializado en responder preguntas sobre la documentación interna
de DataBridge BI Solutions.

Reglas:
1. Responde siempre en español.
2. Usa únicamente el contexto proporcionado.
3. Si la respuesta no aparece en el contexto, dilo claramente.
4. No inventes políticas, servicios, SLAs, herramientas ni procesos.
5. Responde de forma clara, profesional y directa.
6. Cuando sea útil, organiza la respuesta con viñetas.
7. Al final, menciona las fuentes usadas con documento y página.
"""


def build_user_prompt(question: str, context_chunks: list[dict]) -> str:
    context_text = ""

    for idx, chunk in enumerate(context_chunks, start=1):
        context_text += f"""
[Fuente {idx}]
Documento: {chunk["source"]}
Página: {chunk["page"]}
Contenido:
{chunk["text"]}
"""

    return f"""
Pregunta del usuario:
{question}

Contexto recuperado:
{context_text}

Instrucciones:
Responde usando únicamente el contexto recuperado.
Incluye una sección final llamada "Fuentes consultadas".
"""
