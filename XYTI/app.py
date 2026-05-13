import streamlit as st

# --- 1. 页面基本配置 ---
st.set_page_config(page_title="XYTI - 校园生存图鉴", page_icon="🏫")

# --- 2. 界面美化 (CSS) ---
# 注意：这里已经全部修正为 unsafe_allow_html=True
st.markdown("""
    <style>
    .stButton>button { 
        width: 100%; 
        border-radius: 12px; 
        height: 3.8em; 
        background-color: #ffffff; 
        border: 2px solid #1E1E1E; 
        color: #1E1E1E; 
        font-weight: bold; 
        margin-bottom: 10px; 
        transition: 0.3s;
    }
    .stButton>button:hover { 
        background-color: #1E1E1E; 
        color: white; 
    }
    .result-card { 
        padding: 25px; 
        border-radius: 15px; 
        border: 4px solid #1E1E1E; 
        background-color: #fff; 
        box-shadow: 12px 12px 0px #1E1E1E; 
        margin-top: 20px; 
    }
    .question-text { 
        font-size: 22px; 
        font-weight: bold; 
        margin-bottom: 25px; 
        color: #1E1E1E; 
        line-height: 1.5;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 初始化数据 (计分板) ---
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.scores = {
        "普绍波": 0, "李旭明": 0, "金冉": 0, "李春燕": 0, "代世琼": 0,
        "邓晶": 0, "李凌": 0, "侯钰淋": 0, "任帅": 0, "周于人": 0, "易子雨路": 0
    }
    st.session_state.force_result = None

# --- 4. 角色结果文库 ---
results_info = {
    "普绍波": "【成绩判官】唯分论者。擅长用班费买奖品舔优生，并在全班面前批斗退步者。评：班费买的奖品沉吗？记得别让退学女生的梦找你。",
    "李旭明": "【白裤幽默家】酷爱白牛仔裤，美其名曰老婆爱干净。实则喜欢调解气氛。评：地板没事吧？我这人挺幽默的。",
    "金冉": "【负责女神】颜值逆天且工作极其认真。评：你是所有人的缪斯，周于人的命都可以给你。",
    "李春燕": "【火眼金睛】视力堪比孙悟空，主谓宾守护者。评：藏在屁股底下的书也能被你瞬秒，拿出来！",
    "代世琼": "【阿迪硬汉】每天阿迪全套+二战褪色靴，上课氛围恐怖。评：睡着了？厕所洗脸见。作业有问题去办公室趴着做！",
    "邓晶": "【化学特朗普】长得像川普，爱讲黄段子。评：你和语文老师那段‘捉摸不透’的友谊全校熟知。",
    "李凌": "【反向押题王】声音尖锐，划的重点从来不考，爱讲家事。评：信你得高分？不存在的。",
    "侯钰淋": "【旅行博主】体育课就是你的PPT旅行展示会。评：凡尔赛文学被你玩明白了，去的地方真多啊。",
    "任帅": "【粉笔刺客】隐忍冷静，很有风度。评：那一根粉笔划出的弧线，是你最后的优雅。",
    "周于人": "【宽容受气包】迷恋金冉。评：即使被粉笔砸头、被嫁祸脚臭，心里也只有金老师布置的3a小单。",
    "易子雨路": "【代氏信徒】对代老师有种近乎宗教的崇拜。评：去办公室近距离接触代老师是你特殊的快乐。"
}

# --- 5. 游戏流程控制 ---

# A. 封面
if st.session_state.step == 0:
    st.markdown("<h1 style='text-align: center; font-size: 60px;'>XYTI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; letter-spacing: 3px;'>校园生存图鉴 · 记忆轮回</p>", unsafe_allow_html=True)
    try:
        st.image("images/cover.jpg", use_column_width=True)
    except:
        st.warning("提示：请在 images 文件夹放入 cover.jpg 以显示封面")
    
    if st.button("开启轮回"):
        st.session_state.step = 1
        st.rerun()

# B. 答题环节
elif st.session_state.step == 1:
    st.markdown("<p class='question-