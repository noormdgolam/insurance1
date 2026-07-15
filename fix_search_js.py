import os
import glob

directory = "e:/Adsense sites/1/petinsurance-pure-html"
files_updated = 0

html_files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)

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
    
    # Check if the script logic is already there to avoid duplicates
    if "const searchInput = document.getElementById('searchInput');" not in content:
        content = content.replace('</body>', script_replacement)
        with open(file_path, 'w', encoding='utf-8', errors='ignore') as f:
            f.write(content)
        files_updated += 1

print(f"Successfully injected JS search logic into {files_updated} HTML files.")
