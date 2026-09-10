# Contrato inclusivo

## Normativa y alcance

Base web de referencia consultada el 2026-09-05: WCAG 2.2. Identificar nivel y criterios aplicables desde W3-WCAG22; estos apuntes no sustituyen el texto normativo ni constituyen auditoría completa. El nivel legal exigible depende del producto y la jurisdicción; verificarlo específicamente cuando sea necesario.

Distinguir 2.5.8 AA (24×24 CSS px o sus excepciones, incluida separación) de 2.5.5 AAA (44×44 y excepciones). 2.4.11 AA evita foco totalmente oculto; no confundirlo con requisitos mejorados. 2.5.7 AA necesita alternativa de puntero sin arrastre cuando corresponde: **un atajo de teclado por sí solo no basta para ese criterio**. Ver W3-TARGET, W3-FOCUS y el estándar.

Autenticación, entrada redundante y ayuda consistente merecen revisión específica. No bloquear pegar contraseñas o usar gestores sin una razón y alternativa conformes. Verificar el texto y las excepciones del criterio relevante.

## Pruebas por tarea

Comprobar nombre, rol, estado y relaciones semánticas; orden y restauración de foco; uso sin ratón; foco visible; errores identificados; alternativas a gestos; lectura y zoom/reflow pertinentes. Revisar contenido dinámico y anuncios de estado sin interrumpir innecesariamente. No confundir orden visual con orden accesible.

Un escáner aporta hallazgos acotados, no una declaración de conformidad. Realizar comprobaciones manuales en estados relevantes. Si no se usa lector de pantalla, declarar esa limitación. No simular su resultado a partir de atributos ARIA. Preferir HTML nativo adecuado antes de añadir semántica redundante.

## Contextos de acceso

Datos largos, RTL, aumento de texto, contraste, modo de alto contraste, movimiento reducido, teclado, tacto, asistencia y red lenta se incorporan según público, comportamiento cambiado y riesgo. No exigir toda combinación cartesiana para una corrección mínima ni omitir una modalidad central por conveniencia.

En canvas, visualizaciones, juegos o editores, no asumir que la representación gráfica es suficiente: definir qué tareas necesitan una alternativa estructurada y cómo se sincronizan selección, nombre y estado. En audio/video o voz, contemplar alternativas adecuadas a la información y operación.

## Cognición

W3-COGA aporta orientación complementaria sobre comprensión y uso; es una nota de grupo, no una certificación WCAG. Aplicar lenguaje claro, conservación de contexto, ayuda y recuperación como hipótesis verificables. Incluir a personas pertinentes en la investigación; no construir una “persona discapacitada” sintética como sustituto.

## Horizonte

WCAG 3 sigue siendo borrador incompleto según W3-WCAG3. Mantenerlo en observación; no marcar sus propuestas como obligaciones vigentes ni prometer un calendario para 2027. Fechar las consultas y registrar cambios que afecten a pruebas o contratos.
