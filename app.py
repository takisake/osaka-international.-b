import streamlit as st

# =========================
# 🔐 パスワード制限
# =========================
password = st.text_input("パスワードを入力してください", type="password")

if password != "osakainternationalib":
    st.stop()

# =========================
# 初期ページ設定
# =========================
if "page" not in st.session_state:
    st.session_state.page = "question"

# =========================
# 選択肢
# =========================
region_options = ["日本", "オーストラリア", "ヨーロッパ", "イギリス", "アメリカ", "マレーシア", "その他"]
faculty_options = ["工学部", "理学部", "データ", "国際関係学部", "経済", "経営", "商", "医", "建築", "獣医", "歯", "教育", "ファウンデーション", "その他"]
tuition_options = ["100万以内", "200万以内", "300万以内", "400万以内", "500万以内", "600万以内", "700万以内", "800万以内", "900万以内", "1000万以上"]
language_options = ["英語", "日本語"]
ranking_options = ["10位以内", "50位以内", "100位以内", "150位以内", "200位以内", "500位以内", "750位以内", "1000位以内", "1500位以内"]

# =========================
# 仮の大学データ
# =========================
universities = [
    {"name": "ブダペスト工科経済大学機械工学科タクミ", "region": "ヨーロッパ", "faculty": "工学部", "tuition": "100万以内", "language": "英語", "ranking": "500位以内"},
    {"name": "近畿大学理工学部機械工学科タクミ", "region": "日本", "faculty": "工学部", "tuition": "200万以内", "language": "日本語", "ranking": "1500位以内"},
    {"name": "大阪公立大学現代システム科学域タクミ", "region": "日本", "faculty": "データ", "tuition": "100万以内", "language": "日本語", "ranking": "1500位以内"},
    {"name": "セーチェニ大学自動車工学部タクミ", "region": "ヨーロッパ", "faculty": "工学部", "tuition": "100万以内", "language": "英語", "ranking": "1500位以内"},
    {"name": "マーストリヒト大学CSタクミ", "region": "ヨーロッパ", "faculty": "データ", "tuition": "300万以内", "language": "英語", "ranking": "500位以内"},
    {"name": "カルロス3世大学ファウンデーションタクミ", "region": "ヨーロッパ", "faculty": "ファウンデーション", "tuition": "300万以内", "language": "英語", "ranking": "50位以内"},
]

# =========================
# 🟢 質問ページ
# =========================
if st.session_state.page == "question":

    st.title("大学マッチングシステム")
    st.write("重要度は 5 が絶対重要、1 がいらないです。")

    region = st.selectbox("第1問 大学の地域は？", region_options)
    region_imp = st.slider("地域の重要度", 1, 5, 3)

    faculty = st.selectbox("第2問 進学したい学部は？", faculty_options)
    faculty_imp = st.slider("学部の重要度", 1, 5, 3)

    tuition = st.selectbox("第3問 学費はどれくらい？", tuition_options)
    tuition_imp = st.slider("学費の重要度", 1, 5, 3)

    language = st.selectbox("第4問 学びたい言語は？", language_options)
    language_imp = st.slider("言語の重要度", 1, 5, 3)

    ranking = st.selectbox("第5問 世界ランキングは？", ranking_options)
    ranking_imp = st.slider("ランキングの重要度", 1, 5, 3)

    if st.button("診断する"):
        # 入力を保存
        st.session_state.answers = {
            "region": (region, region_imp),
            "faculty": (faculty, faculty_imp),
            "tuition": (tuition, tuition_imp),
            "language": (language, language_imp),
            "ranking": (ranking, ranking_imp),
        }

        st.session_state.page = "result"
        st.rerun()

# =========================
# 🔵 結果ページ
# =========================
if st.session_state.page == "result":

    st.title("診断結果")

    answers = st.session_state.answers
    results = []

    for uni in universities:
        score = 0

        if uni["region"] == answers["region"][0]:
            score += answers["region"][1]
        if uni["faculty"] == answers["faculty"][0]:
            score += answers["faculty"][1]
        if uni["tuition"] == answers["tuition"][0]:
            score += answers["tuition"][1]
        if uni["language"] == answers["language"][0]:
            score += answers["language"][1]
        if uni["ranking"] == answers["ranking"][0]:
            score += answers["ranking"][1]

        results.append((uni["name"], score))

    results.sort(key=lambda x: x[1], reverse=True)

    st.subheader("おすすめランキング")

    for name, score in results:
        st.write(f"{name} ： スコア {score}")

    if st.button("もう一度診断する"):
        st.session_state.page = "question"
        st.rerun()
