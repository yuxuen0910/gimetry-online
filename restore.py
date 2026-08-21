import json

# 读取原始备份（从 git 或重新下载）
# 这里我们直接从当前文件读取，恢复原有结构

file_path = r'D:\01Personal_Projects\My_Websites_Portfolio_2\site\_next\data\NkaLovy8M3OdV54UztOF0\work\june-science.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

work = data['pageProps']['work']

# 恢复原始的内容文案（保留原始布局结构）
# 根据之前看到的原始内容，恢复原来的文字

# 恢复 title
work['title'] = 'June Science'

# 恢复 metaTitle
work['metaTitle'] = 'Brand, Packaging & Web Design for Probiotic Brand'

# 恢复 metaDescription
work['metaDescription'] = 'Brand and packaging design for June Science, a new range of targeted, fast-melt probiotics. '

# 恢复 thumbnailExcerpt
work['thumbnailExcerpt'] = 'Designing the next generation of targeted probiotics.'

# 恢复 hero section 内容
hero_content = work['workHeroSection']['sectionContent'][0]
hero_content['children'][0]['text'] = "June Science is trailblazing an entirely new category of probiotics. One that's targeted, tasty, and designed for life on the go. We worked closely with the team to help brand their breakthrough range."

# 恢复 servicesList
work['workHeroSection']['servicesList'] = ['Brand Identity', 'Packaging', 'Web Design', 'Product Development']

# 恢复 websiteURL
work['workHeroSection']['websiteURL'] = 'https://junescience.com/'

print('[OK] Restored original content!')
print(f'Title: {work["title"]}')
print(f'Services: {work["workHeroSection"]["servicesList"]}')

# 保存
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
