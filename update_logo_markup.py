import subprocess

def update_markup():
    # 1. Update index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Header Logo Section replacement in index.html
    old_index_logo = """    <a href="#" class="flex items-center gap-3 group">
      <div class="w-10 h-10 flex items-center justify-center bg-navy-blue text-gold-accent rounded-md shadow-md shrink-0 border border-gold-accent/20">
        <img src="logo_icon.png" alt="Alpha Dental Logo Icon" class="w-7 h-7 object-contain transition-transform group-hover:scale-110"/>
      </div>
      <div class="flex flex-col">
        <span class="text-base md:text-lg font-bold tracking-wider text-white font-serif leading-none">ALPHA DENTAL</span>
        <span class="text-[9px] tracking-[0.18em] text-gold-accent font-semibold">INTERNATIONAL</span>
      </div>
    </a>"""

    new_index_logo = """    <a href="#" class="flex items-center gap-2.5 group">
      <img src="logo_icon.png" alt="Alpha Dental Logo" class="h-8 w-auto object-contain transition-transform group-hover:scale-105 shrink-0"/>
      <div class="flex flex-col">
        <span class="text-base md:text-lg font-bold tracking-wider text-white font-serif leading-none">ALPHA DENTAL</span>
        <span class="text-[9px] tracking-[0.18em] text-gold-accent font-semibold">INTERNATIONAL</span>
      </div>
    </a>"""

    html = html.replace(old_index_logo, new_index_logo)

    # Mobile Drawer Logo Section replacement in index.html
    old_index_drawer_logo = """      <div class="flex items-center justify-between pb-6 border-b border-border-color">
        <div class="flex items-center gap-2">
          <img src="logo_icon.png" alt="Alpha Dental Logo Icon" class="w-6 h-6 object-contain shrink-0"/>
          <span class="text-lg font-bold font-serif text-navy-dark">Alpha Dental International</span>
        </div>"""

    new_index_drawer_logo = """      <div class="flex items-center justify-between pb-6 border-b border-border-color">
        <div class="flex items-center gap-2.5">
          <img src="logo_icon.png" alt="Alpha Dental Logo" class="h-7 w-auto object-contain shrink-0"/>
          <div class="flex flex-col">
            <span class="text-sm font-bold tracking-wider text-navy-dark font-serif leading-none">ALPHA DENTAL</span>
            <span class="text-[8px] tracking-[0.18em] text-gold-accent font-semibold">INTERNATIONAL</span>
          </div>
        </div>"""

    html = html.replace(old_index_drawer_logo, new_index_drawer_logo)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html logo layout updated successfully!")


    # 2. Update blogs.html
    with open('blogs.html', 'r', encoding='utf-8') as f:
        blogs_html = f.read()

    # Header Logo Section replacement in blogs.html
    old_blogs_logo = """    <a href="#" class="flex items-center gap-3 group">
      <div class="w-10 h-10 flex items-center justify-center bg-navy-dark text-gold-accent rounded-md shadow-md shrink-0">
        <img src="logo_icon.png" alt="Alpha Dental Logo Icon" class="w-7 h-7 object-contain transition-transform group-hover:scale-110"/>
      </div>
      <div class="flex flex-col">
        <span class="text-lg md:text-xl font-bold tracking-wider text-navy-dark font-serif leading-none">ALPHA DENTAL INTERNATIONAL</span>
        <span class="text-[9px] tracking-[0.18em] text-gray-500 font-semibold">INTERNATIONAL</span>
      </div>
    </a>"""

    new_blogs_logo = """    <a href="#" class="flex items-center gap-2.5 group">
      <img src="logo_icon.png" alt="Alpha Dental Logo" class="h-8 w-auto object-contain transition-transform group-hover:scale-105 shrink-0"/>
      <div class="flex flex-col">
        <span class="text-base md:text-lg font-bold tracking-wider text-navy-dark font-serif leading-none">ALPHA DENTAL</span>
        <span class="text-[9px] tracking-[0.18em] text-gold-accent font-semibold">INTERNATIONAL</span>
      </div>
    </a>"""

    blogs_html = blogs_html.replace(old_blogs_logo, new_blogs_logo)

    # Mobile Drawer Logo Section replacement in blogs.html
    old_blogs_drawer_logo = """      <div class="flex items-center justify-between pb-6 border-b border-border-color">
        <div class="flex items-center gap-2">
          <img src="logo_icon.png" alt="Alpha Dental Logo Icon" class="w-6 h-6 object-contain shrink-0"/>
          <span class="text-lg font-bold font-serif text-navy-dark">Alpha Dental International</span>
        </div>"""

    new_blogs_drawer_logo = """      <div class="flex items-center justify-between pb-6 border-b border-border-color">
        <div class="flex items-center gap-2.5">
          <img src="logo_icon.png" alt="Alpha Dental Logo" class="h-7 w-auto object-contain shrink-0"/>
          <div class="flex flex-col">
            <span class="text-sm font-bold tracking-wider text-navy-dark font-serif leading-none">ALPHA DENTAL</span>
            <span class="text-[8px] tracking-[0.18em] text-gold-accent font-semibold">INTERNATIONAL</span>
          </div>
        </div>"""

    blogs_html = blogs_html.replace(old_blogs_drawer_logo, new_blogs_drawer_logo)

    with open('blogs.html', 'w', encoding='utf-8') as f:
        f.write(blogs_html)
    print("blogs.html logo layout updated successfully!")


    # 3. Push changes to GitHub
    git_path = r"C:\Users\Sarthak\AppData\Local\GitHubDesktop\app-3.6.2\resources\app\git\cmd\git.exe"
    
    print("Staging changes...")
    subprocess.run([git_path, "add", "."])
    
    print("Committing changes...")
    res = subprocess.run([git_path, "commit", "-m", "Optimize logo size and remove box borders to place transparent logo directly left to the text"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    
    print("Pushing to GitHub remote repository...")
    res = subprocess.run([git_path, "push", "origin", "main"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)

if __name__ == '__main__':
    update_markup()
