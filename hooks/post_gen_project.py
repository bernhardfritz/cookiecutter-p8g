import os
import shutil
import subprocess
import sys

initialized_git = subprocess.call(['git', 'init'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) == 0
if initialized_git:
    print()
    print('Initialized a git repository.')
else:
    print('Git repo not initialized')
if subprocess.call(['{{ cookiecutter.package_manager }}', 'install']):
    sys.exit('`{{ cookiecutter.package_manager }} install` failed')
if initialized_git:
    try:
        subprocess.check_call(['git', 'add', '-A'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        subprocess.check_call(['git', 'commit', '-m', 'Initialize project using cookiecutter-p8g'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        subprocess.check_call(['git', 'branch', '-M', 'main'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print()
        print('Created git commit.')
    except:
        print('Git commit not created')
        print('Removing .git directory...')
        shutil.rmtree('.git', True)
print()
print('Success! Created {{ cookiecutter.project_name }} at {}'.format(
    os.getcwd()))
print('Inside that directory, you can run several commands:')
print()
print('  {{ cookiecutter.package_manager }} {}dev'.format(
    '' if '{{ cookiecutter.package_manager }}' == 'yarn' else 'run '))
print('    Starts the development server.')
print()
print('  {{ cookiecutter.package_manager }} {}build'.format(
    '' if '{{ cookiecutter.package_manager }}' == 'yarn' else 'run '))
print('    Bundles the app into static files for production.')
print()
print('  {{ cookiecutter.package_manager }} {}preview'.format(
    '' if '{{ cookiecutter.package_manager }}' == 'yarn' else 'run '))
print('    Previews the production build locally.')
print()
print('We suggest that you begin by typing:')
print('  cd {{ cookiecutter.project_slug }}')
print('  {{ cookiecutter.package_manager }} {}dev'.format(
    '' if '{{ cookiecutter.package_manager }}' == 'yarn' else 'run '))
print()
print('Happy hacking!')
