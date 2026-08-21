import json
import os

# 读取原始文件
file_path = r'D:\01Personal_Projects\My_Websites_Portfolio_2\site\_next\data\NkaLovy8M3OdV54UztOF0\work\june-science.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

work = data['pageProps']['work']

# 新的内容（来自参考网站 VB ZipBlind Singapore）
new_title = "VB ZipBlind (Singapore)"
new_meta_title = "Brand & Graphic Design for VB ZipBlind"
new_meta_description = "Brand and graphic design for VB ZipBlind Singapore, delivering a cleaner premium look with refined typography and structured visual direction."
new_thumbnail_excerpt = "Cleaner premium look for product communication."
new_website_url = "https://vbzipblindsingapore.com"  # 假设的URL，可根据实际情况修改

# 更新基本字段
work['title'] = new_title
work['metaTitle'] = new_meta_title
work['metaDescription'] = new_meta_description
work['thumbnailExcerpt'] = new_thumbnail_excerpt
work['workHeroSection']['websiteURL'] = new_website_url

# 更新hero section的内容
hero_content = work['workHeroSection']['sectionContent'][0]
hero_content['children'][0]['text'] = "VB ZipBlind wanted a cleaner premium look for product communication while keeping technical information simple for customers and installers."

# 更新servicesList
work['workHeroSection']['servicesList'] = ["Brand Design", "Graphic Design", "Visual Identity"]

# 构建新的workModules（挑战/方案部分）
new_work_modules = [
    {
        "_key": "challenge-section",
        "_type": "workTextBlock",
        "content": [
            {
                "_key": "challenge-content",
                "_type": "block",
                "children": [
                    {
                        "_key": "challenge-text",
                        "_type": "span",
                        "marks": [],
                        "text": "The challenge was presenting practical product details without making layouts feel too heavy. We needed a visual direction that worked across sales materials, digital touchpoints, and quick campaign assets."
                    }
                ],
                "markDefs": [],
                "style": "normal"
            }
        ],
        "title": "The Challenge"
    },
    {
        "_key": "solution-section",
        "_type": "workTextBlock",
        "content": [
            {
                "_key": "solution-content",
                "_type": "block",
                "children": [
                    {
                        "_key": "solution-text",
                        "_type": "span",
                        "marks": [],
                        "text": "We introduced a structured grid, clearer hierarchy, and a refined typography system. The resulting asset set improved readability and helped the brand communicate product value with a more confident identity."
                    }
                ],
                "markDefs": [],
                "style": "normal"
            }
        ],
        "title": "The Solution"
    }
]
work['workModules'] = new_work_modules

# 构建新的schemaMarkup
new_schema_markup = {
    "_type": "schemaMarkup",
    "jsonLd": json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebPage",
                "@id": "https://www.onboxcreative.com/work/june-science/#webpage",
                "url": "https://www.onboxcreative.com/work/june-science",
                "name": "VB ZipBlind (Singapore) — ONBOX",
                "description": "Brand and graphic design for VB ZipBlind Singapore, delivering a cleaner premium look with refined typography and structured visual direction.",
                "isPartOf": {
                    "@id": "https://www.onboxcreative.com/#website"
                },
                "breadcrumb": {
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {
                            "@type": "ListItem",
                            "position": 1,
                            "name": "Home",
                            "item": "https://www.onboxcreative.com"
                        },
                        {
                            "@type": "ListItem",
                            "position": 2,
                            "name": "Work",
                            "item": "https://www.onboxcreative.com/work"
                        },
                        {
                            "@type": "ListItem",
                            "position": 3,
                            "name": "VB ZipBlind (Singapore)",
                            "item": "https://www.onboxcreative.com/work/june-science"
                        }
                    ]
                }
            },
            {
                "@type": "CreativeWork",
                "@id": "https://www.onboxcreative.com/work/june-science/#project",
                "name": "VB ZipBlind (Singapore) — Brand & Graphic Design",
                "url": "https://www.onboxcreative.com/work/june-science",
                "description": "Brand and graphic design for VB ZipBlind Singapore. We introduced a structured grid, clearer hierarchy, and a refined typography system to help the brand communicate product value with a more confident identity.",
                "creator": {
                    "@id": "https://www.onboxcreative.com/#organization"
                },
                "about": {
                    "@type": "Organization",
                    "name": "VB ZipBlind Singapore",
                    "url": new_website_url,
                    "description": "A brand seeking cleaner premium look for product communication.",
                    "industry": "Design"
                },
                "keywords": [
                    "Brand Design",
                    "Graphic Design",
                    "Visual Identity",
                    "Typography",
                    "Print Design"
                ],
                "workExample": [
                    {
                        "@type": "CreativeWork",
                        "name": "Brand Design",
                        "description": "Cleaner premium look for product communication while keeping technical information simple."
                    },
                    {
                        "@type": "CreativeWork",
                        "name": "Graphic Design",
                        "description": "Structured grid, clearer hierarchy, and refined typography system."
                    }
                ],
                "provider": {
                    "@id": "https://www.onboxcreative.com/#organization"
                }
            }
        ]
    }, ensure_ascii=False)
}
work['schemaMarkup'] = new_schema_markup

# SEO更新
data['pageProps']['seo']['title'] = new_meta_title
data['pageProps']['seo']['description'] = new_meta_description
data['pageProps']['seo']['schemaMarkup'] = new_schema_markup

# 写入更新后的文件
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("[OK] june-science.json updated successfully!")
print(f"Title updated to: {new_title}")
print(f"Meta title: {new_meta_title}")
print(f"Services: {work['workHeroSection']['servicesList']}")
print(f"Modules count: {len(work['workModules'])}")
