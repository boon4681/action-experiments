import subprocess
import os

os.mkdir('./export')
os.chdir('./export')

with open('hi.txt','w') as f: 
    f.write('hi you who see this.')

subprocess.run([
    'git',
    'init',
    '-q'
])
subprocess.run([
    'git', 
    'checkout', 
    '-q', 
    '-b', 
    'hi'
])
tags = subprocess.run(['git','remote','-v'], capture_output=True).stdout.decode('utf-8').split('\n')
add_or_not = 'origin' in tags
subprocess.run(['git', 'config', 'user.name', 'actions-user'])
subprocess.run(['git', 'remote', 'set-url' if add_or_not else 'add' ,'origin',f'https://x-access-token:{os.getenv("github-token")}@github.com/{os.getenv("github-repository")}'])
subprocess.run(['git', 'fetch', '-q', '--tags', 'origin', 'hi'])
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-q', '-m', '🚀 boom burst the big bang'])
subprocess.run(['git', 'tag', '-f', 'hi'])
subprocess.run(['git', 'push', '-f', '-q', '--tags', 'origin', 'TAGS:hi'])