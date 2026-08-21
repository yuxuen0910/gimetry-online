import json

file_path = r'D:\01Personal_Projects\My_Websites_Portfolio_2\site\_next\data\NkaLovy8M3OdV54UztOF0\work\june-science.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

work = data['pageProps']['work']

print("===== Verification =====")
print(f"Title: {work['title']}")
print(f"Meta Title: {work['metaTitle']}")
print(f"Meta Description: {work['metaDescription']}")
print(f"Thumbnail Excerpt: {work['thumbnailExcerpt']}")
print(f"\nHero Section Text:")
print(work['workHeroSection']['sectionContent'][0]['children'][0]['text'])
print(f"\nServices: {work['workHeroSection']['servicesList']}")
print(f"\nWork Modules ({len(work['workModules'])}):")
for i, module in enumerate(work['workModules'], 1):
    title = module.get('title', 'N/A')
    text = module['content'][0]['children'][0]['text'][:100]
    print(f"  {i}. {title}")
    print(f"     {text}...")

print(f"\nWebsite URL: {work['workHeroSection']['websiteURL']}")
