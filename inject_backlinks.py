import os
import re

links_html = """<div class="mt-lg pt-lg border-t border-muted" style="margin-top: 2rem; padding-top: 1rem; border-top: 1px solid var(--color-border);">
    <h3 style="margin-bottom: 0.5rem; font-size: 1rem;">Partner Sites</h3>
    <div style="display: flex; flex-wrap: wrap; gap: 1rem; font-size: 0.875rem;">
        <a href="https://family-law-attorney-state.bongshai.com/" target="_blank" rel="noopener" class="text-muted" style="color: var(--color-text-muted); text-decoration: none;">Family Law</a>
        <a href="https://tax-filing-guide-military.bongshai.com/" target="_blank" rel="noopener" class="text-muted" style="color: var(--color-text-muted); text-decoration: none;">Military Tax Guide</a>
        <a href="https://hearing-aids-veterans.bongshai.com/" target="_blank" rel="noopener" class="text-muted" style="color: var(--color-text-muted); text-decoration: none;">Veterans Hearing Aids</a>
        <a href="https://ai-chatbot-platform-free.bongshai.com/" target="_blank" rel="noopener" class="text-muted" style="color: var(--color-text-muted); text-decoration: none;">Free AI Chatbots</a>
        <a href="https://mortgage-calculator-city-guide.bongshai.com/" target="_blank" rel="noopener" class="text-muted" style="color: var(--color-text-muted); text-decoration: none;">Mortgage Calculator</a>
        <a href="https://bathroom-renovation-diy-professional.bongshai.com/" target="_blank" rel="noopener" class="text-muted" style="color: var(--color-text-muted); text-decoration: none;">Bathroom DIY</a>
        <a href="https://extended-car-warranty-fleet.bongshai.com/" target="_blank" rel="noopener" class="text-muted" style="color: var(--color-text-muted); text-decoration: none;">Fleet Car Warranty</a>
        <a href="https://crypto-tax-calculator-safest.bongshai.com/" target="_blank" rel="noopener" class="text-muted" style="color: var(--color-text-muted); text-decoration: none;">Crypto Tax Tools</a>
        <a href="https://linkedin-optimization-tech-roles.bongshai.com/" target="_blank" rel="noopener" class="text-muted" style="color: var(--color-text-muted); text-decoration: none;">LinkedIn Optimization</a>
        <a href="https://study-abroad-guide-cost.bongshai.com/" target="_blank" rel="noopener" class="text-muted" style="color: var(--color-text-muted); text-decoration: none;">Study Abroad Costs</a>
        <a href="https://reverse-mortgage-guide-cost.bongshai.com/" target="_blank" rel="noopener" class="text-muted" style="color: var(--color-text-muted); text-decoration: none;">Reverse Mortgage Guide</a>
        <a href="https://retirement-savings-calculator-free.bongshai.com/" target="_blank" rel="noopener" class="text-muted" style="color: var(--color-text-muted); text-decoration: none;">Retirement Calculator</a>
        <a href="https://celsius-fahrenheit-converter-no.bongshai.com/" target="_blank" rel="noopener" class="text-muted" style="color: var(--color-text-muted); text-decoration: none;">Temp Converter Tools</a>
    </div>
</div>
"""

def inject_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'Partner Sites' in content:
        return # Already injected
        
    # Find the closing tag of grid-3 inside the footer
    # Usually it looks like: ...</ul></div></div><div class="text-center
    pattern = re.compile(r'(</div>)(\s*<div class="text-center text-sm text-muted">\&copy; 2026)')
    if pattern.search(content):
        new_content = pattern.sub(r'\1' + '\n' + links_html + r'\2', content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Injected in {filepath}")
    else:
        print(f"Could not find insertion point in {filepath}")

for root, dirs, files in os.walk('.'):
    if 'assets' in root or '.git' in root or '_astro' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            inject_in_file(os.path.join(root, f))

print("Injection complete.")
