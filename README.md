# Web scraping de actividades turísticas

> **Proyecto archivado.** Este repositorio se conserva como referencia histórica y ya no recibe mantenimiento ni actualizaciones.

Proyecto de 2016 que utiliza web scraping para identificar menciones de actividades turísticas en el contenido de una página web y mostrarlas en una aplicación Django.

## Funcionamiento

1. Descarga una página web con `requests` y analiza su HTML con `lxml`.
2. Extrae el texto de etiquetas `div`, `a`, `p` y `span`.
3. Filtra los textos que mencionan un destino, sin distinguir mayúsculas ni acentos.
4. Busca coincidencias con un catálogo de actividades, como buceo, ciclismo, kayak, surf y pesca.
5. Muestra el destino, los textos filtrados y las actividades encontradas en la ruta `/lugares/`.

La configuración incluida consulta `http://agendaculturalzacatecas.com/` y filtra por **Zacatecas**. La detección se basa en coincidencias de texto con un catálogo fijo.

## Tecnologías y estructura

El código utiliza Python 2, Django 1.8.4, `requests`, `lxml` y SQLite.

- `curso/curso/`: configuración y rutas del proyecto Django.
- `curso/lugares/principal.py`: descarga y extracción de texto del HTML.
- `curso/lugares/functions.py`: filtrado por destino y búsqueda de actividades.
- `curso/lugares/views.py`: integración del procesamiento con la vista web.
- `curso/templates/lugares.html`: presentación de los resultados.

## Estado del código

El proyecto conserva su implementación original y dependencias antiguas. No se garantiza su funcionamiento con versiones actuales de Python o Django, ni la disponibilidad o compatibilidad de la página consultada.

## Licencia

Distribuido bajo la licencia BSD de 2 cláusulas. Consulta [LICENSE](LICENSE) para conocer sus términos.
