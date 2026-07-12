import os
import subprocess
from PIL import Image

def process_logos():
    # 1. Process user's uploaded high-res logo
    user_logo_path = r"C:\Users\Sarthak\.gemini\antigravity\brain\912c5f96-9287-4a8c-a987-67aa47890241\media__1783848935434.png"
    img_user = Image.open(user_logo_path).convert("RGBA")
    
    # Make background transparent
    datas_user = img_user.getdata()
    newData_user = []
    for item in datas_user:
        if item[0] > 235 and item[1] > 235 and item[2] > 235:
            newData_user.append((255, 255, 255, 0))
        else:
            newData_user.append(item)
    img_user_trans = Image.new("RGBA", img_user.size)
    img_user_trans.putdata(newData_user)
    
    bbox_user = img_user_trans.getbbox()
    if bbox_user:
        img_user_trans = img_user_trans.crop(bbox_user)
        
    img_user_trans.save("logo_blue_tooth.png", "PNG")
    print("User high-res logo processed as logo_blue_tooth.png")
    
    # 2. Process AI recreated logo
    ai_logo_path = r"C:\Users\Sarthak\.gemini\antigravity\brain\912c5f96-9287-4a8c-a987-67aa47890241\recreated_tooth_logo_1783848970593.jpg"
    img_ai = Image.open(ai_logo_path).convert("RGBA")
    
    datas_ai = img_ai.getdata()
    newData_ai = []
    for item in datas_ai:
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData_ai.append((255, 255, 255, 0))
        else:
            newData_ai.append(item)
    img_ai_trans = Image.new("RGBA", img_ai.size)
    img_ai_trans.putdata(newData_ai)
    
    bbox_ai = img_ai_trans.getbbox()
    if bbox_ai:
        img_ai_trans = img_ai_trans.crop(bbox_ai)
        
    img_ai_trans.save("logo_recreated.png", "PNG")
    print("AI recreated logo processed as logo_recreated.png")
    
    # 3. Stage and push all changes to GitHub
    git_path = r"C:\Users\Sarthak\AppData\Local\GitHubDesktop\app-3.6.2\resources\app\git\cmd\git.exe"
    
    print("Staging files...")
    subprocess.run([git_path, "add", "."])
    
    print("Committing changes...")
    res = subprocess.run([git_path, "commit", "-m", "Process and place high-res user logo as logo_blue_tooth.png, and add logo_recreated.png"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    
    print("Pushing to GitHub remote repository...")
    res = subprocess.run([git_path, "push", "origin", "main"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)

if __name__ == '__main__':
    process_logos()
