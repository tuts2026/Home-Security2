import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Using regex to split out everything before the first section and everything after (and including) the footer
# Find the index of the first <section
first_section_idx = html.find('<section')
head_nav = html[:first_section_idx]

# Find the index of the footer
footer_idx = html.find('<footer')
footer = html[footer_idx:]

# Fix nav links to be absolute paths
head_nav = head_nav.replace('href="#systems"', 'href="/#systems"')
head_nav = head_nav.replace('href="#defense"', 'href="/#defense"')
head_nav = head_nav.replace('href="#suburbs"', 'href="/#suburbs"')
head_nav = head_nav.replace('href="#audit"', 'href="/#audit"')

# Make GUARDIAN EAGLE a link home
head_nav = head_nav.replace('<div class="text-headline-md font-headline-md font-black tracking-tighter text-primary">GUARDIAN EAGLE</div>', '<a href="/" class="text-headline-md font-headline-md font-black tracking-tighter text-primary hover:opacity-80 transition-opacity">GUARDIAN EAGLE</a>')

# Update footer links in the footer variable
footer = footer.replace('href="#">Privacy Policy', 'href="/privacy.html">Privacy Policy')
footer = footer.replace('href="#">Terms of Service', 'href="/terms.html">Terms of Service')

# Also update index.html footer
new_index = html.replace('href="#">Privacy Policy', 'href="/privacy.html">Privacy Policy').replace('href="#">Terms of Service', 'href="/terms.html">Terms of Service')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index)

privacy_body = """
<main class="pt-24 pb-32 max-w-4xl mx-auto px-margin-desktop">
<h1 class="font-display-xl text-display-xl leading-[1.1] text-on-surface mb-8">Privacy Policy</h1>
<div class="space-y-6 font-body-lg text-body-lg text-on-surface-variant">
<p><strong>Last Updated: July 2026</strong></p>
<p>Guardian Eagle Security ("we", "our", or "us") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website (rousehillsecurity.com.au) and use our security installation services in Northwest Sydney.</p>

<h2 class="font-headline-md text-headline-md text-on-surface mt-12 mb-4">1. Information We Collect</h2>
<p>We may collect personal information that you voluntarily provide to us when expressing an interest in obtaining information about us or our products and services. The personal information that we collect depends on the context of your interactions with us and the website, the choices you make, and the products and features you use. The personal information we collect can include the following:</p>
<ul class="list-disc pl-8 space-y-2">
<li>Names</li>
<li>Phone numbers</li>
<li>Email addresses</li>
<li>Property addresses and Suburb locations</li>
</ul>

<h2 class="font-headline-md text-headline-md text-on-surface mt-12 mb-4">2. How We Use Your Information</h2>
<p>We use the information we collect or receive:</p>
<ul class="list-disc pl-8 space-y-2">
<li>To facilitate and provide our security installation services.</li>
<li>To send you administrative information, such as quotes or safety audits.</li>
<li>To respond to your inquiries and offer support.</li>
</ul>

<h2 class="font-headline-md text-headline-md text-on-surface mt-12 mb-4">3. Security Footage &amp; Data Privacy</h2>
<p>For clients using our CCTV and smart alarm systems, please note that all camera feeds, recordings, and system data are entirely encrypted and controlled by you. Guardian Eagle Security does NOT retain access to your live feeds or recorded footage without your explicit, temporary authorization for technical support purposes.</p>

<h2 class="font-headline-md text-headline-md text-on-surface mt-12 mb-4">4. Contact Us</h2>
<p>If you have questions or comments about this policy, you may contact us regarding our services in the Northwest Sydney region.</p>
</div>
</main>
"""

terms_body = """
<main class="pt-24 pb-32 max-w-4xl mx-auto px-margin-desktop">
<h1 class="font-display-xl text-display-xl leading-[1.1] text-on-surface mb-8">Terms of Service</h1>
<div class="space-y-6 font-body-lg text-body-lg text-on-surface-variant">
<p><strong>Last Updated: July 2026</strong></p>
<p>Welcome to Guardian Eagle Security. By accessing our website (rousehillsecurity.com.au) and using our services, you agree to be bound by these Terms of Service.</p>

<h2 class="font-headline-md text-headline-md text-on-surface mt-12 mb-4">1. Services Provided</h2>
<p>Guardian Eagle Security provides professional installation and maintenance of CCTV, smart alarms, and access control systems for residential and commercial properties in Northwest Sydney.</p>

<h2 class="font-headline-md text-headline-md text-on-surface mt-12 mb-4">2. Warranties</h2>
<p>We provide a 3-Year Warranty on parts and workmanship for systems directly installed by our licensed technicians. This warranty does not cover damage resulting from misuse, vandalism, extreme weather events, or unauthorized modifications.</p>

<h2 class="font-headline-md text-headline-md text-on-surface mt-12 mb-4">3. Master License</h2>
<p>All work is carried out by NSW Master Licensed professionals. Clients are responsible for ensuring that they have the legal right to authorize the installation of surveillance equipment on their premises.</p>

<h2 class="font-headline-md text-headline-md text-on-surface mt-12 mb-4">4. Limitation of Liability</h2>
<p>While our systems are designed to deter unauthorized entry, Guardian Eagle Security does not guarantee that our systems will prevent all instances of theft, property damage, or personal injury. We shall not be liable for any direct, indirect, incidental, special, or consequential damages resulting from a security breach.</p>
</div>
</main>
"""

with open('privacy.html', 'w', encoding='utf-8') as f:
    f.write(head_nav + privacy_body + footer)

with open('terms.html', 'w', encoding='utf-8') as f:
    f.write(head_nav + terms_body + footer)
