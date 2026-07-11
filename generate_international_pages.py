import os
import random

output_dir = "e:/Adsense sites/1/petinsurance-pure-html/articles"

countries = [
    ("United Kingdom", "£", 30, 60),
    ("Canada", "$", 45, 85),
    ("Australia", "$", 50, 95),
    ("India", "₹", 1500, 3000),
    ("South Africa", "R", 300, 600),
    ("New Zealand", "$", 45, 80),
    ("Ireland", "€", 25, 55),
    ("Germany", "€", 35, 65),
    ("France", "€", 30, 60),
    ("Spain", "€", 25, 50),
    ("Italy", "€", 30, 55),
    ("Netherlands", "€", 35, 65),
    ("Sweden", "kr", 350, 650),
    ("Singapore", "$", 55, 95),
    ("United Arab Emirates", "AED", 150, 300)
]

images = [
    "/images/cat_playing_1783777125388.png",
    "/images/dog_living_room_1783777113868.png",
    "/images/french_bulldog_1783777148813.png",
    "/images/outdoor_dog_1783777160261.png",
    "/images/vet_office_1783777138383.png"
]

authors = ["Jane Doe", "John Smith", "Emily Chen", "Michael Brown"]

# We will read a base template from an existing file to ensure we get the full nav and search bar
base_file = "e:/Adsense sites/1/petinsurance-pure-html/articles/pet-insurance-cost-texas/index.html"
with open(base_file, 'r', encoding='utf-8', errors='ignore') as f:
    template = f.read()

# We need to extract the parts before <main> and after </main>
header_part = template.split('<main>')[0] + '<main>'
footer_part = '</main>' + template.split('</main>')[1]

def generate_country_html(country, currency, min_cost, max_cost):
    slug = f"pet-insurance-cost-{country.lower().replace(' ', '-')}"
    title = f"How Much Is Pet Insurance in {country}? A 2026 Guide"
    desc = f"Discover the average cost of pet insurance in {country}. Compare plans, understand local vet costs, and find the most affordable coverage."
    image = random.choice(images)
    author = random.choice(authors)
    
    # We replace the title and description in the header part
    import re
    curr_header = re.sub(r'<title>.*?</title>', f'<title>{title} | Pet Insurance Rates</title>', header_part)
    curr_header = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">', curr_header)
    curr_header = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://insurance1.bongshai.com/articles/{slug}/">', curr_header)
    curr_header = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title}">', curr_header)
    curr_header = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{desc}">', curr_header)
    curr_header = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="https://insurance1.bongshai.com/articles/{slug}/">', curr_header)
    
    article_content = f"""<article class="container mt-lg mb-xl prose"><header class="mb-lg"><h1 style="margin-bottom: var(--spacing-sm);">{title}</h1><p class="text-muted">By {author} | Last updated: July 11, 2026</p></header><div class="content"><p>If you live in {country}, you already know that the cost of living can vary significantly—and veterinary care is no exception. Pet insurance is one of the best ways to protect your finances from unexpected vet bills.</p>
<p><img src="{image}" alt="Happy pet in {country}"></p>
<p>But exactly how much does pet insurance cost in {country}?</p>
<h2 id="average-cost-of-pet-insurance-in-country">Average Cost of Pet Insurance in {country}</h2>
<p>In {country}, the average monthly premium for pet insurance is typically around <strong>{currency}{max_cost} for dogs</strong> and <strong>{currency}{min_cost} for cats</strong>. However, rates vary significantly based on your exact location, the breed of your pet, and the level of coverage you choose.</p>
<h3 id="factors-influencing-your-premium">Factors Influencing Your Premium</h3>
<ol>
<li><strong>Location:</strong> Vet costs in major metropolitan areas are higher than in rural parts of {country}. Insurance providers adjust premiums to reflect local veterinary costs.</li>
<li><strong>Breed:</strong> Purebred dogs often cost more to insure than mixed breeds due to genetic health predispositions.</li>
<li><strong>Age:</strong> Insuring a puppy or kitten is much cheaper than insuring a senior pet.</li>
</ol>
<h3 id="cost-breakdown-table">Cost Breakdown Table</h3>
<table>
<thead>
<tr>
<th style="text-align: left">Pet Type</th>
<th style="text-align: left">Average Monthly Premium in {country}</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left"><strong>Dogs (Mixed Breed)</strong></td>
<td style="text-align: left">{currency}{int(max_cost * 0.8)} - {currency}{int(max_cost * 1.2)}</td>
</tr>
<tr>
<td style="text-align: left"><strong>Cats (Mixed Breed)</strong></td>
<td style="text-align: left">{currency}{int(min_cost * 0.8)} - {currency}{int(min_cost * 1.2)}</td>
</tr>
<tr>
<td style="text-align: left"><strong>Purebred Dogs</strong></td>
<td style="text-align: left">{currency}{int(max_cost * 1.3)} - {currency}{int(max_cost * 1.8)}</td>
</tr>
</tbody>
</table>
<h2 id="frequently-asked-questions">Frequently Asked Questions</h2>
<h3 id="is-pet-insurance-mandatory-in-country">Is pet insurance mandatory in {country}?</h3>
<p>No, pet insurance is completely optional in {country}. However, given the high cost of emergency vet care, it is highly recommended by veterinary professionals.</p>
<h3 id="do-premiums-go-up-as-my-pet-gets-older">Do premiums go up as my pet gets older?</h3>
<p>Yes. Most pet insurance companies will increase your premium as your pet ages because the statistical likelihood of illness increases.</p>
</div><!-- Mid-article Ad Placeholder --><div class="ad-placeholder format-in-article" data-astro-cid-fnsbmqs7><p data-astro-cid-fnsbmqs7>Advertisement Space</p><span class="text-sm" data-astro-cid-fnsbmqs7>(in-article)</span></div><footer class="mt-xl"><div class="author-bio card mt-lg flex items-center gap-md"><div class="author-avatar" style="width: 60px; height: 60px; border-radius: 50%; background-color: var(--color-primary-light); display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 1.5rem; color: var(--color-primary);">{author[0]}</div><div><h4 style="margin: 0;">Written by {author}</h4><p class="text-sm text-muted" style="margin: 0;">Senior Insurance Analyst</p><p class="text-sm mt-sm" style="margin-bottom: 0;">{author} is an experienced writer focusing on helping pet owners find affordable and comprehensive insurance coverage.</p></div></div><div class="ymyl-disclaimer mt-lg" style="background-color: var(--color-alert-bg); color: var(--color-alert-text); padding: var(--spacing-md); border-left: 4px solid #ffc107; border-radius: 0 var(--border-radius) var(--border-radius) 0;"><strong>Disclaimer:</strong> The content on this website is for educational and informational purposes only and does not constitute professional financial, insurance, or legal advice. Insurance rates and coverage details vary by provider, state, and individual circumstances. Please consult with a licensed insurance agent before making any purchasing decisions.</div></footer></article>"""

    final_html = curr_header + article_content + footer_part
    
    dir_path = os.path.join(output_dir, slug)
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(final_html)

for country, cur, min_c, max_c in countries:
    generate_country_html(country, cur, min_c, max_c)

print(f"Successfully generated {len(countries)} international HTML pages.")
