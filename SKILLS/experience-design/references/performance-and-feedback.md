# Rendimiento y feedback

## Separar relojes

Medir al menos lo que la afirmación necesita: respuesta local a entrada, primer estado útil, primera salida útil, terminación real y recuperación. Streaming, un spinner o un skeleton no prueban progreso de la tarea. La interacción puede responder rápido mientras el trabajo remoto tarda legítimamente.

Para web, PERF-INP describe un umbral de buena respuesta de INP ≤200 ms al percentil 75 de visitas. No es el percentil 75 de todas las pulsaciones. PERF-VITALS incluye LCP y CLS; como referencia, buenos umbrales son LCP ≤2.5 s y CLS ≤0.1, medidos en su contexto y segmentación. Verificar definiciones vigentes antes de instrumentar.

No reducir UX a estas métricas. En editor, audio, vídeo, canvas o tareas nativas también importan continuidad, cancelación y coste de errores. La cifra histórica de Doherty de 400 ms no es una frontera universal entre usable e inútil.

## Presupuesto de tarea

Definir un objetivo realista con producto, infraestructura y usuarios, no inventar uno después de medir. Explicar qué parte del tiempo controla la interfaz y cuál depende del proceso. Observar distribuciones y casos lentos, no solo media de una máquina potente.

## Feedback proporcional

Confirmar que se recibió la acción sin afirmar que terminó. Con denominador real, mostrar conteo/progreso. Sin él, informar fase y controles disponibles. Las estimaciones deben estar rotuladas y admitir corrección. No usar porcentajes falsos ni retrasos artificiales para fabricar confianza.

Para esperas largas: conservar trabajo, permitir salir/volver cuando se soporte y notificar solo por una vía acordada. Al fallar, diferenciar lo no empezado, lo completado y lo que necesita decisión. Al cancelar, explicar posibles efectos ya producidos.

## Verificación

Reproducir escenarios de red/dispositivo pertinentes: ralentización, fallos y repetición. Registrar las condiciones de medición. Las pruebas sintéticas detectan regresiones técnicas; la rapidez percibida y el éxito del recorrido necesitan evidencia adecuada. No publicar una ganancia porcentual sin baseline comparable.
