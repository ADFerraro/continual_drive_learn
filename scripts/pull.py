import os
import subprocess
import argparse

repository_path = '~/Desktop/Tesi/code/continual_drive_learn/'

parser = argparse.ArgumentParser(description="Pull git repository and docker image")
parser.add_argument(
    "-r",
    "--run",
    action="store_true",
    help="run the image inside a container",
)

def git_pull(repo_path):
    if os.path.isdir(os.path.expanduser(repo_path)):
        try:
            subprocess.run(['git', '-C', os.path.expanduser(repo_path), 'pull'], check=True)
            print(f'Succesfully pulled updates in {repo_path}')
        except subprocess.CalledProcessError as e:
            print(f'Error pulling updates in {repo_path}: {e}')
    else:
        print(f'Error: {repo_path} is not a valid directory')

def docker_pull():
    try:
        subprocess.run(['docker', 'pull', 'adferraro/continual_drive'], check=True)
        print(f'Succesfully pulled image')
     except subprocess.CalledProcessError as e:
        print(f'Error pulling docker image: {e}')


git_pull(repository_path)
docker_pull()
if args.run:
    try:
        p = subprocess.Popen(['docker', 'run','--name','testcontainer', '-it', 'adferraro/continual_drive'], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Error running container: {e}')
    except KeyboardInterrupt:
        p.kill()
        os.exit()

