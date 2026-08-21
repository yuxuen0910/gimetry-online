import urllib.request
import json

url = "https://www.onboxcreative.com/_next/data/NkaLovy8M3OdV54UztOF0/work/june-science.json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read().decode('utf-8'))
        
        if 'pageProps' in data and 'work' in data['pageProps']:
            work = data['pageProps']['work']
            print(f"Title: {work['title']}")
            print(f"Meta Title: {work['metaTitle']}")
            print(f"Modules count: {len(work['workModules'])}\n")
            
            for i, module in enumerate(work['workModules'], 1):
                mtype = module.get('_type', 'Unknown')
                title = module.get('title', 'N/A')
                
                if mtype == 'workTextBlock':
                    # Get text content
                    for content in module['content']:
                        if 'children' in content and len(content['children']) > 0:
                            text = content['children'][0].get('text', '')
                            print(f"[{i}] {title} ({mtype})")
                            print(f"    Text: {text[:200]}...")
                            print()
                else:
                    print(f"[{i}] {title} ({mtype})")
                    # Show media info
                    if 'media' in module:
                        media = module['media']
                        print(f"    Media: {media.get('mediaType', 'N/A')}")
                    elif 'leftMedia' in module:
                        print(f"    Media: Double layout")
                    print()
        else:
            print("No work data found")
            print(json.dumps(data, indent=2)[:500])
except Exception as e:
    print(f"Error: {e}")
