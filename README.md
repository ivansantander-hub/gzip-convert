# Conversor de Archivos Parquet

Este script de Python permite leer archivos Parquet (incluyendo archivos comprimidos con gzip) y convertirlos a formatos JSON y CSV.

## 📋 Descripción

El script `app.py` realiza las siguientes operaciones:

1. **Lee un archivo Parquet** comprimido con gzip
2. **Convierte los datos** a un DataFrame de pandas
3. **Muestra los datos** en la consola
4. **Exporta los datos** a formato JSON (líneas separadas)
5. **Exporta los datos** a formato CSV

## 🚀 Características

- ✅ Soporte para archivos Parquet comprimidos con gzip
- ✅ Conversión automática a JSON y CSV
- ✅ Formato JSON con líneas separadas (JSONL)
- ✅ Exportación CSV sin índices
- ✅ Visualización de datos en consola

## 📦 Dependencias

Este proyecto requiere las siguientes librerías de Python:

- `pandas` - Para manipulación de datos
- `pyarrow` - Para lectura de archivos Parquet

## 🛠️ Instalación

1. **Clonar o descargar** este proyecto
2. **Instalar las dependencias** necesarias:

```bash
pip install pandas pyarrow
```

O usando un archivo requirements.txt:

```bash
pip install -r requirements.txt
```

## 💻 Uso

### Uso Básico

1. **Coloca tu archivo Parquet** en el mismo directorio que el script
2. **Modifica la variable `parquet_file`** en el script con el nombre de tu archivo:

```python
parquet_file = 'tu-archivo.parquet'
```

3. **Ejecuta el script**:

```bash
python app.py
```

### Personalización

Puedes modificar las siguientes variables en el script:

```python
# Archivo de entrada
parquet_file = 'part-example-a89704a8-cf16-4113-bc0e-927557be3f45-c000.gz.parquet'

# Archivos de salida
json_file = 'output6.json'
csv_file = 'output6.csv'
```

## 📁 Estructura de Archivos

```
gzip/
├── app.py                          # Script principal
├── README.md                       # Este archivo
├── part-example-*.gz.parquet       # Archivo Parquet de entrada (ejemplo)
├── output6.json                    # Archivo JSON generado
└── output6.csv                     # Archivo CSV generado
```

## 📤 Formatos de Salida

### JSON (JSONL)
- **Formato**: Una línea por registro
- **Fechas**: Formato ISO 8601
- **Orientación**: Records (cada fila es un objeto JSON)

### CSV
- **Separador**: Coma (`,`)
- **Índices**: No incluidos
- **Encabezados**: Primera fila

## 🔧 Solución de Problemas

### Error: "No module named 'pandas'"
```bash
pip install pandas
```

### Error: "No module named 'pyarrow'"
```bash
pip install pyarrow
```

### Error: "FileNotFoundError"
- Verifica que el archivo Parquet existe en el directorio correcto
- Actualiza la variable `parquet_file` con la ruta correcta

### Error de memoria con archivos grandes
- Para archivos muy grandes, considera procesar por chunks:
```python
# Para archivos grandes, usa:
table = pq.read_table(parquet_file, columns=['columna1', 'columna2'])
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -am 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## ✨ Ejemplos de Uso

### Ejemplo 1: Archivo Parquet Simple
```python
parquet_file = 'datos.parquet'
json_file = 'datos.json'
csv_file = 'datos.csv'
```

### Ejemplo 2: Archivo Comprimido
```python
parquet_file = 'datos_grandes.gz.parquet'
json_file = 'salida_completa.json'
csv_file = 'salida_completa.csv'
```

## 📊 Información Técnica

- **Lenguaje**: Python 3.6+
- **Formato de entrada**: Apache Parquet (.parquet, .gz.parquet)
- **Formatos de salida**: JSON (JSONL), CSV
- **Encoding**: UTF-8
- **Compresión soportada**: gzip

---

💡 **Tip**: Para archivos muy grandes, considera usar `chunksize` en pandas o procesar por columnas específicas para optimizar el uso de memoria. 