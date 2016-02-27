from colorama import init
from colorama import Fore, Back, Style
import constant
##############################################################
# Functions
##############################################################
# Provide solution with decision tree
def provideSolution(cmd, msg):
    print(constant.solutionLogo)
    
    gitcmd = getGitCommandName(cmd)
    
    if solutionAvailableCommands.has_key(gitcmd):
        solutionAvailableCommands[gitcmd](msg)
    else:
        raise NotImplementedError('solution for other commands has not implemented yet.')
    return

# get git command name from a git command
def getGitCommandName(cmd):
    if cmd == 'git':
        return 'git'
    rmgit = cmd[cmd.find(' '):].lstrip()
    end = rmgit.find(' ')
    if end == -1:
        return rmgit
    else:
        return rmgit[:rmgit.find(' ')]

# Print formated solution
# explanation: str; command: list; solution: list
def printSolution(explanation, command, solution):
    if explanation != '':
        print(Fore.GREEN + 'Explanation:' + Style.RESET_ALL)
        print
        print('\t' + explanation)
        print
    if command != '':
        print(Fore.GREEN + 'Command:' + Style.RESET_ALL)
        print
        i = 1
        for value in command:
            print('\t' + str(i) + '. ' + Style.DIM + value + Style.RESET_ALL)
            print
            i += 1
    if solution != '':
        print(Fore.GREEN + 'Solution:' + Style.RESET_ALL)
        print
        i = 1
        for value in solution:
            print('\t' + str(i) + '. ' + value)
            print    
    print

##############################################################
# Solutions
##############################################################
# Provide solution for Push Command
def providePushSolution(msg):
    explanation = ''
    solution = ''    
    command = ''
    try:
        #raise NotImplementedError('solution for push command has not been implemented yet')
        if msg.find('[rejected]') > 0 and msg.find('failed to push some refs to') > 0 and (msg.find('(fetch first)') > 0 or msg.find('(non-fast-forward)')):
            explanation = 'The remote server has some work that you do not have on your local machine. You can do a git pull command to get the work you do not have locally.'
            command = ['git pull']
            solution = ["Please use " + Style.DIM + command[0] + Style.RESET_ALL + " command to get the work that you don't have locally."]
        elif msg.find('src refspec') > 0 and msg.find('does not match any') > 0:
            begin = msg.find('src refspec') + len('src refspec')
            end = msg.find('does not match any')
            branchName = msg[begin:end].lstrip().rstrip()
            explanation = 'You get this message most likely because git will not let you to push a completely empty repository to ' + branchName + ' branch. You will at least need to have one file inside your local repository (folder), then add, commit and push.' 
            command = ['git add <file-name>', 
                        'git commit -m "Your commit message here"', 
                        'git push origin ' + branchName]
            solution = ['Make sure you have at least one file in your repository folder.',
                        'Use ' + Style.DIM + command[0] + ' to add files into this commit. Use "." or "-A" for <file-name> if you want to add all files in the repository to this commit.',
                        'Use ' + Style.DIM + command[1] + ' to commit to local repository.',
                        'Use ' + Style.DIM + command[2] + ' to push you commit to ' + branchName + ' of remote repository.']
        else:
            explanation = constant.noSolutionMessage
            solution = constant.noSolutionSolution
        printSolution(explanation,command,solution)
    except Exception as e:
        print('Error in providePushSolution():')
        print(e)
    return

##############################################################
# Constant
##############################################################
# Git commands and their solution provider function
solutionAvailableCommands = {
    'push': providePushSolution
    
}
