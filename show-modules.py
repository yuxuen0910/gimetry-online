import json

file_path = r'D:\01Personal_Projects\My_Websites_Portfolio_2\site\_next\data\NkaLovy8M3OdV54UztOF0\work\june-science.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

work = data['pageProps']['work']

print(f'Total work modules: {len(work["workModules"])}\n')
for i, module in enumerate(work['workModules'], 1):
    module_type = module.get('_type', 'Unknown')
    title = module.get('title', 'N/A')
    print(f'[{i}] Type: {module_type}, Title: {title}')
    
    if module_type == 'workTextBlock':
        # 提取文字内容
        for content in module['content']:
            if 'children' in content and len(content['children']) > 0:
                text = content['children'][0].get('text', '')
                print(f'    Text: {text[:150]}...')
    elif module_type.startswith('workSingle') or module_type.startswith('workDouble'):
        # 媒体模块
        if 'media' in module:
            print(f'    Media type: {module["media"].get("mediaType", "N/A")}')
        else:
            print(f'    Has leftMedia and rightMedia')
    print()
