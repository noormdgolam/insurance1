import os
import glob

# Set the directory path
dir_path = r"e:\Adsense sites\1\petinsurance-pure-html"
old_domain = "https://insurance1.bongshai.com"
new_domain = "https://insurance1.bongshai.com"

# Extensions to check
extensions = ["*.html", "*.xml", "*.py", "*.json", "*.txt"]

# Walk through directory
for ext in extensions:
    for filepath in glob.glob(os.path.join(dir_path, "**", ext), recursive=True):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if old_domain in content:
                new_content = content.replace(old_domain, new_domain)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
        except Exception as e:
            print(f"Failed to process {filepath}: {e}")

# Rename sitemap-index.xml to sitemap.xml
old_sitemap = os.path.join(dir_path, "sitemap-index.xml")
new_sitemap = os.path.join(dir_path, "sitemap.xml")

if os.path.exists(old_sitemap):
    os.rename(old_sitemap, new_sitemap)
    print(f"Renamed {old_sitemap} to {new_sitemap}")

# Update robots.txt to point to sitemap.xml instead of sitemap-index.xml
robots_path = os.path.join(dir_path, "robots.txt")
if os.path.exists(robots_path):
    with open(robots_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if "sitemap-index.xml" in content:
        new_content = content.replace("sitemap-index.xml", "sitemap.xml")
        with open(robots_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated robots.txt to point to sitemap.xml")
