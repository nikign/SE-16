from shutil import copy
import subprocess

copy('rate_results.py', 'git-web/git-helper-2016/')
bashCommand = "cp -r GoogleSearch git-web/git-helper-2016/"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

# copy('rate_results.py', 'git_email_helper/')
# bashCommand = "cp -r GoogleSearch git_email_helper/ls"
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
