import subprocess

def fix_mobile_drawer():
    # 1. Update index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Locate current mobile drawer menu in index.html
    old_mobile_menu = """      <nav class="flex flex-col gap-4 py-6 text-base font-semibold text-dark-text">
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#home">Home</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#chief-doctor">Founder</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#team">Our Specialists</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#clinic-tour">Clinic Tour</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#services">Services</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#testimonials">Testimonials</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="blogs.html">Blogs</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#booking">Contacts</a>
      </nav>"""

    # Reorder it: Home -> Founder -> Services -> Our Specialists -> Clinic Tour -> Testimonials -> Blogs -> Contacts
    new_mobile_menu = """      <nav class="flex flex-col gap-4 py-6 text-base font-semibold text-dark-text">
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#home">Home</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#chief-doctor">Founder</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#services">Services</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#team">Our Specialists</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#clinic-tour">Clinic Tour</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#testimonials">Testimonials</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="blogs.html">Blogs</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#scheduler">Contacts</a>
      </nav>"""

    # Note that in the mobile menu, "Contacts" should link to #scheduler as well to be consistent with the other booking actions!
    html = html.replace(old_mobile_menu, new_mobile_menu)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html mobile drawer reordered successfully!")


    # 2. Update blogs.html
    with open('blogs.html', 'r', encoding='utf-8') as f:
        blogs_html = f.read()

    # Locate current mobile drawer menu in blogs.html
    old_blogs_mobile_menu = """      <nav class="flex flex-col gap-4 py-6 text-base font-semibold text-dark-text">
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html">Home</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#chief-doctor">Founder</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#services">Services</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#team">Our Specialists</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#clinic-tour">Clinic Tour</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#testimonials">Testimonials</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="blogs.html">Blogs</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#booking">Contacts</a>
      </nav>"""

    # Reorder it: Home -> Founder -> Services -> Our Specialists -> Clinic Tour -> Testimonials -> Blogs -> Contacts
    new_blogs_mobile_menu = """      <nav class="flex flex-col gap-4 py-6 text-base font-semibold text-dark-text">
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html">Home</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#chief-doctor">Founder</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#services">Services</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#team">Our Specialists</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#clinic-tour">Clinic Tour</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#testimonials">Testimonials</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="blogs.html">Blogs</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#scheduler">Contacts</a>
      </nav>"""

    blogs_html = blogs_html.replace(old_blogs_mobile_menu, new_blogs_mobile_menu)

    with open('blogs.html', 'w', encoding='utf-8') as f:
        f.write(blogs_html)
    print("blogs.html mobile drawer reordered successfully!")


    # 3. Git commit and push changes
    git_path = r"C:\Users\Sarthak\AppData\Local\GitHubDesktop\app-3.6.2\resources\app\git\cmd\git.exe"
    
    print("Staging changes...")
    subprocess.run([git_path, "add", "."])
    
    print("Committing changes...")
    res = subprocess.run([git_path, "commit", "-m", "Sync mobile menu drawer link order to match desktop hierarchy"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    
    print("Pushing to GitHub remote repository...")
    res = subprocess.run([git_path, "push", "origin", "main"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)

if __name__ == '__main__':
    fix_mobile_drawer()
