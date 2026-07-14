import os
import glob
import json
import re

directory = "e:/Adsense sites/1-10/1/petinsurance-pure-html"
index_data = []

html_files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)

for file_path in html_files:
    # Skip error pages
    if '404' in file_path:
        continue
        
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content)
    if not title_match:
        continue
        
    full_title = title_match.group(1)
    title = full_title.replace(" | Pet Insurance Rates", "").strip()
    
    # Calculate URL relative to root
    rel_path = os.path.relpath(file_path, directory).replace("\\", "/")
    
    if rel_path == "index.html":
        url = "/"
    else:
        # e.g., "articles/french-bulldog-insurance-cost/index.html" -> "/articles/french-bulldog-insurance-cost/"
        url = "/" + rel_path.replace("index.html", "")
        
    index_data.append({
        "title": title,
        "url": url
    })

output_path = os.path.join(directory, "search-index.json")
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(index_data, f, separators=(',', ':'))

print(f"Generated search-index.json with {len(index_data)} entries.")
