import json

# 参考网站的内容
reference_title = "VB ZipBlind (Singapore)"
reference_meta_title = "Brand & Graphic Design for VB ZipBlind"
reference_meta_desc = "Brand and graphic design for VB ZipBlind Singapore, delivering a cleaner premium look with refined typography and structured visual direction."
reference_excerpt = "Cleaner premium look for product communication."
reference_hero_text = "VB ZipBlind wanted a cleaner premium look for product communication while keeping technical information simple for customers and installers."
reference_challenge = "The challenge was presenting practical product details without making layouts feel too heavy. We needed a visual direction that worked across sales materials, digital touchpoints, and quick campaign assets."
reference_solution = "We introduced a structured grid, clearer hierarchy, and a refined typography system. The resulting asset set improved readability and helped the brand communicate product value with a more confident identity."
reference_services = ["Brand Design", "Graphic Design", "Visual Identity"]
reference_website = "https://vbzipblindsingapore.com"

# 读取本地数据
local_path = r'D:\01Personal_Projects\My_Websites_Portfolio_2\site\_next\data\NkaLovy8M3OdV54UztOF0\work\june-science.json'
with open(local_path, 'r', encoding='utf-8') as f:
    local_data = json.load(f)

work = local_data['pageProps']['work']

print("=== Applying VB ZipBlind content (layout preserved) ===\n")

# 1. 更新基本信息
work['title'] = reference_title
work['metaTitle'] = reference_meta_title
work['metaDescription'] = reference_meta_desc
work['thumbnailExcerpt'] = reference_excerpt
work['workHeroSection']['websiteURL'] = reference_website
work['workHeroSection']['servicesList'] = reference_services

print(f"Title: {reference_title}")
print(f"Services: {reference_services}\n")

# 2. 更新hero section文字
work['workHeroSection']['sectionContent'][0]['children'][0]['text'] = reference_hero_text
print(f"Hero text: {reference_hero_text[:80]}...\n")

# 3. 更新文本模块的内容
new_texts = [reference_challenge, reference_solution]
text_index = 0

for module in work['workModules']:
    if module['_type'] == 'workTextBlock':
        old_title = module.get('title', 'N/A')
        if text_index < len(new_texts):
            for content in module['content']:
                if 'children' in content and len(content['children']) > 0:
                    content['children'][0]['text'] = new_texts[text_index]
                    print(f"Module '{old_title}' updated:")
                    print(f"  {new_texts[text_index][:100]}...")
                    print()
                    text_index += 1
    else:
        # 媒体模块保持不变
        print(f"Module ({module['_type']}) preserved")

# 4. 更新schemaMarkup
work['schemaMarkup'] = {
    "_type": "schemaMarkup",
    "jsonLd": json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": "https://www.onboxcreative.com/work/june-science/#webpage",
                "url": "https://www.onboxcreative.com/work/june-science",
                "name": f"{reference_title} — ONBOX",
                "description": reference_meta_desc,
                "isPartOf": {"@id": "https://www.onboxcreative.com/#website"},
                "breadcrumb": {
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.onboxcreative.com"},
                        {"@type": "ListItem", "position": 2, "name": "Work", "item": "https://www.onboxcreative.com/work"},
                        {"@type": "ListItem", "position": 3, "name": reference_title, "item": "https://www.onboxcreative.com/work/june-science"}
                    ]
                }
            },
            {
                "@type": "CreativeWork",
                "@id": "https://www.onboxcreative.com/work/june-science/#project",
                "name": f"{reference_title} — Brand & Graphic Design",
                "url": "https://www.onboxcreative.com/work/june-science",
                "description": reference_solution,
                "creator": {"@id": "https://www.onboxcreative.com/#organization"},
                "about": {
                    "@type": "Organization",
                    "name": "VB ZipBlind Singapore",
                    "url": reference_website,
                    "description": "A brand seeking cleaner premium look for product communication.",
                    "industry": "Design"
                },
                "keywords": ["Brand Design", "Graphic Design", "Visual Identity", "Typography", "Print Design"],
                "workExample": [
                    {"@type": "CreativeWork", "name": "Brand Design", "description": "Cleaner premium look for product communication."},
                    {"@type": "CreativeWork", "name": "Graphic Design", "description": "Structured grid and refined typography system."}
                ],
                "provider": {"@id": "https://www.onboxcreative.com/#organization"}
            }
        ]
    }, ensure_ascii=False)
}

# SEO
local_data['pageProps']['seo']['title'] = reference_meta_title
local_data['pageProps']['seo']['description'] = reference_meta_desc
local_data['pageProps']['seo']['schemaMarkup'] = work['schemaMarkup']

# 保存
with open(local_path, 'w', encoding='utf-8') as f:
    json.dump(local_data, f, ensure_ascii=False, indent=2)

print(f"\n[OK] Done! Total modules: {len(work['workModules'])}")
