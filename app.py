import streamlit as st
import pandas as pd
import random
import os
from datetime import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="English Verb Master Pro", 
    page_icon="🎓", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS PERSONALIZADO ---
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #4CAF50;
        font-size: 3.5em;
        font-weight: bold;
        margin-bottom: 0.3em;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.3em;
        margin-bottom: 2em;
    }
    .verb-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin: 20px 0;
    }
    .verb-title {
        font-size: 4em;
        font-weight: bold;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 3px;
    }
    .verb-type {
        font-size: 1.5em;
        opacity: 0.9;
        margin-top: 10px;
    }
    .streak-badge {
        background: linear-gradient(45deg, #FF6B6B, #FFE66D);
        color: #000;
        padding: 10px 20px;
        border-radius: 25px;
        font-size: 1.2em;
        font-weight: bold;
        display: inline-block;
        margin: 10px 0;
    }
    .result-correct {
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .result-incorrect {
        background-color: #f8d7da;
        border-left: 5px solid #dc3545;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- CARGA DE DATOS ---
@st.cache_data
def load_data():
    path = 'data/english_verbs_dataset.csv'
    if not os.path.exists(path):
        st.error(f"🚨 Error: No se encontró el archivo en la ruta: {path}")
        return pd.DataFrame()
    try:
        df = pd.read_csv(path)
        df.columns = [c.strip().lower() for c in df.columns]
        df = df.replace('stoped', 'stopped')
        for col in df.columns:
            df[col] = df[col].astype(str).str.strip()
        return df
    except Exception as e:
        st.error(f"❌ Error al leer el CSV: {e}")
        return pd.DataFrame()

df_master = load_data()

# --- DICCIONARIO DE TRADUCCIONES Y EJEMPLOS ---
HELPERS = {
    "be": {"t": "ser o estar", "e": "I want to **be** your friend."},
    "become": {"t": "convertirse", "e": "She **became** a doctor last year."},
    "begin": {"t": "comenzar", "e": "Let's **begin** the meeting now."},
    "break": {"t": "romper", "e": "Don't **break** the glass!"},
    "bring": {"t": "traer", "e": "Please **bring** your notebook."},
    "build": {"t": "construir", "e": "They **built** a new house."},
    "buy": {"t": "comprar", "e": "I **bought** a new phone yesterday."},
    "catch": {"t": "atrapar", "e": "Can you **catch** the ball?"},
    "choose": {"t": "elegir", "e": "I **chose** the blue one."},
    "come": {"t": "venir", "e": "**Come** here, please!"},
    "cost": {"t": "costar", "e": "How much does it **cost**?"},
    "cut": {"t": "cortar", "e": "Be careful when you **cut** the paper."},
    "do": {"t": "hacer", "e": "What do you **do** for work?"},
    "draw": {"t": "dibujar", "e": "She **draws** beautifully."},
    "drink": {"t": "beber", "e": "I **drink** coffee every morning."},
    "drive": {"t": "conducir", "e": "He **drives** to work."},
    "eat": {"t": "comer", "e": "They **eat** dinner at 7 PM."},
    "fall": {"t": "caer", "e": "Be careful not to **fall**!"},
    "feel": {"t": "sentir", "e": "I **feel** great today!"},
    "find": {"t": "encontrar", "e": "Did you **find** your keys?"},
    "fly": {"t": "volar", "e": "Birds **fly** south in winter."},
    "forget": {"t": "olvidar", "e": "Don't **forget** your homework!"},
    "get": {"t": "obtener/conseguir", "e": "I **got** a new job!"},
    "give": {"t": "dar", "e": "Please **give** me that book."},
    "go": {"t": "ir", "e": "I **go** to the gym every day."},
    "grow": {"t": "crecer", "e": "Plants **grow** in spring."},
    "have": {"t": "tener", "e": "I **have** two brothers."},
    "hear": {"t": "oír/escuchar", "e": "Did you **hear** that noise?"},
    "keep": {"t": "mantener/guardar", "e": "**Keep** the change!"},
    "know": {"t": "saber/conocer", "e": "I **know** the answer."},
    "leave": {"t": "salir/dejar", "e": "What time do you **leave**?"},
    "let": {"t": "dejar/permitir", "e": "**Let** me help you."},
    "lose": {"t": "perder", "e": "Don't **lose** your ticket!"},
    "make": {"t": "hacer/fabricar", "e": "She **makes** delicious cakes."},
    "meet": {"t": "conocer/encontrarse", "e": "Nice to **meet** you!"},
    "pay": {"t": "pagar", "e": "I'll **pay** for dinner."},
    "put": {"t": "poner", "e": "**Put** it on the table."},
    "read": {"t": "leer", "e": "I **read** books every night."},
    "run": {"t": "correr", "e": "I **run** every morning."},
    "say": {"t": "decir", "e": "What did you **say**?"},
    "see": {"t": "ver", "e": "Can you **see** the stars?"},
    "sell": {"t": "vender", "e": "They **sell** fresh fruit."},
    "send": {"t": "enviar", "e": "I'll **send** you an email."},
    "sit": {"t": "sentarse", "e": "Please **sit** down."},
    "sleep": {"t": "dormir", "e": "I **sleep** 8 hours daily."},
    "speak": {"t": "hablar", "e": "She **speaks** three languages."},
    "stand": {"t": "estar de pie", "e": "Please **stand** up."},
    "take": {"t": "tomar/llevar", "e": "**Take** this medicine twice daily."},
    "teach": {"t": "enseñar", "e": "She **teaches** English."},
    "tell": {"t": "decir/contar", "e": "**Tell** me the truth."},
    "think": {"t": "pensar", "e": "I **think** it's a good idea."},
    "understand": {"t": "entender", "e": "Do you **understand** the lesson?"},
    "wear": {"t": "usar/llevar puesto", "e": "She **wears** glasses."},
    "win": {"t": "ganar", "e": "Our team **won** the championship!"},
    "write": {"t": "escribir", "e": "She **wrote** a beautiful poem."},
    "accept": {"t": "aceptar", "e": "I **accept** your apology."},
    "add": {"t": "agregar/añadir", "e": "**Add** some salt to the soup."},
    "answer": {"t": "responder", "e": "Please **answer** the phone."},
    "arrive": {"t": "llegar", "e": "What time will you **arrive**?"},
    "ask": {"t": "preguntar", "e": "Can I **ask** you a question?"},
    "believe": {"t": "creer", "e": "I **believe** in you!"},
    "call": {"t": "llamar", "e": "I'll **call** you tomorrow."},
    "clean": {"t": "limpiar", "e": "I **clean** my room every weekend."},
    "close": {"t": "cerrar", "e": "Please **close** the door."},
    "cook": {"t": "cocinar", "e": "My mom **cooks** delicious food."},
    "dance": {"t": "bailar", "e": "They **danced** all night."},
    "decide": {"t": "decidir", "e": "We need to **decide** now."},
    "deliver": {"t": "entregar", "e": "They **deliver** packages daily."},
    "develop": {"t": "desarrollar", "e": "She **developed** new skills."},
    "enjoy": {"t": "disfrutar", "e": "I **enjoy** reading books."},
    "explain": {"t": "explicar", "e": "Can you **explain** this again?"},
    "finish": {"t": "terminar", "e": "I **finished** my homework."},
    "help": {"t": "ayudar", "e": "Can you **help** me?"},
    "hope": {"t": "esperar (desear)", "e": "I **hope** you feel better."},
    "improve": {"t": "mejorar", "e": "Practice will **improve** your skills."},
    "invite": {"t": "invitar", "e": "She **invited** me to the party."},
    "join": {"t": "unirse", "e": "**Join** us for dinner!"},
    "learn": {"t": "aprender", "e": "I want to **learn** English."},
    "like": {"t": "gustar", "e": "I **like** chocolate."},
    "listen": {"t": "escuchar", "e": "**Listen** to this song!"},
    "live": {"t": "vivir", "e": "Where do you **live**?"},
    "look": {"t": "mirar", "e": "**Look** at this!"},
    "love": {"t": "amar/encantar", "e": "I **love** pizza!"},
    "need": {"t": "necesitar", "e": "I **need** your help."},
    "open": {"t": "abrir", "e": "**Open** the window, please."},
    "play": {"t": "jugar", "e": "Kids **play** in the park."},
    "rain": {"t": "llover", "e": "It **rains** a lot here."},
    "remember": {"t": "recordar", "e": "I **remember** you!"},
    "start": {"t": "comenzar", "e": "Let's **start** the class."},
    "stop": {"t": "parar/detener", "e": "**Stop** at the red light."},
    "study": {"t": "estudiar", "e": "We **study** English together."},
    "talk": {"t": "hablar", "e": "Can we **talk**?"},
    "travel": {"t": "viajar", "e": "I love to **travel**."},
    "try": {"t": "intentar", "e": "**Try** your best!"},
    "use": {"t": "usar", "e": "How do you **use** this?"},
    "visit": {"t": "visitar", "e": "We **visited** Paris last year."},
    "wait": {"t": "esperar", "e": "Please **wait** here."},
    "walk": {"t": "caminar", "e": "I **walk** to school every day."},
    "want": {"t": "querer", "e": "What do you **want** for dinner?"},
    "watch": {"t": "ver/mirar", "e": "Let's **watch** a movie."},
    "work": {"t": "trabajar", "e": "I **work** at a bank."},
}

# --- INICIALIZACIÓN DE ESTADO ---
if 'score' not in st.session_state: st.session_state.score = 0
if 'current_verb' not in st.session_state: st.session_state.current_verb = None
if 'answered' not in st.session_state: st.session_state.answered = False
if 'options' not in st.session_state: st.session_state.options = {}
if 'total_questions' not in st.session_state: st.session_state.total_questions = 0
if 'correct_answers' not in st.session_state: st.session_state.correct_answers = 0
if 'streak' not in st.session_state: st.session_state.streak = 0
if 'best_streak' not in st.session_state: st.session_state.best_streak = 0
if 'mistakes' not in st.session_state: st.session_state.mistakes = []
if 'session_start' not in st.session_state: st.session_state.session_start = datetime.now()

# --- FUNCIONES LÓGICAS ---
def get_smart_distractors(correct_val, column, verb_base):
    all_vals = list(df_master[column].unique())
    distractors = [v for v in all_vals if v.lower() != correct_val.lower()]
    similar = [v for v in distractors if v.lower().startswith(verb_base[0].lower())]
    sampled = random.sample(similar, min(2, len(similar))) if len(similar) >= 2 else random.sample(distractors, min(2, len(distractors)))
    final_options = list(set(sampled + [correct_val]))
    while len(final_options) < 4:
        extra = random.choice(distractors)
        if extra not in final_options: final_options.append(extra)
    random.shuffle(final_options)
    return final_options

def pick_new_verb(filter_type):
    df_f = df_master if filter_type == "Mixto" else df_master[df_master['type'] == filter_type.lower()]
    if df_f.empty: return
    verb = df_f.sample(1).iloc[0]
    st.session_state.current_verb = verb
    st.session_state.options = {
        'past': get_smart_distractors(verb['past'], 'past', verb['base']),
        'participle': get_smart_distractors(verb['past_participle'], 'past_participle', verb['base'])
    }
    st.session_state.answered = False

def calculate_accuracy():
    return round((st.session_state.correct_answers / st.session_state.total_questions) * 100, 1) if st.session_state.total_questions > 0 else 0

def get_rank():
    s = st.session_state.score
    if s >= 500: return "🏆 Verb Master", "#FFD700"
    if s >= 300: return "⭐ Advanced Learner", "#C0C0C0"
    if s >= 150: return "📚 Intermediate Student", "#CD7F32"
    if s >= 50: return "🌱 Beginner", "#90EE90"
    return "🥚 Newbie", "#87CEEB"

# --- UI PRINCIPAL ---
st.markdown('<p class="main-header">🎓 English Verb Master Pro</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Aprende verbos en inglés de manera divertida e interactiva</p>', unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ Configuración")
    mode = st.selectbox("Tipo de verbos:", ["Mixto", "Regular", "Irregular"])
    st.divider()
    st.header("📊 Estadísticas")
    rank, rank_color = get_rank()
    st.markdown(f"**Rango:** <span style='color:{rank_color}'>{rank}</span>", unsafe_allow_html=True)
    st.metric("Puntuación", st.session_state.score)
    if st.session_state.streak > 0:
        st.markdown(f'<div class="streak-badge">🔥 Racha: {st.session_state.streak}</div>', unsafe_allow_html=True)
    if st.button("🔄 Reiniciar Todo"):
        st.session_state.clear()
        st.rerun()

tab1, tab2, tab3 = st.tabs(["🎮 Entrenador", "🔍 Diccionario", "📈 Mi Progreso"])

# TAB 1: JUEGO
with tab1:
    if st.session_state.current_verb is None: pick_new_verb(mode)
    v = st.session_state.current_verb
    if v is not None:
        st.markdown(f'<div class="verb-card"><div class="verb-title">{v["base"]}</div><div class="verb-type">📌 {v["type"].capitalize()} Verb</div></div>', unsafe_allow_html=True)
        info = HELPERS.get(v['base'], {"t": "Consultar diccionario", "e": f"I need to **{v['base']}** today."})
        c_i1, c_i2 = st.columns(2)
        c_i1.info(f"**🌎 Traducción:** {info['t']}")
        c_i2.success(f"**💡 Ejemplo:** {info['e']}")
        
        col1, col2 = st.columns(2)
        with col1:
            choice_past = st.radio("Past Simple:", st.session_state.options['past'], disabled=st.session_state.answered)
        with col2:
            choice_participle = st.radio("Past Participle:", st.session_state.options['participle'], disabled=st.session_state.answered)
        
        if not st.session_state.answered:
            if st.button("✅ VERIFICAR", use_container_width=True, type="primary"):
                st.session_state.total_questions += 1
                is_past_ok = choice_past.lower() in [x.strip().lower() for x in v['past'].split('/')]
                is_pp_ok = choice_participle.lower() in [x.strip().lower() for x in v['past_participle'].split('/')]
                if is_past_ok and is_pp_ok:
                    st.session_state.correct_answers += 1
                    st.session_state.streak += 1
                    st.session_state.best_streak = max(st.session_state.streak, st.session_state.best_streak)
                    st.session_state.score += (15 + min(st.session_state.streak * 2, 50))
                    st.balloons()
                    st.success("¡Excelente! 🎉")
                else:
                    st.session_state.streak = 0
                    st.session_state.score = max(0, st.session_state.score - 5)
                    st.error(f"❌ Incorrecto. Era: {v['past']} | {v['past_participle']}")
                    if v['base'] not in [m['base'] for m in st.session_state.mistakes]: st.session_state.mistakes.append(dict(v))
                st.session_state.answered = True
                st.rerun()
        else:
            if st.button("➡️ SIGUIENTE VERBO", use_container_width=True, type="primary"):
                pick_new_verb(mode)
                st.rerun()

# TAB 2: DICCIONARIO
with tab2:
    st.header("📖 Diccionario")
    all_verbs = sorted(df_master['base'].tolist())
    selected_verb = st.selectbox("🔍 Busca un verbo:", [""] + all_verbs)
    if selected_verb:
        v_data = df_master[df_master['base'] == selected_verb].iloc[0]
        st.markdown(f"## Verbo: {selected_verb.upper()}")
        c1, c2, c3 = st.columns(3)
        c1.metric("Infinitive", v_data['base'])
        c2.metric("Past Simple", v_data['past'])
        c3.metric("Past Participle", v_data['past_participle'])
        v_info = HELPERS.get(selected_verb, {"t": "N/A", "e": "N/A"})
        st.write(f"**Traducción:** {v_info['t']} | **Tipo:** {v_data['type'].capitalize()}")
        st.info(f"**Ejemplo:** {v_info['e']}")
    st.divider()
    st.dataframe(df_master, use_container_width=True, hide_index=True)

# TAB 3: PROGRESO
with tab3:
    st.header("📈 Mi Progreso")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Puntos", st.session_state.score)
    c2.metric("Preguntas", st.session_state.total_questions)
    c3.metric("Precisión", f"{calculate_accuracy()}%")
    c4.metric("Mejor Racha", st.session_state.best_streak)
    
    rank, rank_color = get_rank()
    st.markdown(f"<div style='background:{rank_color}40; padding:20px; border-radius:15px; text-align:center;'><h2>Rango: {rank}</h2></div>", unsafe_allow_html=True)
    
    if st.session_state.mistakes:
        st.subheader("⚠️ Verbos para Repasar")
        st.table(pd.DataFrame(st.session_state.mistakes)[['base', 'past', 'past_participle']])

st.markdown("<div style='text-align:center; padding:20px; color:#666;'><p>English Verb Master Pro v2.0 | © 2024</p></div>", unsafe_allow_html=True)