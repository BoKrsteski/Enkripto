snaps = []
prompt = 'decode msg = "hi how are you, because im doin great" , msg = "ahh, thats great to hear! mee too!"'
for i in range(len(prompt)):
    if prompt[i] == '''"''':
        snaps.append(i)
print(snaps)
print(len(snaps))
newprompt = prompt
deletedCharacters = 0
allcontents= []
while len(snaps) > 1:
    content = prompt[:snaps[1]][snaps[0]+1:]
    deletedCharactersSnap = len(newprompt[:snaps[1]+1 - deletedCharacters][snaps[0]-deletedCharacters:])
    print(newprompt[:snaps[1]+1-deletedCharacters][snaps[0]-deletedCharacters:])
    print(deletedCharactersSnap)
    newprompt = newprompt[:snaps[0] - deletedCharacters] + newprompt[snaps[1]+1 - deletedCharacters:]
    deletedCharacters = deletedCharactersSnap
    snaps.remove(snaps[0])
    snaps.remove(snaps[0])
    allcontents.append(content)
print("contents: "+ " , ".join(allcontents))
params = newprompt.replace(" ","").split(",")
for i in range(len(params)):
    if "msg=" in params[i]:
        print("this:" + params[i])
        params[i] = params[i] + allcontents[0]
        allcontents.remove(allcontents[0])
print(params)
print(newprompt)