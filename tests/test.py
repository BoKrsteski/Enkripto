#TEST INDEX: 0
#NAME: string catching, snapshotting and concatenating
#STATUS: USED - ACTIVE

snaps = []
prompt = 'decode msg = "hi how are you, because im doin great" , msg = "ahh, thats great to hear! me too!"'
for i in range(len(prompt)):
    if prompt[i] == '''"''':
        snaps.append(i)
if debug:
    print(snaps)
    print(len(snaps))
newprompt = prompt
deletedCharacters = 0
allcontents= []
while len(snaps) > 1:
    content = prompt[:snaps[1]][snaps[0]+1:]
    deletedCharactersSnap = len(newprompt[:snaps[1]+1 - deletedCharacters][snaps[0]-deletedCharacters:])
    if debug:
        print(newprompt[:snaps[1]+1-deletedCharacters][snaps[0]-deletedCharacters:])
        print(deletedCharactersSnap)
    newprompt = newprompt[:snaps[0] - deletedCharacters] + newprompt[snaps[1]+1 - deletedCharacters:]
    deletedCharacters = deletedCharactersSnap
    del snaps[:2]
    allcontents.append(content)
if debug:
    print("contents: "+ " , ".join(allcontents))
    print(newprompt)
params = newprompt.replace(" ","").split(",")
for i in range(len(params)):
    if "msg=" in params[i]:
        if debug:
            print("this:" + params[i])
        params[i] = params[i] + allcontents[0]
        allcontents.remove(allcontents[0])
print(params)
