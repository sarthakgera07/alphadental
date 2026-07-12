import os
import subprocess
from PIL import Image

def main():
    # Load generated logo image
    logo_path = r"C:\Users\Sarthak\.gemini\antigravity\brain\912c5f96-9287-4a8c-a987-67aa47890241\premium_dental_logo_1783848821976.jpg"
    img = Image.open(logo_path)
    img = img.convert("RGBA")
    
    # Make background transparent (white or close to white)
    datas = img.getdata()
    newData = []
    for item in datas:
        # Key out white pixels
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData.append((255, 255, 255, 0)) # transparent
        else:
            newData.append(item)
            
    img_transparent = Image.new("RGBA", img.size)
    img_transparent.putdata(newData)
    
    # Crop to tight bounding box
    bbox = img_transparent.getbbox()
    if bbox:
        img_transparent = img_transparent.crop(bbox)
        
    # Save as active logo filename
    new_logo_name = "logo_blue_tooth.png"
    img_transparent.save(new_logo_name, "PNG")
    print(f"Custom generated logo icon saved as {new_logo_name}!")
    
    # Push the updated logo to GitHub
    git_path = r"C:\Users\Sarthak\AppData\Local\GitHubDesktop\app-3.6.2\resources\app\git\cmd\git.exe"
    
    print("Staging changes...")
    subprocess.run([git_path, "add", "."])
    
    print("Committing changes...")
    res = subprocess.run([git_path, "commit", "-m", "Replace logo with custom generated premium modern dental icon"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    
    print("Pushing to GitHub remote repository...")
    res = subprocess.run([git_path, "push", "origin", "main"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)

if __name__ == '__main__':
    main()
