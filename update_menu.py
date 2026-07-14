import os
import glob

# The exact old nav string to replace
old_nav = '<nav class="desktop-nav" aria-label="Main Navigation" data-astro-cid-nen7h5rs><ul class="flex gap-md" style="list-style: none;" data-astro-cid-nen7h5rs><li data-astro-cid-nen7h5rs><a href="/" class="nav-link" data-astro-cid-nen7h5rs>Home</a></li><li data-astro-cid-nen7h5rs><a href="/articles" class="nav-link" data-astro-cid-nen7h5rs>Articles</a></li><li data-astro-cid-nen7h5rs><a href="/about" class="nav-link" data-astro-cid-nen7h5rs>About</a></li><li data-astro-cid-nen7h5rs><a href="/contact" class="nav-link" data-astro-cid-nen7h5rs>Contact</a></li></ul></nav>'

# The new nav string with inline styles and a dropdown menu
new_nav = """<style>
.dropdown { position: relative; display: inline-block; }
.dropdown-content { display: none; position: absolute; background-color: var(--color-surface); min-width: 180px; box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.1); z-index: 1000; border-radius: var(--border-radius); border: 1px solid var(--color-border); padding: 0.5rem 0; top: 100%; left: 0; }
.dropdown-content a { color: var(--color-text); padding: 10px 16px; text-decoration: none; display: block; font-size: 0.95rem; border-bottom: 1px solid #f1f1f1; }
.dropdown-content a:last-child { border-bottom: none; }
.dropdown-content a:hover { background-color: var(--color-primary-light); color: var(--color-primary-dark); }
.dropdown:hover .dropdown-content { display: block; }
</style>
<nav class="desktop-nav" aria-label="Main Navigation" data-astro-cid-nen7h5rs><ul class="flex gap-md" style="list-style: none; align-items: center;" data-astro-cid-nen7h5rs><li data-astro-cid-nen7h5rs><a href="/" class="nav-link" data-astro-cid-nen7h5rs>Home</a></li><li class="dropdown" data-astro-cid-nen7h5rs><a href="/articles" class="nav-link" data-astro-cid-nen7h5rs style="padding-bottom: 1.5rem;">Articles &#9662;</a><div class="dropdown-content"><a href="/articles">All Articles</a><a href="/articles/pet-insurance-cost-texas">State Guides</a><a href="/articles/french-bulldog-insurance-cost">Breed Guides</a></div></li><li data-astro-cid-nen7h5rs><a href="/about" class="nav-link" data-astro-cid-nen7h5rs>About</a></li><li data-astro-cid-nen7h5rs><a href="/contact" class="nav-link" data-astro-cid-nen7h5rs>Contact</a></li></ul></nav>"""

directory = "e:/Adsense sites/1-10/1/petinsurance-pure-html"
files_updated = 0

# Recursively find all HTML files
html_files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if old_nav in content:
        content = content.replace(old_nav, new_nav)
        with open(file_path, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(content)
        files_updated += 1
    elif new_nav in content:
        # Already updated
        pass
    else:
        print(f"Warning: Nav string not found in {file_path}")

print(f"Successfully updated menu in {files_updated} HTML files.")
