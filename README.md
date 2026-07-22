# DataBridge BI Assistant

DataBridge BI Assistant es un agente inteligente desarrollado como proyecto final del challenge Alura Agente de Alura Latam y Oracle Next Education.

El objetivo del proyecto es permitir que colaboradores de una empresa ficticia de Business Intelligence consulten documentación corporativa mediante preguntas en lenguaje natural.

## Empresa ficticia

DataBridge BI Solutions es una consultora especializada en Business Intelligence, ingeniería de datos, Power BI, modelado semántico, gobierno de datos y soporte analítico.

## Documentos utilizados

La base de conocimiento está formada por 6 documentos PDF:

1. Manual de Onboarding para Nuevos Consultores BI
2. Guía Oficial de Modelado Semántico y Power BI
3. Guía Oficial de Ingeniería de Datos
4. Arquitectura de Soluciones BI y Mapa de Dominios Analíticos
5. Protocolo de Incidentes de Datos y Reportes BI
6. Catálogo de Servicios y SLAs BI

## Arquitectura

```text
Usuario
   ↓
Streamlit App
   ↓
Pregunta en lenguaje natural
   ↓
Embedding de la pregunta con Cohere
   ↓
Búsqueda semántica local con NumPy
   ↓
Chunks relevantes de los documentos
   ↓
Cohere Chat
   ↓
Respuesta fundamentada