import streamlit as st

# --- 页面设置 ---
st.set_page_config(page_title="校园生存图鉴", page_icon="🏫", layout="centered")

# --- 样式美化 ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #f0f2f6; border: 2px solid #333; color: #333; font-weight: bold; }
    .stButton>button:hover { background-color: #333; color: white; }
    .result-card { padding: 20px; border-radius: 15px; border: 3px solid #333; background-color: #fff; box-shadow: 10px 10px 0px #333; }
    </style>
    """, unsafe_allow_view_resolve=True)

# --- 初始化数据 ---
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.scores = {
        "普绍波": 0, "李旭明": 0, "金冉": 0, "李春燕": 0, "代世琼": 0,
        "邓晶": 0, "李凌": 0, "侯钰淋": 0, "任帅": 0, "周于人": 0, "易子雨路": 0
    }
    st.session_state.force_result = None

# --- 角色文案库 ---
results_info = {
    "普绍波": "【成绩判官】唯分论者，擅长用班费买奖品舔优生，并在全班面前批斗退步者。评价：奖品沉吗？记得别让退学女生的梦找你。",
    "李旭明": "【白裤幽默家】酷爱白牛仔裤，美其名曰老婆爱干净，实则喜欢调解气氛。评价：地板没事吧？",
    "金冉": "【负责女神】颜值逆天且工作极其认真。评价：你是所有人的缪斯，周于人的命都可以给你。",
    "李春燕": "【火眼金睛】视力堪比孙悟空，主谓宾守护者。评价：藏在屁股底下的书也能被你瞬秒。",
    "代世琼": "【阿迪硬汉】每天阿迪全套+二战褪色靴，物理压迫感拉满。评价：睡着了？厕所洗脸见。",
    "邓晶": "【化学特朗普】长得像川普，爱讲黄段子。评价：你和语文老师的友谊真是扑朔迷离。",
    "李凌": "【反向押题王】声音尖锐，划的重点从来不考，爱讲家事。评价：信你得高分？不存在的。",
    "侯钰淋": "【旅行博主】体育课就是你的PPT旅行展示会。评价：凡尔赛文学被你玩明白了。",
    "任帅": "【粉笔刺客】隐忍冷静，很有风度。评价：那一根粉笔划出的弧线，是你最后的优雅。",
    "周于人": "【迷弟受气包】宽容大量，极度迷恋金冉。评价：即使被粉笔砸头，心里也只有3a小单。",
    "易子雨路": "【代氏信徒】对物理和代老师有种近乎宗教的崇拜。评价：去办公室重做题是你特殊的快乐。"
}

# --- 题目数据 ---
quiz_data = [
    {"q": "1. 普绍波发班费买的昂贵奖品给优生，你会想：", "opts": [("A. 太好了又能领奖品啦", {"普绍波": 1}), ("B. 恭喜她们吧", {"任帅": 1}), ("C. 与我无关", {}), ("D. 操你爹，老子鸡毛都捞不到", {"周于人": 1})]},
    {"q": "2. 面对和蔼的老师，你会：", "opts": [("A. 认真听讲", {}), ("B. 睡觉发呆", {}), ("C. 一直讲话直到被粉笔砸头", {"任帅": 1}), ("D. 写金冉布置的3a小单", {"周于人": 1})]},
    {"q": "3. 面对上课前味道很大的冷零食：", "opts": [("A. 课前吃掉被批斗", {"代世琼": 1}), ("B. 偷吃并嫁祸给男同学脚臭", {"周于人": 1}), ("C. 下课再吃", {}), ("D. 给普绍波留纸条骗抱抱", {"普绍波": 1})]},
    {"q": "4. 课代表叫你去办公室找代世琼重做大题，你：", "opts": [("A. 好开心又能近距离接触代老师了", "FORCE_易子雨路"), ("B. 好开心又能看金冉了", {"周于人": 1}), ("C. 完蛋了抄猛了", {}), ("D. 完蛋了空猛了", {})]},
    {"q": "5. 旅游回来你会分享：", "opts": [("A. 景点照片视频", {"侯钰淋": 1}), ("B. 狠狠批斗社会现象", {"李凌": 1}), ("C. 自己的美照", {"金冉": 1}), ("D. 没有家人", {"代世琼": 1})]},
    {"q": "6. 权益受损跳槽后你会：", "opts": [("A. 发朋友圈痛斥", {"普绍波": 1}), ("B. 卖保险去了", {"邓晶": 1}), ("C. 反思错误", {"任帅": 1}), ("D. 忠于星耀不跳槽", {"李旭明": 1})]},
    {"q": "7. 作为老师，听写时你去哪排查作弊？", "opts": [("A. 屁股底下的书", {"李春燕": 1}), ("B. 摊在腿上的书", {"普绍波": 1}), ("C. 看不见管你", {"金冉": 1}), ("D. 不听写", {})]},
    {"q": "8. 下课了你会跟学生分享：", "opts": [("A. 踢飞不帮拿行李男人的箱子", {"李凌": 1}), ("B. 老婆爱干净让我穿白裤子", {"李旭明": 1}), ("C. 法国专柜买的LV墨镜", {"侯钰淋": 1}), ("D. 英语只扣作文分的男朋友", {"金冉": 1})]},
    {"q": "9. 你的性取向是？", "opts": [("A. 直男", {}), ("B. 直女", {}), ("C. 女同", {"周于人": 1}), ("D. 男同", {"邓晶": 1})]},
    {"q": "10. 快考试了你会说：", "opts": [("A. 信我者得高分", {"李凌": 1}), ("B. 看我的尚方宝剑", {"李旭明": 1}), ("C. 你考不好是会来怪我的", {"金冉": 1}), ("D. 某同学明天中考才考80怎么办", {"普绍波": 1})]},
    {"q": "11. 只能留下一件你会选：", "opts": [("A. 白裤子", {"李旭明": 1}), ("B. 阿迪达斯", {"代世琼": 1}), ("C. 特朗普头型", {"邓晶": 1}), ("D. London Boy卫衣", {"侯钰淋": 1})]},
]

# --- 游戏流程 ---
if st.session_state.step == 0:
    st.title("🏫 校园生存图鉴：你是哪位风云人物？")
    st.write("有些回忆，是阿迪达斯的套装，也是屁股底下的英语书。")
    if st.button("开启轮回"):
        st.session_state.step = 1
        st.rerun()

elif 1 <= st.session_state.step <= len(quiz_data):
    idx = st.session_state.step - 1
    data = quiz_data[idx]
    st.subheader(data["q"])
    
    for opt_text, effect in data["opts"]:
        if st.button(opt_text):
            # 处理逻辑
            if effect == "FORCE_易子雨路":
                st.session_state.force_result = "易子雨路"
                st.session_state.step = 999
            else:
                for role, score in effect.items():
                    st.session_state.scores[role] += score
                st.session_state.step += 1
            st.rerun()

else:
    # 结算页面
    st.title("📜 你的校园魂是...")
    winner = st.session_state.force_result if st.session_state.force_result else max(st.session_state.scores, key=st.session_state.scores.get)
    
    st.markdown(f"""
        <div class="result-card">
            <h2 style="color:#333;">{winner}</h2>
            <p style="font-size:1.1em;">{results_info[winner]}</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("不服，重新投胎"):
        for k in st.session_state.scores: st.session_state.scores[k] = 0
        st.session_state.step = 0
        st.session_state.force_result = None
        st.rerun()