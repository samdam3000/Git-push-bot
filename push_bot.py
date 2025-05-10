import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

def git_init_commit_push():
    repo_path = os.path.abspath(".")
    commit_message = os.getenv("COMMIT_MSG", "Auto commit via Git Bot")
    github_token = os.getenv("GITHUB_TOKEN")
    github_repo_url = os.getenv("REMOTE_URL")

    if not github_token or not github_repo_url:
        return "Missing GITHUB_TOKEN or REMOTE_URL"

    os.chdir(repo_path)
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "branch", "-M", "main"])
    authenticated_url = github_repo_url.replace("https://", f"https://{github_token}@")
    subprocess.run(["git", "remote", "add", "origin", authenticated_url])
    subprocess.run(["git", "push", "-u", "origin", "main"])

    return "Push complete"

if __name__ == "__main__":
    print(git_init_commit_push())