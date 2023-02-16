import time, os
from datetime import datetime
'''
1. Simple script to run tests until failure
2. Make sure Fiddler's execaction.exe is in your PATH
3. Update delayInSeconds and testcmds to suit
4. Customize testcmds array to suit
'''

fclear = 'execaction.exe clear'
fstart = 'execaction.exe start'
fstop = 'execaction.exe stop'
delayInSeconds = 1 * 60 * 60

# customize to suit
testcmds = [
    'npx playwright test -c playwright/config/playwright.config.ts tests/unit/unit.e2e-spec.ts -g t0 --headed',
]

def getindex(max):
    while(True):
        for i in range(0, max):
            yield i

count = 0
setlength = len(testcmds)
# os.system(fstart)
# os.system(fclear)
for i in getindex(setlength):
    print(f'--- Set: {count // setlength} Run: {count} {datetime.now()}', flush=True)
    pwcmd = testcmds[i]
    print(f'    cmd: {pwcmd }', flush=True)
    status = os.system(pwcmd)
    count += 1
    if ( status == 0 ) :
        print('aok', flush=True)
        # os.system(fclear)
    else :
       break
    time.sleep(delayInSeconds)
    # if i == 8 :
        # os.system(fstop)
# os.system(fstop)

