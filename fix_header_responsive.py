import subprocess

def main():
    # 1. Update index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Logo anchor tag in index.html - add shrink-0
    old_logo_anchor = '<a href="#" class="flex items-center gap-2.5 group">'
    new_logo_anchor = '<a href="#" class="flex items-center gap-2.5 group shrink-0">'
    html = html.replace(old_logo_anchor, new_logo_anchor)
    
    # Book Now button in index.html - responsive collapse
    old_book_btn = """      <a href="#scheduler" class="bg-navy-blue hover:bg-navy-dark border border-gold-accent/30 hover:border-gold-accent text-white px-5 py-2.5 rounded-md text-xs font-bold flex items-center gap-2 transition-all shadow-md hover:shadow-lg">
        <span>BOOK NOW</span>
      </a>"""
      
    new_book_btn = """      <a href="#scheduler" class="bg-navy-blue hover:bg-navy-dark border border-gold-accent/30 hover:border-gold-accent text-white px-3.5 sm:px-5 py-2.5 rounded-md text-xs font-bold flex items-center gap-2 transition-all shadow-md hover:shadow-lg shrink-0" aria-label="Book Appointment">
        <i class="fa-solid fa-calendar-days text-gold-accent text-sm"></i>
        <span class="hidden sm:inline">BOOK NOW</span>
      </a>"""
      
    html = html.replace(old_book_btn, new_book_btn)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html responsive header actions updated successfully!")
    
    # 2. Update blogs.html
    with open('blogs.html', 'r', encoding='utf-8') as f:
        blogs_html = f.read()
        
    # Logo anchor tag in blogs.html - add shrink-0
    old_blogs_logo_anchor = '<a href="#" class="flex items-center gap-2.5 group">'
    new_blogs_logo_anchor = '<a href="#" class="flex items-center gap-2.5 group shrink-0">'
    blogs_html = blogs_html.replace(old_blogs_logo_anchor, new_blogs_logo_anchor)
    
    # Book Now button in blogs.html - responsive collapse
    old_blogs_book_btn = """      <a href="index.html#scheduler" class="bg-gold-accent hover:bg-gold-hover text-white px-5 py-2.5 rounded-md text-xs font-bold flex items-center gap-2 transition-all shadow-md hover:shadow-lg">
        <i class="fa-solid fa-calendar-days text-sm"></i>
        <span>Book Now</span>
      </a>"""
      
    new_blogs_book_btn = """      <a href="index.html#scheduler" class="bg-gold-accent hover:bg-gold-hover text-white px-3.5 sm:px-5 py-2.5 rounded-md text-xs font-bold flex items-center gap-2 transition-all shadow-md hover:shadow-lg shrink-0" aria-label="Book Appointment">
        <i class="fa-solid fa-calendar-days text-sm"></i>
        <span class="hidden sm:inline">Book Now</span>
      </a>"""
      
    blogs_html = blogs_html.replace(old_blogs_book_btn, new_blogs_book_btn)
    
    with open('blogs.html', 'w', encoding='utf-8') as f:
        f.write(blogs_html)
    print("blogs.html responsive header actions updated successfully!")
    
    # 3. Git commit and push
    git_path = r"C:\Users\Sarthak\AppData\Local\GitHubDesktop\app-3.6.2\resources\app\git\cmd\git.exe"
    
    print("Staging changes...")
    subprocess.run([git_path, "add", "."])
    
    print("Committing changes...")
    res = subprocess.run([git_path, "commit", "-m", "Optimize header responsive layout: collapse Book Now button text on mobile to avoid logo collision"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    
    print("Pushing to GitHub remote repository...")
    res = subprocess.run([git_path, "push", "origin", "main"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)

if __name__ == '__main__':
    main()
