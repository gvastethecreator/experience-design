# Interacción, arquitectura de información y estados

## Modelo antes que pantalla

Identificar objetos del dominio, quién los posee, qué acciones admiten, qué alcance tiene cada acción y qué estados persisten. Mapear rutas principales, entradas profundas, retorno y salidas. Usar verbos que distingan guardar, publicar, aplicar y exportar. Hacer explícitos los límites entre documento, proyecto, cuenta y dispositivo.

Diseñar estados y transiciones junto con layouts. Para cada transición costosa especificar precondición, disparador, cambio local, efecto remoto, feedback, foco, rollback y recuperación. Estado pendiente no es éxito. Un fallo parcial conserva la identidad de elementos completados y pendientes.

## Densidad útil

En herramientas expertas, comparar el coste de escanear información visible con el coste de buscarla en menús o recordarla. La divulgación progresiva es útil para lo infrecuente o contextual, no excusa para ocultar lo central. Mantener comando frecuente, selección, modo y estado cerca del artefacto editado. Evaluar acceso por teclado y atajos descubribles.

Para primeros usos, ofrecer ejemplos y orientación en el punto de necesidad. Para retornos, restaurar contexto pertinente. Evitar personalización que cambie ubicaciones durante una tarea. Los contratos recomendados aquí se apoyan en NN-COMPLEX, NN-MODEL y NN-ACTIVE, pero requieren prueba local.

## Patrones a inspeccionar por riesgo

**Formularios:** etiquetas persistentes, requisito y formato antes del error, valores conservados, errores identificables y corrección sin rehacer todo. Validación inmediata solo cuando hay suficiente información; no castigar a quien todavía está escribiendo.

**Búsqueda y selección:** alcance visible, nombres discriminables, filtros reversibles y diferencia entre sin datos, sin resultados, falta de permiso y fallo. Una acción masiva explicita cuántos elementos selecciona, incluso fuera de página o filtro.

**Guardar/importar/exportar:** distinguir cambios locales y remotos, salida prevista, conflicto de nombres, formatos, sobrescritura y resultado comprobable. No mostrar una descarga como completada solo porque empezó a generarse.

**Destructivas:** conservar contexto y especificar objeto/consecuencia. Undo solo si revierte realmente. Si no puede revertirse, describir límites y exigir revisión proporcional. Separar autenticación de consentimiento al alcance.

**Colaboración:** exponer conflictos, versiones y edición concurrente cuando sean pertinentes. No sobrescribir silenciosamente. Explicar quién puede ver y modificar cada artefacto.

## Ejemplos de aplicación, no auditorías de productos

Editor visual: guardar/exportar/seleccionar una región son contratos distintos. Limpieza del sistema: analizar, seleccionar, ejecutar y recuperar no deben ser un único botón opaco. Estudio musical: evitar interrupciones que alteren reproducción, modo o selección. Biblioteca de assets: diferenciar archivo, categoría, versión y estado de aprobación.

Estos escenarios son ejemplos del dominio; no afirman defectos de un repositorio no inspeccionado.

## Entrega mínima

Una transición se entrega con disparador, alcance, estado resultante y prueba. Un recorrido material añade estados de fallo relevantes y contrato de datos. Solo añadir un diagrama, tabla o prototipo cuando reduce una ambigüedad real. Para uno o dos estados, la prosa precisa puede ser suficiente.
