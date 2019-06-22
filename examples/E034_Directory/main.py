# Example 034: Directory

import os

cwd = os.getcwd()
cwdb = os.getcwdb()

print('cwd: ', cwd)
print('cwdb: ', cwdb)

print('type(cwd): ', type(cwd))
print('type(cwdb): ', type(cwdb))

os.chdir("/home/mert/Desktop")
print(os.getcwd())

print(os.listdir())
os.mkdir('PythonTest')
print()
print(os.listdir())
os.rename('PythonTest', 'PyTest')
print()

os.chdir(cwd)
os.remove('text.txt')
os.rmdir('folder')
# Or shutil.rmtree('folder')
