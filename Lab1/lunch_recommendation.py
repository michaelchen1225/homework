import random
import sys

# 針對 Windows 控制台強化 UTF-8 編碼支援
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# 預設午餐選擇清單 (包含豐富常見選項)
DEFAULT_RESTAURANTS = [
    "排骨便當 / 雞腿便當",
    "紅燒/清燉 牛肉麵",
    "滷肉飯 + 水煮蛋 / 貢丸湯",
    "日式拉麵",
    "麥當勞 / 速食套餐",
    "義大利麵 / 燉飯",
    "小火鍋 / 臭臭鍋",
    "手工水餃 / 煎餃",
    "日式咖哩飯",
    "平價鐵板燒",
    "韓式炸雞 / 韓式豆腐鍋",
    "日式丼飯 (豬肉丼/牛肉丼)",
    "Subway / 健康潛艇堡",
    "泰式打拋豬肉飯",
    "美式早午餐 / 漢堡",
    "摩斯漢堡",
    "麻辣燙 / 滷味",
    "健康餐盒 / 低卡便當",
]

def get_recommendations(restaurants, count=5):
    """從餐廳清單中隨機精選指定數量的推薦」"""
    actual_count = min(count, len(restaurants))
    return random.sample(restaurants, actual_count)

def main():
    print("=" * 45)
    print("      今天午餐吃什麼？隨機推薦系統      ")
    print("=" * 45)
    
    restaurants = DEFAULT_RESTAURANTS.copy()
    
    while True:
        recommendations = get_recommendations(restaurants, 5)
        
        print("\n今天為您隨機推薦的 5 間/項午餐選擇：")
        for idx, item in enumerate(recommendations, 1):
            print(f"  {idx}. {item}")
            
        print("\n" + "-" * 45)
        print("操作提示：")
        print("  [ENTER] 重新抽選 5 間")
        print("  [Q]     決定好了，結束程式")
        
        try:
            choice = input("\n請選擇 (預設 Enter 重新抽選): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n程式結束。")
            break

        if choice == 'q':
            print("\n祝您用餐愉快！美食享用時光～\n")
            break

if __name__ == "__main__":
    main()

