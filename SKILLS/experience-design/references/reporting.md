# Informes y utilidades

## Una fuente de verdad

Cuando el entregable requiere un informe durable, `report.json` es canónico y sigue `assets/report.schema.json`. Una consulta puntual puede resolverse en chat sin crear archivos. No escribir conclusiones distintas en HTML y Markdown. El helper conserva todos los campos y las limitaciones; una presentación editorial puede ser adicional, no reemplazar el registro.

Campos: sesión/autoridad; conclusión; evidencia; cobertura; hallazgos; métricas; decisiones; fuentes adicionales. Cada observación tiene ID. Separar gravedad, confianza, alcance y prueba. Clasificar observación/inferencia/hipótesis. Registrar las fuentes del argumento y los artefactos del producto por separado.

`verified-in-scope` solo expresa la verificación de afirmaciones declaradas en un alcance; no certificación, ausencia global de defectos o eficacia poblacional. No utilizarlo con cobertura desconocida/fallida o riesgos P0/P1 abiertos. Un diseño puede concluir `proposed` y estar correctamente entregado.

## Helper opcional

Python 3.10 o superior; solo biblioteca estándar, sin instalaciones, red, subprocesses, telemetría ni llamadas a modelos. Resolver `<skill-root>` a la carpeta instalada real. Ejecutar `python <skill-root>/scripts/ux.py --help` para la interfaz exacta.

Comandos: `init` crea un registro desconocido/draft; `lookup` filtra fichas; `validate` comprueba estructura y coherencia; `render` genera JSON/Markdown/HTML desde el registro; `doctor` comprueba datos y enlaces. `init` y `render` exigen directorio de salida nuevo y fuera de la skill; no sobrescriben. Consultar `assets/example-report.json` para un ejemplo sintético y `--help` para argumentos exactos.

El formato JSON usa fechas YYYY-MM-DD y rechaza claves duplicadas, NaN/Infinity, campos desconocidos y archivos mayores de 5 MiB. El validador implementa únicamente el subconjunto del schema incluido; no se anuncia como validador JSON Schema general. Falla si el schema incorpora keywords no soportadas.

## Límites deliberados

No comprueba existencia, autenticidad ni contenido de artefactos citados. No analiza si una observación escrita es cierta. No detecta todos los dark patterns ni evalúa un diseño por código. No sustituye inspección humana, pruebas de producto ni la validación canónica del ecosistema. Una referencia declarada correctamente puede seguir siendo falsa: debe inspeccionarse antes de afirmar.

El helper impide algunas contradicciones comprobables: aprobar cobertura sin evidencia compatible, observación humana basada solo en código o simulación, resultado medido sin muestra/fuente, comparación sin baseline, referencias desconocidas y veredicto verificado con P0/P1 abierto.

El ejemplo incluido es sintético, con cobertura desconocida y métricas planeadas. No usar sus cifras o hipótesis como hallazgos de un producto.
