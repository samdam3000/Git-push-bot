import os
import subprocess

def git_init_commit_push(repo_path, commit_message, remote_url):
    os.chdir(repo_path)
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "branch", "-M", "main"])
    subprocess.run(["git", "remote", "add", "origin", remote_url])
    subprocess.run(["git", "push", "-u", "origin", "main"])

if __name__ == "__main__":
    repo_path = os.path.abspath(".")
    commit_message = "Initial commit via Git Push Bot"
    remote_url = input("Enter your GitHub repo URL: ").strip()
    git_init_commit_push(repo_path, commit_message, remote_url)
