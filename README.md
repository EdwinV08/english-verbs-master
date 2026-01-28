# 🎓 English Verb Master Pro

<div align="center">

![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)



</div>

---

## 📋 Tabla de Contenidos

- [Acerca del Proyecto](#-acerca-del-proyecto)
- [Características](#-características)
- [Demo](#-demo)
- [Tecnologías](#️-tecnologías-utilizadas)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Dataset](#-dataset)
- [Roadmap](#-roadmap)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)
- [Contacto](#-contacto)
- [Agradecimientos](#-agradecimientos)

---

## 🎯 Acerca del Proyecto

**English Verb Master Pro** es una aplicación web educativa construida con **Streamlit** que transforma el aprendizaje de verbos en inglés en una experiencia interactiva y divertida. 

### 🤔 ¿Por qué este proyecto?

Aprender las formas irregulares de los verbos en inglés puede ser tedioso y aburrido. Esta aplicación resuelve ese problema mediante:
- **Gamificación**: Sistema de puntos, rachas y rangos que motivan el aprendizaje continuo
- **Feedback Inmediato**: Saber al instante si acertaste o fallaste, con las respuestas correctas
- **Repetición Espaciada**: Sistema que identifica verbos difíciles para repasarlos
- **Aprendizaje Activo**: No solo leer, sino practicar activamente cada verbo

### 🎓 ¿Para quién es?

- Estudiantes de inglés (niveles A2-B2)
- Profesores que buscan herramientas interactivas
- Autodidactas que quieren mejorar su inglés
- Cualquier persona preparándose para exámenes de inglés

---

## ✨ Características

### 🎮 Modos de Aprendizaje

#### 1. **Entrenador Interactivo**
- Sistema de opciones múltiples con 4 alternativas
- Validación inteligente de respuestas (soporta variantes como was/were, got/gotten)
- Feedback visual instantáneo con animaciones
- Sistema de puntuación progresivo:
  - **15 puntos base** por respuesta correcta
  - **+2 puntos por cada racha** (máx. 50 puntos bonus)
  - **-5 puntos** por respuesta incorrecta

#### 2. **Diccionario Completo**
- Búsqueda rápida con autocompletado
- Información detallada de cada verbo:
  - Infinitivo, Past Simple, Past Participle
  - Traducción al español
  - Ejemplo de uso en contexto
  - Tipo (regular/irregular)
- Tabla completa con todos los verbos
- Filtros por tipo de verbo
- Botón de práctica directa desde el diccionario

#### 3. **Sistema de Progreso**
- Dashboard personalizado con estadísticas en tiempo real
- Métricas clave:
  - Puntuación total
  - Precisión porcentual
  - Racha actual y mejor racha
  - Tiempo de estudio
- Sistema de rangos:
  - 🥚 **Newbie** (0-49 puntos)
  - 🌱 **Beginner** (50-149 puntos)
  - 📚 **Intermediate Student** (150-299 puntos)
  - ⭐ **Advanced Learner** (300-499 puntos)
  - 🏆 **Verb Master** (500+ puntos)
- Lista de verbos para repasar (errores cometidos)
- Barra de progreso hacia el siguiente rango

### 🧠 Características Avanzadas

- **Algoritmo de Distractores Inteligentes**: Genera opciones de respuesta que comienzan con la misma letra para aumentar la dificultad
- **Sistema de Rachas**: Motiva a mantener respuestas correctas consecutivas con bonificaciones
- **Modo de Práctica Personalizado**: Enfócate solo en verbos regulares, irregulares o ambos
- **Registro de Errores**: Identifica y guarda verbos difíciles para repasarlos después
- **Caché de Datos**: Carga rápida del dataset con `@st.cache_data`
- **Diseño Responsivo**: Interfaz optimizada para desktop, tablet y móvil

### 🎨 Diseño e Interfaz

- **Cards Animadas**: Diseño moderno con gradientes y sombras
- **Feedback Visual**: Colores y animaciones según el resultado
- **Estadísticas en Tiempo Real**: Métricas actualizadas instantáneamente
- **Badges Dinámicos**: Indicadores visuales de racha y progreso
- **Tema Profesional**: Paleta de colores cuidadosamente seleccionada

---



## 🛠️ Tecnologías Utilizadas

### Core
- **[Python 3.9+](https://www.python.org/)** - Lenguaje de programación
- **[Streamlit 1.31.0](https://streamlit.io/)** - Framework de UI para aplicaciones de datos
- **[Pandas 2.1.4](https://pandas.pydata.org/)** - Manipulación y análisis de datos

### Adicionales
- **CSV** - Almacenamiento de datos
- **Git** - Control de versiones
- **Markdown** - Documentación

### Herramientas de Desarrollo
- **VS Code** - IDE recomendado
- **Git Bash / PowerShell** - Terminal
- **Virtual Environment** - Aislamiento de dependencias

---

## 📥 Instalación

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.9 o superior** → [Descargar Python](https://www.python.org/downloads/)
- **pip** (incluido con Python)
- **Git** → [Descargar Git](https://git-scm.com/downloads)

### Instalación Paso a Paso

#### 1️⃣ Clonar el Repositorio
```bash
git clone https://github.com/TU_USUARIO/english-verb-master.git
cd english-verb-master
```

#### 2️⃣ Crear Entorno Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Instalar Dependencias
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4️⃣ Verificar Estructura de Archivos

Asegúrate de tener esta estructura:
```
english-verb-master/
├── app.py
├── requirements.txt
├── README.md
└── data/
    └── english_verbs_dataset.csv
```

#### 5️⃣ Ejecutar la Aplicación
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

---

## 💻 Uso

### Inicio Rápido

1. **Selecciona el tipo de verbos** en el sidebar (Mixto, Regular, Irregular)
2. **Responde las preguntas** seleccionando las formas correctas
3. **Click en "Verificar"** para ver si acertaste
4. **Mantén rachas altas** para obtener más puntos
5. **Consulta tu progreso** en la pestaña de estadísticas

### Modos de Uso

#### 🎮 Modo Entrenador
```
1. El sistema muestra un verbo en infinitivo
2. Lee la traducción y el ejemplo
3. Selecciona el Past Simple correcto
4. Selecciona el Past Participle correcto
5. Verifica tu respuesta
6. Avanza al siguiente verbo
```

#### 🔍 Modo Diccionario
```
1. Usa el buscador para encontrar un verbo
2. Revisa sus formas y ejemplos
3. Filtra por tipo (regular/irregular)
4. Practica directamente desde ahí
```

#### 📈 Modo Progreso
```
1. Revisa tus estadísticas generales
2. Consulta tu rango actual
3. Ve cuántos puntos necesitas para subir
4. Repasa los verbos donde fallaste
```

### Comandos Útiles
```bash
# Ejecutar la app
streamlit run app.py

# Ejecutar en un puerto específico
streamlit run app.py --server.port 8080

# Modo de desarrollo (auto-reload)
streamlit run app.py --server.runOnSave true

# Ver ayuda de Streamlit
streamlit --help
```

---

## 📂 Estructura del Proyecto
```
english-verb-master/
│
├── 📄 app.py                          # Aplicación principal de Streamlit
│   ├── 🎨 Configuración de página
│   ├── 💾 Carga de datos (@st.cache_data)
│   ├── 🎮 Lógica del juego
│   ├── 📊 Sistema de puntuación
│   └── 🖥️ Interfaz de usuario (3 pestañas)
│
├── 📋 requirements.txt                # Dependencias del proyecto
│   ├── streamlit==1.31.0
│   ├── pandas==2.1.4
│   └── python-dotenv==1.0.0
│
├── 📖 README.md                       # Este archivo
│
├── 📁 data/                           # Carpeta de datos
│   └── 📊 english_verbs_dataset.csv  # Dataset de verbos (98 verbos)
│
├── 🔐 .gitignore                      # Archivos ignorados por Git


```

### Descripción de Archivos Clave

| Archivo | Descripción |
|---------|-------------|
| `app.py` | Contiene toda la lógica de la aplicación: UI, juego, estadísticas |
| `requirements.txt` | Lista de paquetes Python necesarios |
| `data/english_verbs_dataset.csv` | Base de datos de verbos con 4 columnas |
| `.gitignore` | Define qué archivos no subir a Git (venv, cache, etc.) |

---

## 📊 Dataset

### Estructura del CSV

El archivo `english_verbs_dataset.csv` contiene **98 verbos** organizados en 4 columnas:

| Columna | Descripción | Ejemplo |
|---------|-------------|---------|
| `base` | Forma infinitiva del verbo | `go` |
| `past` | Past Simple (puede tener variantes) | `went` |
| `past_participle` | Past Participle | `gone` |
| `type` | Tipo de verbo | `irregular` |

### Ejemplo de Datos
```csv
base,past,past_participle,type
be,was/were,been,irregular
go,went,gone,irregular
eat,ate,eaten,irregular
write,wrote,written,irregular
play,played,played,regular
study,studied,studied,regular
```

### Estadísticas del Dataset

- **Total de verbos:** 98
- **Verbos irregulares:** 53 (54%)
- **Verbos regulares:** 45 (46%)
- **Verbos con variantes:** 2 (`be`, `get`)

### Expandir el Dataset

Para agregar más verbos, simplemente edita `data/english_verbs_dataset.csv`:

1. Abre el archivo CSV
2. Añade una nueva línea con el formato: `base,past,past_participle,type`
3. Guarda el archivo
4. Reinicia la aplicación

**Ejemplo:**
```csv
swim,swam,swum,irregular
dance,danced,danced,regular
```

---

## 🗺️ Roadmap

### ✅ Versión 1.0 (Completado)
- [x] Sistema de quiz interactivo
- [x] Diccionario de verbos
- [x] Sistema de puntuación
- [x] Estadísticas básicas
- [x] Diseño responsivo

### ✅ Versión 2.0 (Actual)
- [x] Sistema de rachas y bonificaciones
- [x] Rangos de jugador
- [x] Registro de errores
- [x] Tiempo de estudio
- [x] Diseño mejorado con CSS

### 🚧 Versión 3.0 (En Planificación)
- [ ] Sistema de usuarios con login
- [ ] Guardar progreso en la nube
- [ ] Modo multijugador (competición)
- [ ] Gráficos de progreso histórico
- [ ] Exportar estadísticas a PDF
- [ ] Modo de práctica oral (pronunciación)
- [ ] Integración con API de traducción
- [ ] Aplicación móvil nativa

### 💡 Ideas Futuras
- [ ] Ejercicios de listening
- [ ] Conjugación de tiempos verbales
- [ ] Phrasal verbs
- [ ] Mini juegos adicionales
- [ ] Sistema de logros y badges
- [ ] Modo offline
- [ ] Soporte para más idiomas

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Este proyecto es de código abierto y cualquier ayuda es apreciada.

### Cómo Contribuir

1. **Fork el proyecto**
```bash
   # Click en el botón "Fork" en GitHub
```

2. **Clona tu fork**
```bash
   git clone https://github.com/TU_USUARIO/english-verb-master.git
```

3. **Crea una rama para tu feature**
```bash
   git checkout -b feature/NuevaFuncionalidad
```

4. **Haz tus cambios y commit**
```bash
   git add .
   git commit -m "Add: Nueva funcionalidad increíble"
```

5. **Push a tu fork**
```bash
   git push origin feature/NuevaFuncionalidad
```

6. **Abre un Pull Request**
   - Ve a tu fork en GitHub
   - Click en "New Pull Request"
   - Describe tus cambios detalladamente

### Guía de Estilo

- Usa **nombres descriptivos** para variables y funciones
- Comenta código complejo
- Sigue **PEP 8** para Python
- Agrega **docstrings** a funciones
- Mantén funciones **pequeñas y específicas**

### Reportar Bugs

Si encuentras un error, por favor [abre un issue](https://github.com/EdwinV08/english-verb-master/issues) con:

- 🐛 Descripción clara del bug
- 📝 Pasos para reproducirlo
- 💻 Tu sistema operativo y versión de Python
- 📸 Capturas de pantalla (si aplica)

---



Copyright (c) 2026 Edwin Villa Sánchez

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
de este software y archivos de documentación asociados (el "Software"), para usar
el Software sin restricciones...
```

---

## 📞 Contacto


**Enlace del Proyecto:** https://github.com/Edwinv08/english-verb-master




---

## 🙏 Agradecimientos

Este proyecto no sería posible sin:

- **[Streamlit](https://streamlit.io/)** - Por su increíble framework
- **[Pandas](https://pandas.pydata.org/)** - Por facilitar el manejo de datos
- **Comunidad de Python** - Por las herramientas open source
- **Estudiantes de inglés** - Por el feedback y sugerencias
- **Profesores de inglés** - Por validar el contenido educativo

### Recursos Útiles

- [Documentación de Streamlit](https://docs.streamlit.io/)
- [Guía de Verbos Irregulares](https://www.englishpage.com/irregularverbs/irregularverbs.html)
- [PEP 8 Style Guide](https://pep8.org/)
- [Markdown Guide](https://www.markdownguide.org/)

---

## ⭐ Star History

Si este proyecto te ayudó, considera darle una estrella ⭐ en GitHub!

[![Star History Chart](https://api.star-history.com/svg?repos=EdwinV08/english-verb-master&type=Date)](https://star-history.com/#TU_USUARIO/english-verb-master&Date)

---

<div align="center">

**Hecho con ❤️ y ☕ por Edwin Villa**

Si este proyecto te fue útil, ¡compártelo con otros estudiantes de inglés!

[⬆️ Volver arriba](#-english-verb-master-pro)

</div>

---

> 💡 **Tip:** ¿Tienes ideas para mejorar esta app? ¡Abre un issue o contribuye con código!