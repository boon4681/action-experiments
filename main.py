import subprocess
import os

os.makedirs('./export',exist_ok=True)
os.chdir('./export')

with open('hi.txt','w') as f: 
    f.write('hi you.')

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
    'export'
], capture_output=True)
# subprocess.run(['git', 'config', 'user.name', 'actions-user'])
# subprocess.run(['git', 'config', 'user.email', 'actions@github.com'])

tags = subprocess.run(['git','remote'], capture_output=True).stdout.decode('utf-8').split('\n')
add_or_not = 'origin' in tags
# subprocess.run(['git', 'remote', 'set-url' if add_or_not else 'add' ,'origin',f'https://x-access-token:{os.getenv("github-token")}@github.com/{os.getenv("github-repository")}'])
subprocess.run(['git', 'remote', 'set-url' if add_or_not else 'add' ,'origin',f'https://github.com/boon4681/action-experiments.git'])

subprocess.run(['git', 'fetch', '-q', '--tags', 'origin', 'export'])
subprocess.run(['git', 'reset', '-q', '--hard', f'origin/export'])


subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-q', '-m', '🚀 boom burst the big bang'])
subprocess.run(['git', 'tag', '-f', 'export'])
subprocess.run(['git', 'push','-f','-q', '--tags', 'origin', 'export'])