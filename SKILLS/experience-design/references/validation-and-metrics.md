# Validación de UX y medición

## Elegir el nivel correcto

**Código:** prueba de implementación o regla estática. **Navegador:** controles y transiciones ejecutados en un entorno. **Render:** apariencia en viewport/estado declarados. **Participantes:** comprensión y conducta observada en muestra descrita. **Analítica/experimento:** métricas instrumentadas con diseño de comparación explícito.

Ninguno absorbe automáticamente a los demás. Un test Playwright que recorre un flujo no demuestra que una persona lo descubrirá. Una preferencia estética no prueba productividad. Un error observado no justifica extrapolar prevalencia a toda la población.

## Objetivo, señal, métrica

Usar RES-HEART para orientar la elección, no para obligar a medir todas sus dimensiones. Ejemplo propio: objetivo “exportar la selección correcta”; señal “archivo corresponde a elementos elegidos”; métrica “proporción de tareas completadas sin exportación incorrecta”. Añadir guardrail de pérdida de trabajo y medida de confianza/comprensión cuando sea pertinente.

Preferir métricas de resultado: tarea correcta, errores, ayudas, abandono justificado, recuperación, tiempo hasta valor y esfuerzo percibido. Retorno o conversión pueden ser relevantes, pero no deben premiar compulsión, ocultación de costes o consentimiento defectuoso. Menos clics no es éxito si aumenta errores.

## Protocolo de comparación

Fijar pregunta, población, unidad de análisis, baseline, variantes, método, variable principal, guardrails y criterio de decisión antes de observar resultados. Mantener tarea y datos equivalentes. Contrabalancear orden cuando el aprendizaje importe. Registrar exclusiones, fallos, ayuda y condiciones del dispositivo.

Un A/B necesita instrumentación fiable, asignación apropiada y planificación de muestra/precisión según efecto de interés y tráfico. No inventar tamaño universal. Evitar detener al primer resultado favorable. Si no hay evidencia suficiente, informar incertidumbre; “no significativo” no equivale a “son iguales”.

Sin tráfico o presupuesto, una prueba cualitativa puede resolver ambigüedades y detectar daños. No convertirla en un porcentaje de mejora comercial. Si faltan participantes, dejar protocolo preparado y resultado sin medir.

## Experiencia de IA

Medir no solo aceptación, sino aceptación incorrecta, correcciones, capacidad de detectar límites y recuperación del control. Segmentar por conocimiento y riesgo cuando proceda. Una IA más convincente puede aumentar satisfacción mientras empeora decisiones; verificar ambas cosas.

## Pruebas de la propia skill

Distinguir tres preguntas: ¿se activa donde corresponde?, ¿sigue un buen proceso?, ¿mejora resultados a coste razonable? Fixtures estáticos solo describen casos. Para eficacia, comparar mismo modelo/configuración/tarea/permisos, con y sin skill, en contextos limpios. Conservar outputs y rastros; evaluar sin mostrar al juez cuál es candidato. No incluir respuestas esperadas en el contexto del ejecutor.

Usar casos centrales, variaciones, límites y holdout. Registrar calidad, errores, alcance indebido, tiempo, tokens y utilidad humana. Una ganancia que triplica coste es un tradeoff, no un éxito gratuito. No declarar mejora hasta correr esa comparación. Ver el protocolo de mantenimiento y `evals/evals.json`.
