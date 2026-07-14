import os
import re

file_path = "generate_international_pages.py"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacement = '''
    spin_intros = [
        f"<p>If you live in {country}, you already know that the cost of living can vary significantly—and veterinary care is no exception. Pet insurance is one of the best ways to protect your finances from unexpected vet bills.</p>",
        f"<p>Navigating the veterinary landscape in {country} can be daunting. As costs continue to rise, securing a reliable pet insurance policy has never been more important for responsible pet owners.</p>",
        f"<p>Protecting your furry companion in {country} means planning for the unexpected. With vet costs soaring, pet insurance offers a vital safety net for your family's finances.</p>"
    ]
    
    spin_costs = [
        f"""<h2 id="average-cost-of-pet-insurance-in-country">Average Cost of Pet Insurance in {country}</h2>
<p>In {country}, the average monthly premium for pet insurance is typically around <strong>{currency}{max_cost} for dogs</strong> and <strong>{currency}{min_cost} for cats</strong>. However, rates vary significantly based on your exact location, the breed of your pet, and the level of coverage you choose.</p>""",
        f"""<h2 id="average-cost-of-pet-insurance-in-country">How Much Should You Expect to Pay in {country}?</h2>
<p>Generally, pet parents in {country} can expect to pay roughly <strong>{currency}{max_cost} monthly for dogs</strong> and <strong>{currency}{min_cost} for cats</strong>. Remember that these are averages; your specific premium will depend on your pet's age and your local postal code.</p>""",
        f"""<h2 id="average-cost-of-pet-insurance-in-country">{country} Pet Insurance Pricing Guide</h2>
<p>While prices fluctuate, standard monthly policies in {country} hover around <strong>{currency}{max_cost} for dogs</strong> and <strong>{currency}{min_cost} for cats</strong>. Comprehensive plans with low deductibles will naturally push these averages higher.</p>"""
    ]
    
    intro_text = random.choice(spin_intros)
    cost_text = random.choice(spin_costs)

    article_content = f"""<article class="container mt-lg mb-xl prose"><header class="mb-lg"><h1 style="margin-bottom: var(--spacing-sm);">{title}</h1><p class="text-muted">By {author} | Last updated: July 11, 2026</p></header><div class="content">
{intro_text}
<p><img src="{image}" alt="Happy pet in {country}"></p>
<p>But exactly how much does pet insurance cost in {country}?</p>
{cost_text}
'''

content = re.sub(r'    article_content = f"""<article class="container mt-lg mb-xl prose"><header class="mb-lg"><h1 style="margin-bottom: var\(--spacing-sm\);">{title}</h1><p class="text-muted">By {author} \| Last updated: July 11, 2026</p></header><div class="content"><p>If you live in {country}, you already know that the cost of living can vary significantly—and veterinary care is no exception\. Pet insurance is one of the best ways to protect your finances from unexpected vet bills\.</p>\n<p><img src="{image}" alt="Happy pet in {country}"></p>\n<p>But exactly how much does pet insurance cost in {country}\?</p>\n<h2 id="average-cost-of-pet-insurance-in-country">Average Cost of Pet Insurance in {country}</h2>\n<p>In {country}, the average monthly premium for pet insurance is typically around <strong>{currency}{max_cost} for dogs</strong> and <strong>{currency}{min_cost} for cats</strong>\. However, rates vary significantly based on your exact location, the breed of your pet, and the level of coverage you choose\.</p>', replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
