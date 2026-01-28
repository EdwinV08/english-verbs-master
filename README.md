# 🎓 English Verb Master Pro

Una aplicación interactiva y gamificada construida con **Streamlit** para dominar los verbos regulares e irregulares en inglés. Diseñada para estudiantes que buscan una forma dinámica de practicar el *Past Simple* y el *Past Participle*.

## 🚀 Características
- **🎮 Modo Entrenamiento:** Quiz interactivo con sistema de puntuación y feedback inmediato.
- **🧠 Distractores Inteligentes:** Algoritmo que genera opciones similares para desafiar tu conocimiento.
- **🔍 Diccionario Integrado:** Buscador completo de todos los verbos en el dataset con ejemplos de uso y traducciones.
- **📊 Filtros Personalizados:** Practica solo verbos regulares, irregulares o ambos.
- **📱 Interfaz Responsiva:** Optimizado para uso en computadoras y dispositivos móviles.

## 🛠️ Tecnologías Utilizadas
- **Python 3.9+**
- **Streamlit** (Framework de UI)
- **Pandas** (Manejo de datos)

## 📂 Estructura del Proyecto
```text
english-verbs-master/
├── app.py                # Lógica principal de la aplicación
├── requirements.txt      # Dependencias del proyecto
├── README.md             # Documentación
└── data/
    └── english_verbs_dataset.csv  # Base de datos de verbos

Instalación Local

1- Clonar el repositorio:
code
Bash
git clone https://github.com/TU_USUARIO/english-verbs-master.git
cd english-verbs-master

2- Crear y activar entorno virtual:
code
Bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

3- Instalar dependencias:
code
Bash
pip install -r requirements.txt

4-Ejecutar la app:
streamlit run app.py

📝 Dataset
El sistema utiliza un archivo CSV con la siguiente estructura:
base, past, past_participle, type

---

