import json

file_path = r'D:\01Personal_Projects\My_Websites_Portfolio_2\site\_next\data\NkaLovy8M3OdV54UztOF0\work.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 查看页面结构
if 'pageProps' in data:
    print("Has pageProps")
    if 'workList' in data['pageProps']:
        works = data['pageProps']['workList']
        print(f'Total works: {len(works)}')
        for w in works:
            print(f'  - {w.get("title", "N/A")}: {w.get("slug", {}).get("current", "N/A")}')
else:
    print("No pageProps, direct data")
    print(list(data.keys()))
