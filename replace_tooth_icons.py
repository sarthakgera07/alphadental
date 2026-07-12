import subprocess

def replace_icons():
    # Define replacements for index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Header Logo icon replacement
    old_header_icon = '<i class="fa-solid fa-tooth text-2xl transition-transform group-hover:scale-110"></i>'
    new_header_icon = '<img src="logo_icon.png" alt="Alpha Dental Logo Icon" class="w-7 h-7 object-contain transition-transform group-hover:scale-110"/>'
    html = html.replace(old_header_icon, new_header_icon)

    # Mobile Drawer icon replacement
    old_drawer_icon = '<i class="fa-solid fa-tooth text-gold-accent text-2xl"></i>'
    new_drawer_icon = '<img src="logo_icon.png" alt="Alpha Dental Logo Icon" class="w-6 h-6 object-contain shrink-0"/>'
    html = html.replace(old_drawer_icon, new_drawer_icon)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html logo icons successfully updated!")


    # Define replacements for blogs.html
    with open('blogs.html', 'r', encoding='utf-8') as f:
        blogs_html = f.read()

    # Header Logo icon replacement in blogs.html
    blogs_old_header = '<i class="fa-solid fa-tooth text-2xl transition-transform group-hover:scale-110"></i>'
    blogs_new_header = '<img src="logo_icon.png" alt="Alpha Dental Logo Icon" class="w-7 h-7 object-contain transition-transform group-hover:scale-110"/>'
    blogs_html = blogs_html.replace(blogs_old_header, blogs_new_header)

    # Mobile Drawer icon replacement in blogs.html
    blogs_old_drawer = '<i class="fa-solid fa-tooth text-gold-accent text-2xl"></i>'
    blogs_new_drawer = '<img src="logo_icon.png" alt="Alpha Dental Logo Icon" class="w-6 h-6 object-contain shrink-0"/>'
    blogs_html = blogs_html.replace(blogs_old_drawer, blogs_new_drawer)

    with open('blogs.html', 'w', encoding='utf-8') as f:
        f.write(blogs_html)
    print("blogs.html logo icons successfully updated!")


    # Push changes to GitHub
    git_path = r"C:\Users\Sarthak\AppData\Local\GitHubDesktop\app-3.6.2\resources\app\git\cmd\git.exe"
    
    print("Staging changes...")
    subprocess.run([git_path, "add", "."])
    
    print("Committing changes...")
    res = subprocess.run([git_path, "commit", "-m", "Replace generic FontAwesome tooth icons with custom transparent logo icon"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    
    print("Pushing to GitHub remote repository...")
    res = subprocess.run([git_path, "push", "origin", "main"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)

if __name__ == '__main__':
    replace_icons()
