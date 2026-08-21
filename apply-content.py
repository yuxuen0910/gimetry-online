import json
import urllib.request

# 1. 从原站获取原始数据
url = "https://www.onboxcreative.com/_next/data/NkaLovy8M3OdV54UztOF0/work/june-science.json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

with urllib.request.urlopen(req, timeout=10) as response:
    original_data = json.loads(response.read().decode('utf-8'))

# 2. 读取本地当前数据
local_path = r'D:\01Personal_Projects\My_Websites_Portfolio_2\site\_next\data\NkaLovy8M3OdV54UztOF0\work\june-science.json'
with open(local_path, 'r', encoding='utf-8') as f:
    local_data = json.load(f)

# 3. 从原站获取的原始work模块
original_work = original_data['pageProps']['work']
original_modules = original_work['workModules']

# 4. 本地数据
local_work = local_data['pageProps']['work']

print("=== Applying content update (layout preserved) ===\n")

# 5. 更新基本信息（从原站恢复）
local_work['title'] = original_work['title']
local_work['metaTitle'] = original_work['metaTitle']
local_work['metaDescription'] = original_work['metaDescription']
local_work['thumbnailExcerpt'] = original_work['thumbnailExcerpt']
local_work['workHeroSection']['websiteURL'] = original_work['workHeroSection']['websiteURL']
local_work['workHeroSection']['servicesList'] = original_work['workHeroSection']['servicesList']

# 6. 更新hero section内容
hero_original = original_work['workHeroSection']['sectionContent'][0]['children'][0]['text']
local_hero = local_work['workHeroSection']['sectionContent'][0]['children'][0]
local_hero['text'] = hero_original

print(f"Hero text updated: {hero_original[:80]}...")
print(f"Services: {local_work['workHeroSection']['servicesList']}")

# 7. 更新workModules中的文本内容（保持布局结构）
# 找到原站中的文本模块内容
original_text_modules = {}
for module in original_modules:
    if module['_type'] == 'workTextBlock':
        title = module.get('title', 'N/A')
        # 提取文本内容
        for content in module['content']:
            if 'children' in content and len(content['children']) > 0:
                text = content['children'][0].get('text', '')
                original_text_modules[title] = text
                break

print(f"\nText modules to update: {list(original_text_modules.keys())}")

# 更新本地workModules中的文本
for local_module in local_work['workModules']:
    if local_module['_type'] == 'workTextBlock':
        title = local_module.get('title', 'N/A')
        if title in original_text_modules:
            # 更新文本内容
            for content in local_module['content']:
                if 'children' in content and len(content['children']) > 0:
                    content['children'][0]['text'] = original_text_modules[title]
                    print(f"  Updated '{title}': {original_text_modules[title][:80]}...")
        else:
            print(f"  Title '{title}' not found in original")
    else:
        print(f"  Media module preserved: {local_module['_type']}")

# 8. 更新schemaMarkup
local_work['schemaMarkup'] = original_work['schemaMarkup']

# 9. 更新SEO
local_data['pageProps']['seo']['title'] = original_work['metaTitle']
local_data['pageProps']['seo']['description'] = original_work['metaDescription']
local_data['pageProps']['seo']['schemaMarkup'] = original_work['schemaMarkup']

# 10. 保存
with open(local_path, 'w', encoding='utf-8') as f:
    json.dump(local_data, f, ensure_ascii=False, indent=2)

print(f"\n[OK] Content updated successfully! Modules: {len(local_work['workModules'])}")
