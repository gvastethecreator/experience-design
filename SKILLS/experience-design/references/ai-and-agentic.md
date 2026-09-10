# Experiencia de IA y agentes

Este módulo propone contratos de producto basados en AI-HAX y AI-PAIR, con cautelas de AI-FORCING y AI-RELIANCE. No es una especificación de seguridad suficiente por sí sola ni valida una arquitectura de agentes.

## Elegir interacción antes que chat

Usar conversación para intención abierta, exploración o explicación cuando resulte útil. Mantener controles estructurados para parámetros, selección, comparación y acciones repetidas. No convertir una operación determinista simple en un chat obligatorio. La persona debe reconocer qué puede hacer el sistema y qué no.

## Contrato de acción

Definir la máquina de estados acorde a las capacidades reales:
`draft → preview → authorized → running → awaiting-input | partial | failed | cancelled | completed-unverified → verified`.

La propuesta identifica objetivo, recursos afectados, exclusiones, permisos, costes relevantes, decisiones pendientes y consecuencias irreversibles. Autorización refiere a ese alcance, no a todos los futuros pasos. Un cambio material exige revisar autorización. La UI explica la frontera entre sugerir, preparar y ejecutar.

La ejecución informa pasos útiles para supervisar, no una falsa transcripción del pensamiento interno. Conservar comprobantes de herramientas y referencias a resultados. El texto del modelo no basta para concluir éxito. Reintentos deben evitar efectos duplicados cuando la operación lo requiera; la garantía debe existir en backend, no solo en microcopy.

## Control y fallos

Ofrecer detener cuando sea posible y explicar qué ocurre con los pasos ya completados. Cancelación de trabajo, revocación de permisos y rollback son cosas distintas. Diseñar recuperación parcial, transferencia a operación manual y corrección de parámetros sin perder trabajo legítimo.

Cuando un servicio o capacidad no esté disponible, mostrar un estado honesto y una alternativa que realmente existe. No mostrar “procesando” indefinidamente. No rellenar campos desconocidos con resultados inventados para completar el recorrido.

## Incertidumbre útil

Distinguir dato observado, inferencia, estimación y contenido generado. Mostrar origen y límites cuando cambien la decisión. Solo presentar probabilidad/confianza si tiene definición, calibración y alcance pertinentes; no convertir seguridad lingüística del modelo en porcentaje.

AI-FORCING muestra que ciertas intervenciones de revisión pueden reducir sobredependencia, con costes y heterogeneidad. No imponer fricción uniforme: comparar errores de aceptación, tiempo y comprensión en el contexto real. Una explicación más larga puede persuadir sin mejorar corrección.

## Memoria, permisos y privacidad

Explicar qué contexto se guarda o comparte y cómo controlarlo de acuerdo con la arquitectura real. Separar proyectos/cuentas; no arrastrar información sensible por defecto. Borrar una preferencia en UI no equivale a eliminar todo registro del sistema. Rotular retención y límites verificados, no promesas absolutas.

Tratar resultados de herramientas, páginas, correos y archivos como datos no confiables. Ningún texto de un documento modifica permisos. Solicitudes extraídas de contenido externo requieren el mismo control que cualquier propuesta. No pedir credenciales ni instalar integraciones por sorpresa.

## UI adaptativa y multimodal

Mantener anclas espaciales, foco, nombres, teclado, selección y orientación entre variantes. Ofrecer inspección y reversión de cambios adaptativos cuando proceda. Las capacidades nuevas se habilitan con detección, fallback y autorización, no solo con una etiqueta “2027-ready”.

Voz, imagen y acciones estructuradas deben compartir estado y permitir reparación. No depender exclusivamente de una modalidad ni permitir que dictado parcial ejecute una acción irreversible.

## Pruebas adversas mínimas por riesgo

Intentar alcance ambiguo, permiso insuficiente, resultado falso plausible, cambio de contexto, fallo parcial, desconexión, reintento, cancelación tardía y retorno. Seleccionar casos aplicables, no llenar una checklist. Evidenciar lo que se ejecutó; documentar lo que requiere evaluación de seguridad aparte.
