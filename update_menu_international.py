import os
import glob

directory = "e:/Adsense sites/1-10/1/petinsurance-pure-html"
files_updated = 0

html_files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)

target_str = '<a href="/articles/french-bulldog-insurance-cost">Breed Guides</a>'
replace_str = '<a href="/articles/french-bulldog-insurance-cost">Breed Guides</a><a href="/articles/pet-insurance-cost-united-kingdom">International Guides</a>'

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if target_str in content and 'International Guides' not in content:
        content = content.replace(target_str, replace_str)
        with open(file_path, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(content)
        files_updated += 1

print(f"Successfully updated menu to include International Guides in {files_updated} HTML files.")
