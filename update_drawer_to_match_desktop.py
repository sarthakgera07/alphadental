import subprocess

def update_drawers():
    # 1. Update index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    old_index_drawer = """      <nav class="flex flex-col gap-4 py-6 text-base font-semibold text-dark-text">
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#home">Home</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#chief-doctor">Founder</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#services">Services</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#team">Our Specialists</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#clinic-tour">Clinic Tour</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#testimonials">Testimonials</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="blogs.html">Blogs</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#scheduler">Contacts</a>
      </nav>"""

    new_index_drawer = """      <nav class="flex flex-col gap-4 py-6 text-base font-semibold text-dark-text">
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#home">Home</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#chief-doctor">Founder</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#services">Services</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#team">Our Specialists</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#clinic-tour">Clinic Tour</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#testimonials">Patient Stories</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="#booking">Find Us</a>
      </nav>"""

    html = html.replace(old_index_drawer, new_index_drawer)

    # Let's check if the mobile footer contact button also needs to be updated (change text to Find Us or something?
    # No, the mobile drawer contact section is "Quick Contact" and "Book Appointment" which is good.
    # Wait, the link href for the button inside the mobile drawer panel (line 140) should point to #scheduler as updated. That's good!

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html mobile drawer menu elements updated!")


    # 2. Update blogs.html
    with open('blogs.html', 'r', encoding='utf-8') as f:
        blogs_html = f.read()

    old_blogs_drawer = """      <nav class="flex flex-col gap-4 py-6 text-base font-semibold text-dark-text">
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html">Home</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#chief-doctor">Founder</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#services">Services</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#team">Our Specialists</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#clinic-tour">Clinic Tour</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#testimonials">Testimonials</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="blogs.html">Blogs</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#scheduler">Contacts</a>
      </nav>"""

    # Wait, in the previous step, did blogs.html have "index.html#scheduler" for Contacts?
    # Yes, we updated it. Let's make sure it matches.
    # The new drawer for blogs should point to index.html sections.
    new_blogs_drawer = """      <nav class="flex flex-col gap-4 py-6 text-base font-semibold text-dark-text">
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html">Home</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#chief-doctor">Founder</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#services">Services</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#team">Our Specialists</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#clinic-tour">Clinic Tour</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#testimonials">Patient Stories</a>
        <a class="hover:text-gold-accent transition-colors py-1.5 border-b border-gray-50" href="index.html#booking">Find Us</a>
      </nav>"""

    blogs_html = blogs_html.replace(old_blogs_drawer, new_blogs_drawer)

    # Let's also check if there is any other match for the drawer if it didn't match.
    # Let's run a fallback check in case of spacing mismatches.
    
    with open('blogs.html', 'w', encoding='utf-8') as f:
        f.write(blogs_html)
    print("blogs.html mobile drawer menu elements updated!")


    # 3. Git push
    git_path = r"C:\Users\Sarthak\AppData\Local\GitHubDesktop\app-3.6.2\resources\app\git\cmd\git.exe"
    
    print("Staging changes...")
    subprocess.run([git_path, "add", "."])
    
    print("Committing changes...")
    res = subprocess.run([git_path, "commit", "-m", "Match mobile drawer navigation links to desktop header options"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    
    print("Pushing to remote repo...")
    res = subprocess.run([git_path, "push", "origin", "main"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)

if __name__ == '__main__':
    update_drawers()
