import os
import glob

directory = "e:/Adsense sites/1/petinsurance-pure-html"
files_updated = 0

html_files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)

nav_target = '<li data-astro-cid-nen7h5rs><a href="/contact" class="nav-link" data-astro-cid-nen7h5rs>Contact</a></li></ul>'
nav_replacement = """<li data-astro-cid-nen7h5rs><a href="/contact" class="nav-link" data-astro-cid-nen7h5rs>Contact</a></li>
<li data-astro-cid-nen7h5rs class="search-container" style="position: relative; margin-left: 1rem;">
  <input type="text" id="searchInput" placeholder="Search articles..." style="padding: 0.4rem 0.8rem; border-radius: 20px; border: 1px solid var(--color-border); font-size: 0.9rem; width: 220px; background-color: var(--color-surface); color: var(--color-text);">
  <div id="searchResults" style="display: none; position: absolute; top: 100%; right: 0; background: var(--color-surface); min-width: 280px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); border: 1px solid var(--color-border); border-radius: 8px; margin-top: 0.5rem; z-index: 1001; max-height: 300px; overflow-y: auto;"></div>
</li>
</ul>"""

script_target = '</body>'
script_replacement = """<script>
document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');
    let searchData = null;

    if (!searchInput) return;

    searchInput.addEventListener('focus', function() {
        if (!searchData) {
            fetch('/search-index.json')
                .then(res => res.json())
                .then(data => { searchData = data; })
                .catch(err => console.error('Error loading search index:', err));
        }
    });

    searchInput.addEventListener('input', function(e) {
        const query = e.target.value.toLowerCase();
        if (query.length < 2) {
            searchResults.style.display = 'none';
            return;
        }
        if (!searchData) return;

        const results = searchData.filter(item => item.title.toLowerCase().includes(query)).slice(0, 6);
        
        if (results.length > 0) {
            searchResults.innerHTML = results.map(r => `<a href="${r.url}" style="display: block; padding: 10px 15px; border-bottom: 1px solid #eee; text-decoration: none; color: var(--color-text); font-size: 0.9rem;">${r.title}</a>`).join('');
            searchResults.style.display = 'block';
        } else {
            searchResults.innerHTML = `<div style="padding: 10px 15px; color: #777; font-size: 0.9rem;">No results found</div>`;
            searchResults.style.display = 'block';
        }
    });

    document.addEventListener('click', function(e) {
        if (searchInput && searchResults && !searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.style.display = 'none';
        }
    });
});
</script>
</body>"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    modified = False
    
    if nav_target in content:
        content = content.replace(nav_target, nav_replacement)
        modified = True
        
    if script_target in content and 'id="searchInput"' not in content:
        content = content.replace(script_target, script_replacement)
        modified = True
        
    if modified:
        with open(file_path, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(content)
        files_updated += 1

print(f"Successfully injected search into {files_updated} HTML files.")
