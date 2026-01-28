import streamlit as st
import pandas as pd
import random
import os

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="English Verb Master Pro", page_icon="🎓", layout="wide")

# --- CARGA DE DATOS (Ruta específica solicitada) ---
@st.cache_data
# --- CARGA DE DATOS (Corregida) ---
@st.cache_data
def load_data():
    path = 'data/english_verbs_dataset.csv'
    
    # Verificamos si la carpeta y el archivo existen
    if not os.path.exists(path):
        st.error(f"🚨 Error: No se encontró el archivo en la ruta: {path}")
        st.info("Asegúrate de que la carpeta se llame 'data' y el archivo 'english_verbs_dataset.csv'")
        return pd.DataFrame()
    
    try:
        df = pd.read_csv(path)
        
        # CORRECCIÓN DEL ERROR: Normalizamos nombres de columnas usando lista de comprensión
        df.columns = [c.strip().lower() for c in df.columns]
        
        # Limpieza de los datos internos
        df = df.replace('stoped', 'stopped')
        
        # Aseguramos que todo sea string y sin espacios en blanco
        for col in df.columns:
            df[col] = df[col].astype(str).str.strip()
            
        return df
    except Exception as e:
        st.error(f"Error al leer el CSV: {e}")
        return pd.DataFrame()

df_master = load_data()

# --- DICCIONARIO DE TRADUCCIONES Y EJEMPLOS (Fallback) ---
# Esto asegura que siempre haya contenido aunque el CSV sea básico
HELPERS = {
    "be": {"t": "ser o estar", "e": "I want to **be** your friend."},
    "go": {"t": "ir", "e": "I **go** to the gym every day."},
    "eat": {"t": "comer", "e": "They **eat** dinner at 7 PM."},
    "write": {"t": "escribir", "e": "She **wrote** a beautiful poem."},
    "study": {"t": "estudiar", "e": "We **study** English together."},
    # El sistema generará ejemplos automáticos para los demás
}

# --- LÓGICA DE ESTADO (STATE MACHINE) ---
if 'score' not in st.session_state: st.session_state.score = 0
if 'current_verb' not in st.session_state: st.session_state.current_verb = None
if 'answered' not in st.session_state: st.session_state.answered = False
if 'options' not in st.session_state: st.session_state.options = {}

# --- FUNCIONES DEL JUEGO ---
def get_smart_distractors(correct_val, column, verb_base):
    all_vals = list(df_master[column].unique())
    # Filtrar para obtener distractores que no sean la respuesta correcta
    distractors = [v for v in all_vals if v.lower() != correct_val.lower()]
    
    # Buscar similares (que empiecen con la misma letra)
    similar = [v for v in distractors if v.lower().startswith(verb_base[0].lower())]
    
    if len(similar) >= 2:
        sampled = random.sample(similar, 2)
    else:
        sampled = random.sample(distractors, 2)
        
    final_options = list(set(sampled + [correct_val]))
    # Asegurar siempre 4 opciones
    while len(final_options) < 4:
        extra = random.choice(distractors)
        if extra not in final_options: final_options.append(extra)
        
    random.shuffle(final_options)
    return final_options

def pick_new_verb(filter_type):
    if df_master.empty: return
    
    df_f = df_master if filter_type == "Mixto" else df_master[df_master['type'] == filter_type.lower()]
    verb = df_f.sample(1).iloc[0]
    
    st.session_state.current_verb = verb
    st.session_state.options = {
        'past': get_smart_distractors(verb['past'], 'past', verb['base']),
        'participle': get_smart_distractors(verb['past_participle'], 'past_participle', verb['base'])
    }
    st.session_state.answered = False

# --- INTERFAZ DE USUARIO ---
st.title("🎓 English Verb Master Pro")

if df_master.empty:
    st.warning("Carga el dataset en la carpeta 'data/' para comenzar.")
else:
    tab_game, tab_search = st.tabs(["🎮 Entrenador Interactivo", "🔍 Buscador de Verbos"])

    # --- PESTAÑA 1: EL JUEGO ---
    with tab_game:
        st.sidebar.header("Configuración")
        mode = st.sidebar.selectbox("Tipo de verbos:", ["Mixto", "Regular", "Irregular"])
        
        if st.session_state.current_verb is None:
            pick_new_verb(mode)

        v = st.session_state.current_verb
        
        # Dashboard
        c_score, c_type = st.columns([1, 4])
        c_score.metric("Puntos", st.session_state.score)
        
        # Card del Verbo
        st.markdown(f"""
            <div style="background-color:#1E1E1E; color:white; padding:30px; border-radius:15px; text-align:center;">
                <h1 style="color:#4CAF50; font-size:50px; margin:0;">{v['base'].upper()}</h1>
                <p style="font-size:1.2rem; opacity:0.8;">Tipo: {v['type'].capitalize()}</p>
            </div>
        """, unsafe_allow_html=True)

        st.write("### Selecciona las formas correctas:")
        
        col1, col2 = st.columns(2)
        with col1:
            choice_past = st.radio("Past Simple:", st.session_state.options['past'], disabled=st.session_state.answered)
        with col2:
            choice_participle = st.radio("Past Participle:", st.session_state.options['participle'], disabled=st.session_state.answered)

        if not st.session_state.answered:
            if st.button("VERIFICAR", use_container_width=True, type="primary"):
                # Validación flexible (soporta was/were)
                is_past_ok = choice_past.lower() in [x.strip().lower() for x in v['past'].split('/')]
                is_pp_ok = choice_participle.lower() in [x.strip().lower() for x in v['past_participle'].split('/')]
                
                if is_past_ok and is_pp_ok:
                    st.session_state.score += 15
                    st.success("¡Excelente! Dominas este verbo. +15 puntos.")
                    st.balloons()
                else:
                    st.error(f"¡Casi! La respuesta correcta era: {v['past']} | {v['past_participle']}")
                    st.session_state.score = max(0, st.session_state.score - 5)
                
                st.session_state.answered = True
                st.rerun()
        else:
            if st.button("SIGUIENTE VERBO ➡️", use_container_width=True):
                pick_new_verb(mode)
                st.rerun()

    # --- PESTAÑA 2: BUSCADOR ---
    with tab_search:
        st.header("🔎 Diccionario Completo")
        # Autocompletado con todos los verbos del dataset
        all_verbs = sorted(df_master['base'].tolist())
        selected_search = st.selectbox("Busca un verbo para ver sus detalles:", [""] + all_verbs)

        if selected_search:
            v_data = df_master[df_master['base'] == selected_search].iloc[0]
            
            st.markdown(f"## Verbo: {selected_search.upper()}")
            
            res1, res2, res3 = st.columns(3)
            res1.info(f"**Past Simple**\n### {v_data['past']}")
            res2.info(f"**Past Participle**\n### {v_data['past_participle']}")
            res3.info(f"**Tipo**\n### {v_data['type'].capitalize()}")
            
            # Traducción y Ejemplo
            st.divider()
            info = HELPERS.get(selected_search, {"t": "Consultar diccionario", "e": f"I need to {v_data['base']} today. Yesterday I {v_data['past']}."})
            
            col_t, col_e = st.columns(2)
            with col_t:
                st.write("### 🌎 Traducción sugerida:")
                st.write(info['t'])
            with col_e:
                st.write("### 💡 Ejemplo de uso:")
                st.info(info['e'])

# --- FOOTER ---
st.sidebar.markdown("---")
if st.sidebar.button("Reiniciar Aplicación"):
    st.session_state.clear()
    st.rerun()