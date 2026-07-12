import subprocess

def main():
    # 1. Update index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Target: index.html Header container replacement
    old_index_header = '<header class="sticky top-0 z-40 bg-navy-dark text-white px-4 md:px-8 py-3.5 flex items-center justify-between border-b border-border-color/10 shadow-lg">'
    new_index_header = '<header class="sticky top-0 z-40 bg-navy-dark text-white px-2.5 sm:px-4 md:px-8 py-3 flex items-center justify-between border-b border-border-color/10 shadow-lg">'
    html = html.replace(old_index_header, new_index_header)

    # Target: index.html Logo anchor block
    old_index_logo = """    <a href="#" class="flex items-center gap-2.5 group shrink-0">
      <img src="logo_blue_tooth.png" alt="Alpha Dental Logo" class="h-8 w-auto object-contain transition-transform group-hover:scale-105 shrink-0"/>
      <div class="flex flex-col">
        <span class="text-base md:text-lg font-bold tracking-wider text-white font-serif leading-none">ALPHA DENTAL</span>
        <span class="text-[9px] tracking-[0.18em] text-gold-accent font-semibold">INTERNATIONAL</span>
      </div>
    </a>"""

    new_index_logo = """    <a href="#" class="flex items-center gap-1.5 sm:gap-2.5 group shrink-0">
      <img src="logo_blue_tooth.png" alt="Alpha Dental Logo" class="h-7 sm:h-8 w-auto object-contain transition-transform group-hover:scale-105 shrink-0"/>
      <div class="flex flex-col">
        <span class="text-sm sm:text-base md:text-lg font-bold tracking-wider text-white font-serif leading-none">ALPHA DENTAL</span>
        <span class="text-[8px] sm:text-[9px] tracking-[0.12em] sm:tracking-[0.18em] text-gold-accent font-semibold">INTERNATIONAL</span>
      </div>
    </a>"""

    html = html.replace(old_index_logo, new_index_logo)

    # Target: index.html Header actions container gap
    old_index_actions = '<div class="flex items-center gap-5">'
    new_index_actions = '<div class="flex items-center gap-2 sm:gap-5">'
    html = html.replace(old_index_actions, new_index_actions)

    # Target: index.html Book Now button
    old_index_btn = """      <a href="#scheduler" class="bg-navy-blue hover:bg-navy-dark border border-gold-accent/30 hover:border-gold-accent text-white px-3.5 sm:px-5 py-2.5 rounded-md text-xs font-bold flex items-center gap-2 transition-all shadow-md hover:shadow-lg shrink-0" aria-label="Book Appointment">
        <i class="fa-solid fa-calendar-days text-gold-accent text-sm"></i>
        <span class="hidden sm:inline">BOOK NOW</span>
      </a>"""

    new_index_btn = """      <a href="#scheduler" class="bg-navy-blue hover:bg-navy-dark border border-gold-accent/30 hover:border-gold-accent text-white px-2 sm:px-4 py-2 rounded-md text-[10px] sm:text-xs font-bold flex items-center gap-1.5 sm:gap-2 transition-all shadow-md hover:shadow-lg shrink-0">
        <i class="fa-solid fa-calendar-days text-gold-accent text-[11px] sm:text-sm"></i>
        <span>BOOK NOW</span>
      </a>"""

    html = html.replace(old_index_btn, new_index_btn)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html responsive spacing updated successfully!")


    # 2. Update blogs.html
    with open('blogs.html', 'r', encoding='utf-8') as f:
        blogs_html = f.read()

    # Target: blogs.html Header container replacement
    old_blogs_header = '<header class="sticky top-0 z-40 bg-white/75 backdrop-blur-lg px-4 md:px-8 py-3.5 flex items-center justify-between border-b border-border-color/60 shadow-[0_2px_15px_rgba(0,0,0,0.015)]">'
    new_blogs_header = '<header class="sticky top-0 z-40 bg-white/75 backdrop-blur-lg px-2.5 sm:px-4 md:px-8 py-3 flex items-center justify-between border-b border-border-color/60 shadow-[0_2px_15px_rgba(0,0,0,0.015)]">'
    blogs_html = blogs_html.replace(old_blogs_header, new_blogs_header)

    # Target: blogs.html Logo anchor block
    old_blogs_logo = """    <a href="#" class="flex items-center gap-2.5 group shrink-0">
      <img src="logo_blue_tooth.png" alt="Alpha Dental Logo" class="h-8 w-auto object-contain transition-transform group-hover:scale-105 shrink-0"/>
      <div class="flex flex-col">
        <span class="text-base md:text-lg font-bold tracking-wider text-navy-dark font-serif leading-none">ALPHA DENTAL</span>
        <span class="text-[9px] tracking-[0.18em] text-gold-accent font-semibold">INTERNATIONAL</span>
      </div>
    </a>"""

    new_blogs_logo = """    <a href="#" class="flex items-center gap-1.5 sm:gap-2.5 group shrink-0">
      <img src="logo_blue_tooth.png" alt="Alpha Dental Logo" class="h-7 sm:h-8 w-auto object-contain transition-transform group-hover:scale-105 shrink-0"/>
      <div class="flex flex-col">
        <span class="text-sm sm:text-base md:text-lg font-bold tracking-wider text-navy-dark font-serif leading-none">ALPHA DENTAL</span>
        <span class="text-[8px] sm:text-[9px] tracking-[0.12em] sm:tracking-[0.18em] text-gold-accent font-semibold">INTERNATIONAL</span>
      </div>
    </a>"""

    blogs_html = blogs_html.replace(old_blogs_logo, new_blogs_logo)

    # Target: blogs.html Header actions container gap
    old_blogs_actions = '<div class="flex items-center gap-3">'
    new_blogs_actions = '<div class="flex items-center gap-1.5 sm:gap-3">'
    blogs_html = blogs_html.replace(old_blogs_actions, new_blogs_actions)

    # Target: blogs.html Book Now button
    old_blogs_btn = """      <a href="index.html#scheduler" class="bg-gold-accent hover:bg-gold-hover text-white px-3.5 sm:px-5 py-2.5 rounded-md text-xs font-bold flex items-center gap-2 transition-all shadow-md hover:shadow-lg shrink-0" aria-label="Book Appointment">
        <i class="fa-solid fa-calendar-days text-sm"></i>
        <span class="hidden sm:inline">Book Now</span>
      </a>"""

    new_blogs_btn = """      <a href="index.html#scheduler" class="bg-gold-accent hover:bg-gold-hover text-white px-2 sm:px-4 py-2 rounded-md text-[10px] sm:text-xs font-bold flex items-center gap-1.5 sm:gap-2 transition-all shadow-md hover:shadow-lg shrink-0">
        <i class="fa-solid fa-calendar-days text-[11px] sm:text-sm"></i>
        <span>Book Now</span>
      </a>"""

    blogs_html = blogs_html.replace(old_blogs_btn, new_blogs_btn)

    with open('blogs.html', 'w', encoding='utf-8') as f:
        f.write(blogs_html)
    print("blogs.html responsive spacing updated successfully!")


    # 3. Git push
    git_path = r"C:\Users\Sarthak\AppData\Local\GitHubDesktop\app-3.6.2\resources\app\git\cmd\git.exe"
    
    print("Staging changes...")
    subprocess.run([git_path, "add", "."])
    
    print("Committing changes...")
    res = subprocess.run([git_path, "commit", "-m", "Refine mobile header spacing: fit BOOK NOW text inline on all viewport widths"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    
    print("Pushing to GitHub remote repository...")
    res = subprocess.run([git_path, "push", "origin", "main"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)

if __name__ == '__main__':
    main()
