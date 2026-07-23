# DataBridge BI Assistant

DataBridge BI Assistant es un agente inteligente desarrollado para consultar documentación corporativa de una empresa ficticia de Business Intelligence llamada *DataBridge BI Solutions*.

El proyecto fue creado como parte del *Challenge Alura*. El objetivo principal es demostrar cómo un agente de IA puede responder preguntas en lenguaje natural utilizando documentos PDF como fuente de conocimiento.

La solución implementa una arquitectura RAG, Retrieval-Augmented Generation, utilizando documentos internos en PDF, embeddings semánticos, búsqueda vectorial local y generación de respuestas con Cohere.

---

## Descripción general del proyecto

DataBridge BI Solutions es una consultora ficticia especializada en:

- Business Intelligence.
- Power BI.
- Modelado semántico.
- Ingeniería de datos.
- Gobierno de datos.
- Calidad de datos.
- Soporte y operación de soluciones BI.

El agente permite hacer preguntas sobre la documentación interna de la empresa y recibir respuestas basadas en los documentos cargados.

Ejemplos de uso:

- Consultar estándares de nomenclatura DAX.
- Entender cómo se clasifican incidentes BI.
- Revisar procesos de onboarding.
- Consultar servicios y SLAs.
- Explorar la arquitectura analítica de la empresa.
- Revisar reglas de calidad e ingeniería de datos.

---

## Problema que resuelve

En muchas organizaciones, la documentación técnica, operativa y comercial se encuentra distribuida en múltiples archivos PDF, manuales, guías y protocolos. Esto dificulta que nuevos colaboradores o usuarios internos encuentren rápidamente respuestas confiables.

Este proyecto resuelve ese problema creando un agente capaz de:

1. Leer documentos PDF.
2. Procesar su contenido.
3. Dividir el texto en fragmentos consultables.
4. Crear embeddings semánticos.
5. Recuperar los fragmentos más relevantes ante una pregunta.
6. Generar una respuesta clara utilizando el contexto documental.
7. Mostrar las fuentes utilizadas.

---

## Base documental utilizada

La base de conocimiento está formada por 6 documentos PDF generados para la empresa ficticia *DataBridge BI Solutions*:

```text
docs/
├── 01_Manual_Onboarding_Consultores_BI_DataBridge_BI_Solutions.pdf
├── 02_Guia_Oficial_Modelado_Semantico_y_PowerBI_DataBridge_BI_Solutions.pdf
├── 03_Guia_Oficial_Ingenieria_de_Datos_DataBridge_BI_Solutions.pdf
├── 04_Arquitectura_Soluciones_BI_y_Mapa_Dominios_Analiticos_DataBridge_BI_Solutions.pdf
├── 05_Protocolo_Incidentes_Datos_y_Reportes_BI_DataBridge_BI_Solutions.pdf
└── 06_Catalogo_Servicios_y_SLAs_BI_DataBridge_BI_Solutions.pdf