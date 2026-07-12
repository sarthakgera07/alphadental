import subprocess
import os

def run_updates():
    # 1. Update index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Add id="scheduler" to the outer card div
    old_card_div = '<div class="bg-white/95 backdrop-blur-md border border-white/20 p-6 md:p-8 rounded-2xl shadow-2xl text-navy-dark w-full max-w-md relative overflow-hidden transition-all duration-300">'
    new_card_div = '<div id="scheduler" class="bg-white/95 backdrop-blur-md border border-white/20 p-6 md:p-8 rounded-2xl shadow-2xl text-navy-dark w-full max-w-md relative overflow-hidden transition-all duration-300">'
    html = html.replace(old_card_div, new_card_div)

    # Update Header booking link
    old_header_btn = '<a href="#booking" class="bg-navy-blue hover:bg-navy-dark border border-gold-accent/30 hover:border-gold-accent text-white px-5 py-2.5 rounded-md text-xs font-bold flex items-center gap-2 transition-all shadow-md hover:shadow-lg">'
    new_header_btn = '<a href="#scheduler" class="bg-navy-blue hover:bg-navy-dark border border-gold-accent/30 hover:border-gold-accent text-white px-5 py-2.5 rounded-md text-xs font-bold flex items-center gap-2 transition-all shadow-md hover:shadow-lg">'
    html = html.replace(old_header_btn, new_header_btn)

    # Update Hero booking link
    old_hero_btn = '<a href="#booking" class="bg-gold-accent hover:bg-gold-hover text-navy-dark px-8 py-3.5 rounded-md font-bold text-sm tracking-wider flex items-center gap-2 transition-all shadow-md btn-pulse-glow">'
    new_hero_btn = '<a href="#scheduler" class="bg-gold-accent hover:bg-gold-hover text-navy-dark px-8 py-3.5 rounded-md font-bold text-sm tracking-wider flex items-center gap-2 transition-all shadow-md btn-pulse-glow">'
    html = html.replace(old_hero_btn, new_hero_btn)

    # Update Mobile drawer booking link
    old_mobile_btn = '<a href="#booking" id="mobile-drawer-booking-btn" class="w-full bg-gold-accent text-white py-3 rounded-md text-sm font-bold flex items-center justify-center gap-2 shadow-md">'
    new_mobile_btn = '<a href="#scheduler" id="mobile-drawer-booking-btn" class="w-full bg-gold-accent text-white py-3 rounded-md text-sm font-bold flex items-center justify-center gap-2 shadow-md">'
    html = html.replace(old_mobile_btn, new_mobile_btn)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html booking redirects updated successfully!")


    # 2. Update blogs.html
    with open('blogs.html', 'r', encoding='utf-8') as f:
        blogs_html = f.read()

    # Update Header booking link in blogs.html
    old_blogs_header_btn = '<a href="index.html#booking" class="bg-gold-accent hover:bg-gold-hover text-white px-5 py-2.5 rounded-md text-xs font-bold flex items-center gap-2 transition-all shadow-md hover:shadow-lg">'
    new_blogs_header_btn = '<a href="index.html#scheduler" class="bg-gold-accent hover:bg-gold-hover text-white px-5 py-2.5 rounded-md text-xs font-bold flex items-center gap-2 transition-all shadow-md hover:shadow-lg">'
    blogs_html = blogs_html.replace(old_blogs_header_btn, new_blogs_header_btn)

    # Update Mobile drawer booking link in blogs.html
    old_blogs_mobile_btn = '<a href="index.html#booking" id="mobile-drawer-booking-btn" class="w-full bg-gold-accent text-white py-3 rounded-md text-sm font-bold flex items-center justify-center gap-2 shadow-md">'
    new_blogs_mobile_btn = '<a href="index.html#scheduler" id="mobile-drawer-booking-btn" class="w-full bg-gold-accent text-white py-3 rounded-md text-sm font-bold flex items-center justify-center gap-2 shadow-md">'
    blogs_html = blogs_html.replace(old_blogs_mobile_btn, new_blogs_mobile_btn)

    # Fix mobile drawer menu links in blogs.html to fully match reordered and renamed index items
    old_blogs_mobile_menu = """      <nav class="flex flex-col gap-5 py-8 text-base font-semibold text-dark-text">
        <a class="hover:text-gold-accent transition-colors py-2 border-b border-gray-50" href="index.html">Home</a>
        <a class="hover:text-gold-accent transition-colors py-2 border-b border-gray-50" href="index.html#about">About</a>
        <a class="hover:text-gold-accent transition-colors py-2 border-b border-gray-50" href="index.html#services">Services</a>
        <a class="hover:text-gold-accent transition-colors py-2 border-b border-gray-50" href="index.html#team">Our Team</a>
        <a class="hover:text-gold-accent transition-colors py-2 border-b border-gray-50" href="index.html#testimonials">Testimonials</a>
        <a class="hover:text-gold-accent transition-colors py-2 border-b border-gray-50" href="blogs.html">Blogs</a>
        <a class="hover:text-gold-accent transition-colors py-2 border-b border-gray-50" href="index.html#booking">Contacts</a>
      </nav>"""

    new_blogs_mobile_menu = """      <nav class="flex flex-col gap-4 py-6 text-base font-semibold text-dark-text">
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html">Home</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#chief-doctor">Founder</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#services">Services</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#team">Our Specialists</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#clinic-tour">Clinic Tour</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#testimonials">Testimonials</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="blogs.html">Blogs</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#booking">Contacts</a>
      </nav>"""

    blogs_html = blogs_html.replace(old_blogs_mobile_menu, new_blogs_mobile_menu)

    with open('blogs.html', 'w', encoding='utf-8') as f:
        f.write(blogs_html)
    print("blogs.html booking redirects and mobile menu synced successfully!")


    # 3. Git commit and push all files to GitHub
    git_path = r"C:\Users\Sarthak\AppData\Local\GitHubDesktop\app-3.6.2\resources\app\git\cmd\git.exe"
    
    print("Staging changes...")
    subprocess.run([git_path, "add", "."])
    
    print("Committing changes...")
    res = subprocess.run([git_path, "commit", "-m", "Redirect booking buttons to Hero scheduler and sync blogs navigation"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    
    print("Pushing to GitHub remote repository...")
    res = subprocess.run([git_path, "push", "origin", "main"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)

if __name__ == '__main__':
    run_updates()
