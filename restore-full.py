import json
import urllib.request

# 从原站获取完整的原始数据
url = "https://www.onboxcreative.com/_next/data/NkaLovy8M3OdV54UztOF0/work/june-science.json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

with urllib.request.urlopen(req, timeout=10) as response:
    original_data = json.loads(response.read().decode('utf-8'))

original_work = original_data['pageProps']['work']

# 读取本地数据
local_path = r'D:\01Personal_Projects\My_Websites_Portfolio_2\site\_next\data\NkaLovy8M3OdV54UztOF0\work\june-science.json'
with open(local_path, 'r', encoding='utf-8') as f:
    local_data = json.load(f)

local_work = local_data['pageProps']['work']

print("=== Restoring full layout from original site ===\n")

# 更新所有基本信息
local_work['title'] = original_work['title']
local_work['metaTitle'] = original_work['metaTitle']
local_work['metaDescription'] = original_work['metaDescription']
local_work['thumbnailExcerpt'] = original_work['thumbnailExcerpt']
local_work['workHeroSection']['websiteURL'] = original_work['workHeroSection']['websiteURL']
local_work['workHeroSection']['servicesList'] = original_work['workHeroSection']['servicesList']

# 更新hero section内容
local_work['workHeroSection']['sectionContent'][0]['children'][0]['text'] = \
    original_work['workHeroSection']['sectionContent'][0]['children'][0]['text']

# 更新schemaMarkup
local_work['schemaMarkup'] = original_work['schemaMarkup']

# SEO
local_data['pageProps']['seo']['title'] = original_work['metaTitle']
local_data['pageProps']['seo']['description'] = original_work['metaDescription']
local_data['pageProps']['seo']['schemaMarkup'] = original_work['schemaMarkup']

# 恢复完整的workModules（保留原始布局结构）
local_work['workModules'] = original_work['workModules']

print(f"Restored {len(local_work['workModules'])} work modules")
print(f"Services: {local_work['workHeroSection']['servicesList']}")

# 显示每个模块的类型和标题
for i, module in enumerate(local_work['workModules'], 1):
    mtype = module['_type']
    title = module.get('title', 'N/A')
    print(f"  [{i}] {title} ({mtype})")

# 保存
with open(local_path, 'w', encoding='utf-8') as f:
    json.dump(local_data, f, ensure_ascii=False, indent=2)

print("\n[OK] Full layout restored!")
