import os
import subprocess

def git_init_commit_push(repo_path, commit_message, github_token, github_repo_url):
    os.chdir(repo_path)
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "branch", "-M", "main"])

    # Add GitHub token directly into remote URL
    if github_token in github_repo_url:
        authenticated_url = github_repo_url
    else:
        authenticated_url = github_repo_url.replace("https://", f"https://{github_token}@")

    subprocess.run(["git", "remote", "add", "origin", authenticated_url])
    subprocess.run(["git", "push", "-u", "origin", "main"])

if __name__ == "__main__":
    repo_path = os.path.abspath(".")
    commit_message = os.getenv("COMMIT_MSG", "Auto commit via bot")
    github_token = os.getenv("GITHUB_TOKEN")
    github_repo_url = os.getenv("REMOTE_URL")

    if github_token and github_repo_url:
        git_init_commit_push(repo_path, commit_message, github_token, github_repo_url)
    else:
        print("Missing GITHUB_TOKEN or REMOTE_URL")