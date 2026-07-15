import os
import glob
import re

files = glob.glob('**/*.html', recursive=True)

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    modified = False
    
    # Extract Title and Description
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    title = title_match.group(1) if title_match else ""
    
    desc_match = re.search(r'<meta name="description" content="(.*?)">', content, re.IGNORECASE)
    desc = desc_match.group(1) if desc_match else ""
    
    # URL construction
    url_path = f.replace('\\', '/')
    if url_path.endswith('index.html') and url_path != 'index.html':
        url_path = url_path.replace('index.html', '')
        url = f"https://insurance1.bongshai.com/{url_path}"
    else:
        url = f"https://insurance1.bongshai.com/{url_path}"
        
    if url.endswith('index.html'):
        url = "https://insurance1.bongshai.com/"
    
    # Fix Hardcoded Texas tags
    if 'content="How Much Is Pet Insurance in Texas' in content and 'texas' not in f.lower():
        content = re.sub(r'<meta property="twitter:title" content="[^"]*">', f'<meta property="twitter:title" content="{title}">', content)
        content = re.sub(r'<meta property="twitter:description" content="[^"]*">', f'<meta property="twitter:description" content="{desc}">', content)
        content = re.sub(r'<meta property="twitter:url" content="[^"]*">', f'<meta property="twitter:url" content="{url}">', content)
        modified = True
        
    # Inject missing Canonical and OG tags
    if '<link rel="canonical"' not in content:
        seo_tags = f'''
    <link rel="canonical" href="{url}">
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="{url}">
    <meta property="twitter:title" content="{title}">
    <meta property="twitter:description" content="{desc}">'''
        # Inject right after <meta name="description" ...>
        if desc_match:
            content = content.replace(desc_match.group(0), desc_match.group(0) + seo_tags)
            modified = True
        elif title_match:
            content = content.replace(title_match.group(0), title_match.group(0) + seo_tags)
            modified = True
                
    if modified:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
