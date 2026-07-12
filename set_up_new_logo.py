import os
import subprocess
from PIL import Image

def main():
    # 1. Load correct raw logo and process it to be transparent
    raw_logo_path = r"C:\Users\Sarthak\.gemini\antigravity\brain\912c5f96-9287-4a8c-a987-67aa47890241\media__1783848150715.png"
    img = Image.open(raw_logo_path)
    img = img.convert("RGBA")
    
    # Make background transparent
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] > 235 and item[1] > 235 and item[2] > 235:
            newData.append((255, 255, 255, 0)) # transparent
        else:
            newData.append(item)
            
    img_transparent = Image.new("RGBA", img.size)
    img_transparent.putdata(newData)
    
    # Crop to tight bounding box
    bbox = img_transparent.getbbox()
    if bbox:
        img_transparent = img_transparent.crop(bbox)
        
    # Save as new filename logo_blue_tooth.png to bypass browser caching
    new_logo_name = "logo_blue_tooth.png"
    img_transparent.save(new_logo_name, "PNG")
    print(f"Processed logo saved as {new_logo_name}!")
    
    # 2. Update index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace("logo_icon.png", new_logo_name)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html logo references updated to logo_blue_tooth.png!")
    
    # 3. Update blogs.html
    with open('blogs.html', 'r', encoding='utf-8') as f:
        blogs_html = f.read()
    blogs_html = blogs_html.replace("logo_icon.png", new_logo_name)
    with open('blogs.html', 'w', encoding='utf-8') as f:
        f.write(blogs_html)
    print("blogs.html logo references updated to logo_blue_tooth.png!")
    
    # 4. Clean up old files in workspace to avoid confusion
    for old_file in ["logo_icon.png", "logo_full.png"]:
        if os.path.exists(old_file):
            os.remove(old_file)
            print(f"Removed old file {old_file}")
            
    # 5. Git commit and push
    git_path = r"C:\Users\Sarthak\AppData\Local\GitHubDesktop\app-3.6.2\resources\app\git\cmd\git.exe"
    
    print("Staging changes...")
    subprocess.run([git_path, "add", "."])
    
    print("Committing changes...")
    res = subprocess.run([git_path, "commit", "-m", "Rename logo image to logo_blue_tooth.png to bypass browser cache issues"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    
    print("Pushing to GitHub remote repository...")
    res = subprocess.run([git_path, "push", "origin", "main"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)

if __name__ == '__main__':
    main()
