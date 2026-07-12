import subprocess
import os

def run_git():
    git_path = r"C:\Users\Sarthak\AppData\Local\GitHubDesktop\app-3.6.2\resources\app\git\cmd\git.exe"
    
    # 1. git init
    print("Running git init...")
    res = subprocess.run([git_path, "init"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    
    # 2. Check if remote origin already exists
    res = subprocess.run([git_path, "remote", "v"], capture_output=True, text=True)
    if "origin" in res.stdout:
        print("Remote origin already exists. Removing it...")
        subprocess.run([git_path, "remote", "remove", "origin"])
        
    # 3. git remote add origin
    print("Adding remote origin...")
    res = subprocess.run([git_path, "remote", "add", "origin", "https://github.com/sarthakgera07/alphadental.git"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    
    # 4. git add .
    print("Running git add...")
    res = subprocess.run([git_path, "add", "."], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    
    # 5. git commit
    print("Running git commit...")
    # Configure user name/email if not configured
    subprocess.run([git_path, "config", "user.name", "Sarthak Gera"])
    subprocess.run([git_path, "config", "user.email", "delhidentalclinicindia@gmail.com"])
    
    res = subprocess.run([git_path, "commit", "-m", "Initialize Alpha Dental website ready for Vercel deployment"], capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
    
    # 6. git branch -M main
    print("Setting branch to main...")
    subprocess.run([git_path, "branch", "-M", "main"])
    
    # 7. git push
    print("Running git push...")
    # We will try to push. If it prompts credentials, it might hang, so we'll run it with a timeout of 30 seconds
    try:
        res = subprocess.run([git_path, "push", "-u", "origin", "main", "-f"], capture_output=True, text=True, timeout=30)
        print("STDOUT:", res.stdout)
        print("STDERR:", res.stderr)
    except subprocess.TimeoutExpired:
        print("Git push timed out. This usually means GitHub requires authentication. Please use GitHub Desktop to push, or we can configure a token.")

if __name__ == '__main__':
    run_git()
