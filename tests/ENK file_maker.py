#TEST INDEX: 1
#NAME: .enk file creation and interpretation
#STATUS: USED - UPDATED

compatibleENKversions= ["1"]
MAGIC="ENKR"
ENKversion = "1"
encryptedData = "lihahpuzt4ß08zqghvufgdy,kcdgqßg08z"
encryptedDataLength = str(len(encryptedData))
lengthOfEncryptedDataLength = str(len(str(encryptedDataLength)))
packerlibrary = "azgq48q8taegoihybvyoiztz<r948g"
packerlibrarylength = str(len(packerlibrary))
lengthOfPackerlibrarylength=str(len(str(packerlibrarylength)))
content = MAGIC + ENKversion + lengthOfEncryptedDataLength + encryptedDataLength + lengthOfPackerlibrarylength + packerlibrarylength + encryptedData + packerlibrary
print(content)
def writefile():
    with open("file.enk","w") as file:
        file.write(content)
def readfile():
    with open("file.enk","r") as file:
        filecontent = file.read()
    if not filecontent.startswith("ENKR"):
        print("ERROR: file structure is invalid.")
    elif filecontent[4] not in compatibleENKversions:
        print(f"ERROR: File uses Wrong interpreter version. ({filecontent[4]})")
    else:
        try:
            lOFl=int(filecontent[5])
            print(f"len of len: {lOFl}")
        except ValueError:
            print("ERROR: file structure is invalid.")
            return
        encLen = filecontent[6:6+lOFl]
        print(f"length: {encLen}")
        
writefile()
readfile()
