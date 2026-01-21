import streamlit as st
import random

# --- 1. 設定網頁標題 ---
st.title("🍱 香港食咩好？決定器")
st.write("解決你的午餐/晚餐選擇困難症")

# --- 2. 餐廳資料庫 ---
# 這裡建議未來可以升級成讀取 Excel 或 Google Sheets
restaurants = [
    {"name": "九記牛腩", "district": "中環", "cuisine": "港式", "price": "平", "type": "午餐"},
    {"name": "Sushi Sase", "district": "中環", "cuisine": "日本菜", "price": "貴", "type": "晚餐"},
    {"name": "Samsen", "district": "灣仔", "cuisine": "泰國菜", "price": "中", "type": "晚餐"},
    {"name": "華星冰室", "district": "灣仔", "cuisine": "港式", "price": "平", "type": "午餐"},
    {"name": "Yardbird", "district": "上環", "cuisine": "日本菜", "price": "中", "type": "晚餐"},
    {"name": "麥當勞", "district": "全港", "cuisine": "快餐", "price": "平", "type": "午餐"},
    {"name": "Chiptole (假設)", "district": "中環", "cuisine": "西式", "price": "中", "type": "午餐"}
]

# --- 3. 側邊欄：使用者輸入選項 ---
st.sidebar.header("🔎 篩選條件")

# 使用 selectbox 製作下拉選單，讓介面更乾淨
target_district = st.sidebar.selectbox("地區", ["中環", "灣仔", "上環", "全港"])
target_cuisine = st.sidebar.selectbox("菜式", ["港式", "日本菜", "泰國菜", "快餐", "西式"])
target_price = st.sidebar.select_slider("預算", options=["平", "中", "貴"])

# --- 4. 主按鈕與邏輯 ---
if st.button("🎲 幫我隨機揀一間！"):
    
    # 篩選邏輯
    candidates = [
        r for r in restaurants 
        if (r["district"] == target_district or r["district"] == "全港" or target_district == "全港")
        and (r["cuisine"] == target_cuisine)
        and (r["price"] == target_price)
    ]
    
    # 顯示結果
    if not candidates:
        st.error("😔 搵唔到餐廳！試下轉變篩選條件？")
    else:
        choice = random.choice(candidates)
        st.success(f"🎉 系統推介：**{choice['name']}**")
        st.info(f"📍 地區：{choice['district']} | 💰 價位：{choice['price']}")
        
        # 額外功能：模擬 Google Maps Link
        map_url = f"https://www.google.com/maps/search/?api=1&query={choice['name']}+{choice['district']}"
        st.markdown(f"[🗺️ 喺 Google Maps 打開]({map_url})")
