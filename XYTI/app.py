import streamlit as st

# --- 1. 页面基本配置 ---
st.set_page_config(page_title="XYTI - 校园生存图鉴", page_icon="🏫")

# --- 2. 界面美化 (CSS) ---
st.markdown("""
    <style>
    .stButton>button { 
        width: 100%; border-radius: 12px; height: 3.8em; 
        background-color: #ffffff; border: 2px solid #1E1E1E; 
        color: #1E1E1E; font-weight: bold; margin-bottom: 10px; 
    }
    .stButton>button:hover { background-color: #1E1E1E; color: white; }
    .result-card { 
        padding: 25px; border-radius: 15px; border: 4px solid #1E1E1E; 
        background-color: #fff; box-shadow: 12px 12px 0px #1E1E1E; margin-top: 20px; 
    }
    .question-text { font-size: 19px; font-weight: bold; margin-bottom: 25px; color: #1E1E1E; line-height: 1.5; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. 初始化数据 ---
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.scores = {
        "普绍波": 0, "李旭明": 0, "金冉": 0, "李春燕": 0, "代世琼": 0,
        "邓晶": 0, "李凌": 0, "侯钰淋": 0, "任帅": 0, "周于人": 0, "易子雨路": 0
    }
    st.session_state.force_result = None

# 角色结果描述
results_info = {
    "普绍波": "【成绩判官】唯分论者。擅长用班费买奖品。评：奖品沉吗？记得别让退学女生的梦找你。",
    "李旭明": "【白裤幽默家】酷爱白牛仔裤，美其名曰老婆爱干净。评：地板没事吧？我这人挺幽默的。",
    "金冉": "【负责女神】颜值逆天且工作极其认真。评：你是所有人的缪斯，周于人的命都可以给你。",
    "李春燕": "【火眼金睛】视力堪比孙悟空。评：藏在屁股底下的书也能被你瞬秒，拿出来！",
    "代世琼": "【阿迪硬汉】每天阿迪全套+二战褪色靴。评：睡着了？厕所洗脸见。作业有问题去办公室趴着做！",
    "邓晶": "【化学特朗普】长得像川普，爱讲黄段子。评：你和语文老师那段‘捉摸不透’的友谊全校熟知。",
    "李凌": "【反向押题王】声音尖锐，爱讲家事。评：信你得高分？不存在的。",
    "侯钰淋": "【旅行博主】体育课就是你的PPT旅行展示会。评：凡尔赛文学被你玩明白了。",
    "任帅": "【粉笔刺客】隐忍冷静，很有风度。评：那一根粉笔划出的弧线，是你最后的优雅。",
    "周于人": "【宽容受气包】迷恋金冉。评：即使被粉笔砸头、被嫁祸脚臭，心里也只有金老师布置的3a小单。",
    "易子雨路": "【代氏信徒】对代老师有种近乎宗教的崇拜。评：去办公室近距离接触代老师是你特殊的快乐。"
}

# --- 4. 答题逻辑 ---
if st.session_state.step == 0:
    st.markdown("<h1 style='text-align: center;'>XYTI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>校园生存图鉴 · 记忆轮回</p>", unsafe_allow_html=True)
    try:
        st.image("images/cover.jpg", use_column_width=True)
    except:
        st.warning("提示：请确认 images 文件夹中有封面图 cover.jpg")
    if st.button("开启轮回"):
        st.session_state.step = 1
        st.rerun()

elif st.session_state.step == 1:
    st.markdown("<p class='question-text'>1. 普绍波又一次举行了颁奖仪式，把用班费买的昂贵奖品发给成绩优异的同学，这时你会想：</p>", unsafe_allow_html=True)
    if st.button("A. 太好了又能领奖品啦"): st.session_state.scores["普绍波"] += 1; st.session_state.step = 2; st.rerun()
    if st.button("B. 恭喜她们吧"): st.session_state.scores["任帅"] += 1; st.session_state.step = 2; st.rerun()
    if st.button("C. 与我无关"): st.session_state.step = 2; st.rerun()
    if st.button("D. 操你爹，老子鸡毛都捞不到"): st.session_state.scores["周于人"] += 1; st.session_state.step = 2; st.rerun()

elif st.session_state.step == 2:
    st.markdown("<p class='question-text'>2. 上课老师是一个看起来很和蔼可亲不会生气的老师，上课时你会：</p>", unsafe_allow_html=True)
    if st.button("A. 认真听讲"): st.session_state.step = 3; st.rerun()
    if st.button("B. 睡觉或者发呆不影响课堂"): st.session_state.step = 3; st.rerun()
    if st.button("C. 和同学一直讲话不在意老师的眼神提示直到被老师粉笔砸头"): st.session_state.scores["任帅"] += 1; st.session_state.step = 3; st.rerun()
    if st.button("D. 写金冉布置的3a小单"): st.session_state.scores["周于人"] += 1; st.session_state.step = 3; st.rerun()

elif st.session_state.step == 3:
    st.markdown("<p class='question-text'>3. 同学上课前给了你一个味道很大但下课就冷掉不能吃的零食 这时你会：</p>", unsafe_allow_html=True)
    if st.button("A. 上课之前吃掉 忘记味道一会散不掉被老师当众批斗"): st.session_state.scores["代世琼"] += 1; st.session_state.step = 4; st.rerun()
    if st.button("B. 上课时打开偷偷吃掉 被老师闻到伪装成脚臭嫁祸给男同学"): st.session_state.scores["周于人"] += 1; st.session_state.step = 4; st.rerun()
    if st.button("C. 管他冷不冷 为了课堂纪律下课再吃"): st.session_state.step = 4; st.rerun()
    if st.button("D. 下课后写个纸条“记得按时吃饭”放在普绍波的桌子上 获得普绍波的大大拥抱一个"): st.session_state.scores["普绍波"] += 1; st.session_state.step = 4; st.rerun()

elif st.session_state.step == 4:
    st.markdown("<p class='question-text'>4. 午休结束课代表突然叫你去办公室找代世琼 重做大题 这时你心里会想：</p>", unsafe_allow_html=True)
    if st.button("A. 好开心又能近距离接触代老师了"): 
        st.session_state.force_result = "易子雨路"
        st.session_state.step = 12 
        st.rerun()
    if st.button("B. 好开心又能去办公室看金冉了"): st.session_state.scores["周于人"] += 1; st.session_state.step = 5; st.rerun()
    if st.button("C. 完蛋了 昨天晚上抄猛了"): st.session_state.step = 5; st.rerun()
    if st.button("D. 完蛋了 昨天晚上空猛了"): st.session_state.step = 5; st.rerun()

elif st.session_state.step == 5:
    st.markdown("<p class='question-text'>5. 你和家人去旅游回来会分享的是：</p>", unsafe_allow_html=True)
    if st.button("A. 在各个景点拍摄的视频照片"): st.session_state.scores["侯钰淋"] += 1; st.session_state.step = 6; st.rerun()
    if st.button("B. 一路上遇到的社会现象并狠狠批斗"): st.session_state.scores["李凌"] += 1; st.session_state.step = 6; st.rerun()
    if st.button("C. 自己的美照"): st.session_state.scores["金冉"] += 1; st.session_state.step = 6; st.rerun()
    if st.button("D. 没有家人"): st.session_state.scores["代世琼"] += 1; st.session_state.step = 6; st.rerun()

elif st.session_state.step == 6:
    st.markdown("<p class='question-text'>6. 跳槽后自己的权益收到影响 你会：</p>", unsafe_allow_html=True)
    if st.button("A. 发朋友圈痛斥"): st.session_state.scores["普绍波"] += 1; st.session_state.step = 7; st.rerun()
    if st.button("B. 卖保险去了管你"): st.session_state.scores["邓晶"] += 1; st.session_state.step = 7; st.rerun()
    if st.button("C. 反思自己的错误"): st.session_state.scores["任帅"] += 1; st.session_state.step = 7; st.rerun()
    if st.button("D. 忠于星耀 不会跳槽！"): st.session_state.scores["李旭明"] += 1; st.session_state.step = 7; st.rerun()

elif st.session_state.step == 7:
    st.markdown("<p class='question-text'>7. 如果你是老师马上听写了你会去哪里排查学生作弊：</p>", unsafe_allow_html=True)
    if st.button("A. 屁股底下的书"): st.session_state.scores["李春燕"] += 1; st.session_state.step = 8; st.rerun()
    if st.button("B. 摊在腿上的书"): st.session_state.scores["普绍波"] += 1; st.session_state.step = 8; st.rerun()
    if st.button("C. 看不见 管你"): st.session_state.scores["金冉"] += 1; st.session_state.step = 8; st.rerun()
    if st.button("D. 不听写"): st.session_state.step = 8; st.rerun()

elif st.session_state.step == 8:
    st.markdown("<p class='question-text'>8. 如果你是老师课上完了会和学生分享什么：</p>", unsafe_allow_html=True)
    if st.button("A. 高铁上陌生男人不帮自己拿行李箱结果自己一脚把人家箱子踢飞的故事"): st.session_state.scores["李凌"] += 1; st.session_state.step = 9; st.rerun()
    if st.button("B. 老婆希望自己爱干净天天穿的白裤子"): st.session_state.scores["李旭明"] += 1; st.session_state.step = 9; st.rerun()
    if st.button("C. 去旅游法国专柜买的LV墨镜"): st.session_state.scores["侯钰淋"] += 1; st.session_state.step = 9; st.rerun()
    if st.button("D. 高考英语只扣作文书写分的男朋友"): st.session_state.scores["金冉"] += 1; st.session_state.step = 9; st.rerun()

elif st.session_state.step == 9:
    st.markdown("<p class='question-text'>9. 你的性取向：</p>", unsafe_allow_html=True)
    if st.button("A. 直男"): st.session_state.step = 10; st.rerun()
    if st.button("B. 直女"): st.session_state.step = 10; st.rerun()
    if st.button("C. 女同"): st.session_state.scores["周于人"] += 1; st.session_state.step = 10; st.rerun()
    if st.button("D. 男同"): st.session_state.scores["邓晶"] += 1; st.session_state.step = 10; st.rerun()

elif st.session_state.step == 10:
    st.markdown("<p class='question-text'>10. 如果快考试了你会说：</p>", unsafe_allow_html=True)
    if st.button("A. 信我者得高分"): st.session_state.scores["李凌"] += 1; st.session_state.step = 11; st.rerun()
    if st.button("B. 看我的尚方宝剑"): st.session_state.scores["李旭明"] += 1; st.session_state.step = 11; st.rerun()
    if st.button("C. 你考不好是会来怪我的"): st.session_state.scores["金冉"] += 1; st.session_state.step = 11; st.rerun()
    if st.button("D. 周贾妈妈 明天中考了她才考八十分怎么办"): st.session_state.scores["普绍波"] += 1; st.session_state.step = 11; st.rerun()

elif st.session_state.step == 11:
    st.markdown("<p class='question-text'>11. 只能留下一件你会选：</p>", unsafe_allow_html=True)
    if st.button("A. 白裤子"): st.session_state.scores["李旭明"] += 1; st.session_state.step = 12; st.rerun()
    if st.button("B. 阿迪达斯"): st.session_state.scores["代世琼"] += 1; st.session_state.step = 12; st.rerun()
    if st.button("C. 特朗普头型"): st.session_state.scores["邓晶"] += 1; st.session_state.step = 12; st.rerun()
    if st.button("D. London Boy卫衣"): st.session_state.scores["侯钰淋"] += 1; st.session_state.step = 12; st.rerun()

# --- 5. 结果显示 ---
else:
    winner = st.session_state.force_result if st.session_state.force_result else max(st.session_state.scores, key=st.session_state.scores.get)
    st.markdown(f"<div class='result-card'><h2 style='text-align: center;'>{winner}</h2>", unsafe_allow_html=True)
    try:
        st.image(f"images/{winner}.jpg", use_column_width=True)
    except:
        st.info(f"（未找到图片：images/{winner}.jpg）")
    st.markdown(f"<p style='font-size: 18px;'>{results_info[winner]}</p></div>", unsafe_allow_html=True)
    if st.button("重新开始轮回"):
        st.session_state.step = 0
        st.session_state.force_result = None
        for k in st.session_state.scores: st.session_state.scores[k] = 0
        st.rerun()