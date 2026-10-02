import random
import os
import sys
import json
import time
import traceback

YELLOW = "\033[93m"
GREEN = "\033[1;92m"
PROMPTPINK = "\033[1;95m"
RESET = "\033[0m"
RED = "\033[91m"
BLUE = "\033[96m"
GREY = "\033[38;2;143;163;191m"
DIRBLUE = "\033[38;2;91;158;230m"
DIRRED = "\033[38;2;230;168;91m"
# TODO documentation for mktxt & showprefs
#AQcreator. last function in regs!!!!!!!!

if os.name == "nt":
    os.system("mode con: cols=120 lines=100")
else:
    os.system("printf '\\033[8;100;120t'")
def fetchPreferences(withStatus: bool = False):
    global Preferences
    preferenceIdol = ["Default.enk",1,0]
    try:
        print(BLUE+"fetching preferences..."+RESET)
        with open("preferences.json","r") as file:
            Preferences = json.load(file)
    except FileNotFoundError:
        print(YELLOW + "WARNING: no preferences.json found. Creating new with default values..." + RESET)
        with open("preferences.json","w") as file:
            json.dump({"filelocation":"Default.enk",
                    "createnew": 1,
                    "readfromENK": 0},file,indent=4)
            Preferences = {"filelocation":"Default.enk",
                        "createnew": 1,
                        "readfromENK": 0}
    except json.JSONDecodeError:
            print(YELLOW + "WARNING: no preferences.json contains invalid JSON. restoring default values..." +RESET)
            with open("preferences.json","w") as file:
                json.dump({"filelocation":"Default.enk",
                        "createnew": 1,
                        "readfromENK": 0},file,indent=4)
                Preferences = {"filelocation":"Default.enk",
                            "createnew": 1,
                            "readfromENK": 0}
    def defaultpref():
        global preference
        print(RED+"FATAL WARNING: invalid preferences.json provided. Setting default values..."+RESET)
        with open("preferences.json","w") as file:
            json.dump({"filelocation":"Default.enk",
                    "createnew": 1,
                    "readfromENK": 0},file,indent=4)
            preference = preferenceIdol
    if len(Preferences) == 3:
        preference = Preferences.values()
    else:
        defaultpref()
    indexCounter=0
    for i in preference:
        indexCounter +=1
        if indexCounter == 1:
            global fileLocation
            if i.endswith(".enk"):
                fileLocation = i
            else:
                print(YELLOW+f"WARNING: invalid preference '{i}'. Using default value..."+RESET)
                with open("preferences.json","w") as file:
                    Preferences["filelocation"] = "Default.enk"
                    json.dump(Preferences,file,indent=4)
                fileLocation = "Default.enk"
        elif indexCounter ==2 or indexCounter==3:
            global readFromENK
            global createNew
            if i == 1 or i==0:
                if indexCounter==2:
                    createNew = bool(int(i))
                else:
                    readFromENK=bool(int(i))
            else:
                print(YELLOW+f"WARNING: invalid preference '{i}'. Using default value..."+RESET)
                if indexCounter==2:
                    with open("preferences.json","w") as file:
                        Preferences["createnew"] = 1
                        json.dump(Preferences,file,indent=4)
                    createNew = True
                else:
                    print(YELLOW+f"WARNING: invalid preference '{i}'. Using default value..."+RESET)
                    with open("preferences.json","w") as file:
                        Preferences["readfromENK"] = 0
                        json.dump(Preferences,file,indent=4)
                    readFromENK=False
    if withStatus:
        print(GREY+"preferences:\n"+GREEN+f"{" , ".join(Preferences)}"+RESET)
    else:
        print(GREEN+"preferences imported!"+RESET)


normallibrary=r"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ß!§$%&/\()?`+*~#'<>|²³"}]{[.-;_: =@"""
throwawaylibrary=normallibrary
library:str=""
compatibleENKversions= ["1"]

def intro():
    print(RED + r'''
                             s@S$$S@s                    ,@S$$S.               s@S$$S@s                    
      ,sS$S@go_              $$$$$$$'       ,sS$S@S$s,_  $$$$$$$    ,sS$S@go,  $$$$$$$'         ,sS$S@go,  
    ,s$$$$$$$$$$,sS$S@S$s,_  `$$$$$'  .,$$$$$$$$$  o$$$s,`$$$$P'  ,s$$$$$$$$$, `$$$$$,        ,s$$$$$$$$$, 
    $$$$$' )$$$s$$$$$  $$$$s, $$$$$  $$$$$²'$$$$l `$$$$$P         $$$$$$l$$$$s $$$$$$%S$S;    $$$$$$l$$$$s 
    $$$$' o$$$P'$$$$l   `$$$$ $$$$$%$s²"`_  $$$$$  `"""" od$$$bo. $$$$l' `$$$$,`$$$$$"²╙'     $$$$l' `$$$$,
    $$$$,$"'"   $$$$$   ,$$$$ $$$$iP²╙$$$$$,$$$$$$       .l$$$i   $$$$$   $$$$$ l$$$i         $$$$,   $$$$$
    $$$$$s.,$$$$$$$$$$  $$$$$ $$$$$   `$$$$$$$$$$$       $$$$$$,o.$$$$$ .,$$$$  $$$$$, _,b$$$$$$$$$s.,$$$$ 
    `²$$$$$$$²' `²$$$  $$$$$ $$$$$   ,$$$$$`$²$$$       4$$$$$$b)$$$$$ $$$$²'  $$$$$$Sb$$$$$' `²$$$$$$$²' 
        `"²"`           `²$ⁿ' `²$$$  ,$$$$$'  `""         `4$$$$" $$$$$ `$`     `²$²"^²$$$²'      `"²"`    
                                     gV$$²'                       $$$$$                                    
                                                                  $$$$$                                    
                                                                  $$$$$                                     ''' + RESET)
    print(BLUE+"-- ENKRIPTO v2.3.4 --\n"+GREY+"type 'help' to see a list of commands or a command's function"+RESET)
    if debug:
        print(YELLOW+"WARNING: debug active!"+RESET)
#TODO CHANGE VERSION NAME WITH EACH UPDATE DUDE

#MADE BY A SINGLE DUDE - EXPECT BUGS - ALTHOUGH I HAVEN'T SEEN ANY


                    ###############
                    # DICTIONARY: #
                    ###############

# seed: the seed is a series of numbers that indicate procedures and parameters for the script to replicate the original circumstances. This way, the same en/decoding scheme can be used on different devices and/or instances.
# pack : packing refers to the extra encryption of the seed. it is encrypted (with a custom or default) library and then shuffled (by a custom or random amount). these are extra safety measures to allow the seed to be transferred safely
# library-layers : library-layers are shuffled versions of the alphabet ; An indefinite amount of them can be created, with each one of them encrypting itself using the previous one's properties. The last created layer is always the library that will be used for the main en-/de-coding.



                        ###########
                        # PARAMS: #
                        ###########

# createNew:  if True, creates new seed. readFromENK,custom_Packer, importseed and seed_ispacked will be ignored, as these functions are used for importing existing seeds.
# readFromENK: if you have an .enk file containing your data, enable this. otherwhise disable.
# custom_PackerLibrary: only used if readFromtx = False, custom library that was used to pack this seed
# importseed: only used if readFromtx = False ; the seed you used, if it is packed, enable seed_ispacked. otherwhise disable.  A packed seed looks like this :  11QT'`V>'`TQV[>nQ[Vn    ; An unpacked seed looks like this:   902138.231.2079187
# seed_ispacked: set to true if the seed you provided is packed, otherwhise set to false
# encryptionamount: amount of encryption layers
# PackMySeed: if True, packs the seed before displaying. set this to True if you want an extra layer of encryption. This will encrypt and shuffle the seed with a custom or default library. if false, displays pure seed


custom_PackerLibrary: str = r""
importseed: str = r""
seed_ispacked: bool = True
encryptionamount: int =random.randint(100,500) 
packMySeed: bool = True
packerLibrary = None

debug = False
if __name__ == "__main__" and not getattr(sys, "frozen", False):
    debug = True
# used to exit upon self-raised errors
def StopFunc(func: str):
    print(YELLOW+f"'{func}' Function execution aborted."+RESET)

# use this to either reset or create the txt file with default values
def resetFile():
    with open(fileLocation,"w",encoding="utf-8") as file:
        file.write(createLibrary(normallibrary,random.randint(1,9999999), "None"))
    print(GREEN+"file reset"+RESET)

# restores correct order in packed seeds.
def cleanse(providedSeed):
        cleanedSeed = ""
        try:
            formatter = int(providedSeed[:2])
        except ValueError:
            print(RED+"ERROR in Cleanse() ; invalid seed imported"+RESET)
            return None
        rest = (providedSeed[2:])
        for u in range(formatter):
            rest = rest[-1] + rest[:-1]
        cleanedSeed = rest
        return cleanedSeed

#this function is called by makeLibrary() to create each commercial and initial layer(s)
def createLibrary(factor, seed1, state):
    throwawaylibrary=factor
    seedCreator=""
    random.seed(seed1)
    while len(seedCreator) < len(normallibrary):
        randomLetter=throwawaylibrary[random.randint(0,len(throwawaylibrary)-1)]
        throwawaylibrary = throwawaylibrary.replace(randomLetter, "")
        seedCreator += randomLetter
    if state == "init":
        global initseed
        initseed = seed1
    elif state == "commercial":
        global commercialseed
        commercialseed = seed1
    return seedCreator

#this function encrypts/decodes your messages!
#hellz yeah
def execute(method:str ="encrypt", message:str = "lorem ipsum", library:str = createLibrary(normallibrary,random.randint(1,9999999), "None"), outputMode:bool = False):
    if method == "encrypt":
        encrypted_message = ""
        if outputMode:
            print(GREY+"provided message to encrypt:"+RESET)
            print(DIRBLUE+message+RESET)
        if debug:
            print(normallibrary)
        for i in message:
            try:
                location = normallibrary.index(i)
            except ValueError:
                return print(RED+f"ERROR: the Enkripto library currently does not support use of the character '{i}'. Please make sure to leave this particular character out during your next attempt"+RESET)
            encrypted_message += library[location]
        if outputMode:
            print(GREY+"encrypted message:"+RESET)
        return encrypted_message
    elif method == "decrypt" or method == "decipher":
        decrypted_message = ""
        if outputMode:
            print("provided message to decode:")
            print(BLUE+message+RESET)
        if debug:
            print(library)
        for i in message:
            try:
                location = library.index(i)
            except ValueError:
                return print(RED+f"ERROR: the Enkripto library currently does not support use of the character '{i}'. Please make sure to leave this particular character out during your next attempt"+RESET)
            decrypted_message += normallibrary[location]
        if outputMode:
            print("decoded message:")
        return decrypted_message
    else:
        return print(RED+f"invalid param '{method}'"+RESET)


#this function packs all seeds provided (see help menu)
#params:
# UsedSeed: the seed you want to pack
def packSeed(UsedSeed: str,outputMode: bool):
    global packerLibrary
    if packerLibrary is None:
        packerLibrary = createLibrary(normallibrary , random.randint(100,9999999),"none")
    encryptedSeed = execute("encrypt", UsedSeed, packerLibrary, False)
    shuffleBy = random.randint(0, len(encryptedSeed)-1)
    for e in range(shuffleBy):
        encryptedSeed += encryptedSeed[0]
        encryptedSeed = encryptedSeed[1:]
    return "0" + str(shuffleBy) + encryptedSeed if len(str(shuffleBy)) == 1 else str(shuffleBy) + encryptedSeed
# this is the initial creation and definition of important variables
def makeLibrary():
    global SeedInUse1
    global importseed
    global library
    global packerLibrary
    if createNew:
        library = createLibrary(normallibrary, random.randint(100,9999999), "init")
        createLibrary(library , random.randint(100,9999999) , "commercial")
        for i in range(encryptionamount):
            library = createLibrary(library , random.randint(100,9999999),"none")
        SeedInUse1 = str(initseed) + "." + str(encryptionamount) + "." + str(commercialseed)
        print(BLUE+"creating new seed..."+RESET)
        print(GREY+"layers:"+RESET)
        print(GREEN+str(encryptionamount)+RESET)
        print(GREY+"library in use:"+RESET)
        print(GREEN+library+RESET)
        print(GREY+"seed in use:"+RESET)
        print(GREEN+SeedInUse1+RESET)
        packerLibrary = None
    elif readFromENK or importseed:
        #behold, the legendary ENK file interpreter:
        if readFromENK:
            try:
                with open(fileLocation,"r") as file:
                    filecontent = file.read()
                    if not filecontent.startswith("ENKR"):
                        print(RED+"ERROR: file structure is invalid."+RESET)
                        StopFunc("init")
                        return
                    elif filecontent[4] not in compatibleENKversions:
                        print(RED+f"ERROR: File uses Wrong interpreter version. ({filecontent[4]})"+RESET)
                        StopFunc("init")
                        return
                    else:
                        try:
                            lOFl_seed=int(filecontent[5])
                            seedLen = int(filecontent[6:6+lOFl_seed])
                            lOFl_libr = int(filecontent[6+lOFl_seed])
                            librLen = int(filecontent[7+lOFl_seed:7+lOFl_seed+lOFl_libr])
                        except ValueError:
                            print(RED+"ERROR: file structure is invalid."+RESET)
                            StopFunc("init")
                            return
                        importseed = filecontent[7+lOFl_seed+lOFl_libr:7+lOFl_seed+lOFl_libr+seedLen]
                        packerLibrary = filecontent[7+lOFl_seed+lOFl_libr+seedLen:7+lOFl_seed+lOFl_libr+seedLen+librLen]
            except FileNotFoundError:
                print(YELLOW+f"WARNING: no {fileLocation} file exists. creating new Default..."+RESET)
                with open(fileLocation,"w") as file:
                    library = createLibrary(normallibrary, random.randint(100,9999999), "init")
                    createLibrary(library , random.randint(100,9999999) , "commercial")
                    for i in range(encryptionamount):
                        library = createLibrary(library , random.randint(100,9999999),"none")
                    SeedInUse1 = str(initseed) + "." + str(encryptionamount) + "." + str(commercialseed)
                    importseed=packSeed(SeedInUse1,True)
                    packerLibrary = createLibrary(normallibrary, random.randint(1000,9898),"None")
                    MAGIC="ENKR"
                    ENKversion = "1"
                    seedData = importseed
                    seedDataLength = str(len(seedData))
                    lengthOfseedDataLength = str(len(str(seedDataLength)))
                    packerlibrary = packerLibrary
                    packerlibrarylength = str(len(packerlibrary))
                    lengthOfPackerlibrarylength=str(len(str(packerlibrarylength)))
                    content = MAGIC + ENKversion + lengthOfseedDataLength + seedDataLength + lengthOfPackerlibrarylength + packerlibrarylength + seedData + packerlibrary
                    file.write(content)
            except IndexError:
                print(RED+f"ERROR in ENKreader ; {fileLocation} file format is invalid."+RESET)
                StopFunc("init")
                return
        else:
            print(YELLOW+f"WARNING: reading {fileLocation} disabled. reading manual seed..."+RESET)
            if seed_ispacked:
                if len(custom_PackerLibrary) == len(normallibrary):
                    packerLibrary = custom_PackerLibrary
                else:
                    print(RED+"ERROR in custom_PackerLibrary reader ; custom_packerlibrary format is invalid."+RESET)
                    StopFunc("init")
                    return
        print(BLUE+"provided seed: " + importseed+RESET)
        if seed_ispacked:
            if cleanse(importseed) is not None:
                cleansedSeed = cleanse(importseed)
                print(BLUE+"cleansed seed: " + cleansedSeed+RESET)
                CleansedAndDecodedSeed = execute("decrypt", cleansedSeed,packerLibrary)
                print(BLUE+"decoded seed: " + CleansedAndDecodedSeed+RESET)
            else:
                print(RED+"ERROR in cleanseSeed ; invalid seed provided!"+RESET)
                StopFunc("init")
                return
        try:
            getinitseed , getencryptionamount, getCommercialSeed = CleansedAndDecodedSeed.split(".") if seed_ispacked else cleansedSeed.split(".")
        except ValueError:
            print(RED+"ERROR in getSeedValues ; invalid seed provided!"+RESET)
            StopFunc("init")
            return
        try:
            getinitseed = int(getinitseed)
            getencryptionamount = int(getencryptionamount)
            getCommercialSeed = int(getCommercialSeed)
        except ValueError:
            print(RED+"ERROR in convertSeedValues ; invalid seed provided!"+RESET)
            StopFunc("init")
            return
        #TODO
        library=createLibrary(normallibrary, getinitseed, "init")
        createLibrary(library, getCommercialSeed, "commercial")
        for i in range(getencryptionamount):
            library = createLibrary(library, random.randint(100,9999999), "commercial")
        SeedInUse1 = CleansedAndDecodedSeed if seed_ispacked else cleansedSeed
        print("library in use:")
        print(BLUE+library+RESET)
        print("seed in use:")
        print(BLUE+SeedInUse1+RESET)
        print("encryption layer amount:")
        print(BLUE+str(encryptionamount)+RESET)

#displays the seed. either packed or raw
def displaySeed():
    print(BLUE+"displaying seed in use..."+RESET)
    if packMySeed:
        if packSeed(SeedInUse1,False) is not None:
            print(YELLOW+"seed is packed:"+RESET)
            print(BLUE+"--->   " + packSeed(SeedInUse1,False) + "   <---"+RESET)
            print("packerLibrary:")
            print(BLUE+packerLibrary+RESET)
        else:
            print(RED+"ERROR: Unable to fetch seed. If you are sure that your seed was not tampered with, please report this." +RESET)
            StopFunc("displayseed")
            return
    else:
        print(YELLOW+"seed is unpacked:"+RESET)
        print(SeedInUse1)

#transfers your current seed and packerlibrary to the .enk file, overwrites previous values
def writeToENK():
    print(BLUE+f"writing packed seed and packerLibrary into {fileLocation} ..."+RESET)
    try:
        test = SeedInUse1
    except NameError:
        print(RED+"ERROR seed has not been defined yet. Try initiating before saving."+RESET)
        StopFunc("writeToENK")
        return
    try:
        test1 = packerLibrary
    except NameError:
        print(YELLOW+"WARNING: packerLibrary has not been defined yet. Packing seed..."+RESET)
    if packSeed(SeedInUse1,False) is not None:
        MAGIC="ENKR"
        ENKversion = "1"
        seedData = packSeed(SeedInUse1,True)
        seedDataLength = str(len(seedData))
        lengthOfseedDataLength = str(len(str(seedDataLength)))
        packerlibrary = packerLibrary
        packerlibrarylength = str(len(packerlibrary))
        lengthOfPackerlibrarylength=str(len(str(packerlibrarylength)))
        content = MAGIC + ENKversion + lengthOfseedDataLength + seedDataLength + lengthOfPackerlibrarylength + packerlibrarylength + seedData + packerlibrary
        with open(fileLocation,"w") as file:
            file.write(content)
    else:
        print(RED+"ERROR: Unable to pack seed. If you are sure that your seed was not tampered with, please report this." +RESET)
        StopFunc("save/write")
        return
    print(GREEN+f"successfully written data to {fileLocation}"+RESET)

# self explanatory
def checkForBool(item: str):
    if item.split("=")[1] == "true" or item.split("=",1)[1] == "1":
        return True
    if item.split("=")[1] == "false" or item.split("=",1)[1] == "0":
        return False
    print(RED+f"ERROR: expected Boolean value (true/false/1/0) and got faulty value ('{item}')"+RESET)
    return None

# self explanatory too
def checkForInt(item: str):
    try:
        intitem= int(item.split("=",1)[1])
        return intitem
    except ValueError:
        print(RED+f"ERROR: expected integer value and got faulty value ('{item}')"+RESET)
        return None

#this is an example of what a workflow used to look like:
# resetFile()
# makeLibrary()
# displaySeed()
# print(execute("decipher","5abB{5hbjLmGhb5WW$bh{5BbW b-$xBh")) <- all this is probably outdated as well
# luckily I have added my own parser now... So you don't have to hardcode inputs... Thank me later... Or never...



def testEncryption(mode: int):
    if mode == 1:
        print(BLUE+"Running diagnostics..."+RESET)
    else:
        print(BLUE+"Running backup diagnostics..."+RESET)
    time.sleep(0.15)
    old_stdout=sys.stdout
    sys.stdout=open(os.devnull,"w")
    try:
        makeLibrary()
        global library
        encodeThis = execute("encrypt", "Hello World! 0.7&3 <- hope that works...", library,True)
        decodeThat = execute("decipher", encodeThis, library, False)
    except Exception as e:
        sys.stdout=old_stdout
        print(RED+f"FATAL ERROR FOUND: {e}"+RESET)
        print("This Release will thus not run.")
        print("PLEASE REPORT THIS ERROR ON GITHUB ISSUES!"+RESET)
        if debug:
            traceback.print_exc()
        print(YELLOW+"the program will close in 5 seconds..."+RESET)
        time.sleep(5)
        exit()
    if decodeThat != "Hello World! 0.7&3 <- hope that works...":
        sys.stdout=old_stdout
        print(RED+"EXCEPTION FOUND: Incorrect decoding results")
        print("This Release will thus not run.")
        print("PLEASE REPORT THIS ERROR ON GITHUB ISSUES!"+RESET)
        print(YELLOW+"the program will close in 5 seconds..."+RESET)
        print(encodeThis)
        print(decodeThat)
        time.sleep(5)
        exit()
    sys.stdout=old_stdout
    print(GREEN+"Testing completed successfully!"+RESET)
    global SeedInUse1,importseed,packerLibrary
    del SeedInUse1,packerLibrary
    library=""
    importseed=r""
    time.sleep(0.1)

def mktxt(name: str, content: str):
    name = name if name.endswith(".txt") else name + ".txt"
    with open(name,  "w", encoding="utf-8") as file:
        write = content if content else ""
        file.write(write)
    return name

def AQcreator():
    while True:
        print(PROMPTPINK+"AutoQueryCreator: Enter Prompt > "+RESET)

# IMPORTANT main workflow:
fetchPreferences()
time.sleep(0.25)
testEncryption(1)
testEncryption(2)
time.sleep(0.25)
intro()


#   @0@@@@@@    @@@@@@   @@@@@@@    @@@@@@   @@@@@@@@  @@@@@@@        
#   @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@  @@@@@@@@       
#   @@!  @@@  @@!  @@@  @@!  @@@  !@@       @@!       @@!  @@@       
#   !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!       !@!  @!@  @!@  
#   @!@@!@!   @!@!@!@!  @!@!!@!   !!@@!!    @!!!:!    @!@!!@!   !@!  
#   !!@!!!    !!!@!!!!  !!@!@!     !!@!!!   !!!!!:    !!@!@!    !:!  
#   !!:       !!:  !!!  !!: :!!        !:!  !!:       !!: :!!        
#   :!:       :!:  !:!  :!:  !:!      !:!   :!:       :!:  !:!  :!:  
#    ::       ::   :::  ::   :::  :::: ::    :: ::::  ::   :::  :::  
#    :         :   : :   :   : :  :: : :    : :: ::    :   : :  :::  

while True:
    prompt = input(PROMPTPINK + "NHH: awaiting input >  " + RESET)

        #####################
        #HELP RELATED TOPICS#
        #####################
    
    #CHECKING FOR help REQUEST
    if prompt.lower() == "help":
        # get ready... FOR PRINT HELL!
        print(BLUE+"\n-- HELP MENU --"+RESET)
        print('type "help" followed by a certain command or term to view advanced information about it (type "help list" to view all terms that have help data)\n') 
        print('type "explain" to receive a tutorial on how to use ENKRIPTO\n')
        print("capitalization doesn't matter\n")
        print("Enkripto uses it's own mini parsing language: NHH - Native Handling Hub\n")
        print("parameters: {parameter_name: parameter_type} ; function aliases: name1 / name2  (either works. just pick the one you prefer)\n")
        print("to see all global parameters, type 'all.params'\n")
        print("parameter order does not matter\n")
        print('refrain from using any quotation marks in your prompts. strings are interpreted as such by default and will thus end up containing extra quotations mark in them, making them uninterpretable. if you set your seed to importseed = "123.456.789", the value will be ""123.456.789"".\n')
        print("the underscore ( _ ) can be left out in parameter names ( seed_ispacked = seedispacked )\n")
        print("If parameters are not provided ENKRIPTO will vent to defaults \n")
        print("startup preferences are stored in preferences.json\n")
    elif prompt.lower() == "help commands":
        print(YELLOW+"-- COMMANDS --\n"+RESET)
        print(BLUE+"resetfile"+RESET+" - resets the txt file to default values\n")
        print(BLUE+"initiate / init"+YELLOW+" {createnew: bool} , {readfromENK: bool} , {filelocation: str} , {custom_packerlibrary: str} , {seed_ispacked: bool} , {encryptionamount: int} , {packmyseed: bool}"+RESET+" - initiates ENKRIPTO's library (re)creation process;\n⤤ type 'help initiate' or 'help init' for a parameter explanation\n")
        print(BLUE+"(function).params "+RESET+"- shows a function's params and their current values \n") 
        print(BLUE+"save / write "+YELLOW+"{filelocation: str} "+RESET+"- packs and saves current seed in a txt.\n⤤ type 'help save' or 'help write' for a parameter explanation\n")
        print(BLUE+"displayseed / display "+YELLOW+"{packmyseed / pack: bool}"+RESET+" - displays the current seed in use. if packmyseed / pack is true, it will be displayed as a packed seed. Otherwhise it will be displayed in it's natural form.\n")
        print(BLUE+"scan / list / ls "+RESET+"- scans and lists current directory to make locating your save .txt file easier.\n") #TODO
        print(BLUE+"currentpath / cwd / currentdir "+RESET+"- displays your work directory's path.\n")
        print(BLUE+"restoredefaults / defaults / default "+RESET+"- restores all parameters to their default values.\n")
        print(BLUE+"exit "+RESET+"- closes the program\n")
        print(BLUE+"setparams / setparam "+YELLOW+"{createnew: bool} , {packmyseed / pack: bool} , {custom_packerlibrary / custompackerlibrary: str} , {importseed: str} , {seed_ispacked / seedispacked: bool} , {debug: bool} , {encryptionamount: int} , {filelocation: str} "+RESET+"- command used to change certain parameters without executing any other functions. The debug parameter is a developer tool that shows extra information. Enabling it isn't recommended.\n")
        print(BLUE+"encrypt / encode "+YELLOW+"{msg: str} . {target: str} "+RESET+"- encrypts the provided target message using your library. Use msg for raw text and target for txts.\n")
        print(BLUE+"decipher / decode "+YELLOW+"{msg / target: str} "+RESET+"- decodes the provided target message using your library.\n")
    #CHECKING FOR help REQUESTS AND FURTHER ARGS
    elif prompt.lower() == "help initiate" or prompt.lower() == "help init":
        print(BLUE+"-- ADVANCED HELP MENU - ENTRY 01 --\n"+RESET)
        print(GREEN+"INIT(IATE) FUNCTION:\n"+RESET)
        print("general info:\nthe initiate function is used to kickstart the process of generating your library and seed. It is highly customizeable due to it's variety in different parameters (params). It is imperative that this function has been called before any other functions may run because it sets the baseline for any other further tools this module contains. It can not only create a new library and seed etc. , but it can also be used to import already existing seed-data, either from a .txt file, or using the data's manual input. your choice.\n")
        print("parameters:\n")
        print("NAME:\ncreatenew\nTYPE:\nBool\nUSECASE:\nif set to True, an entirely new seed and library will be generated in the initiation process. given data like readfromENK, importseed, custompackerlibrary and more will be ignored, however params used solely for creation like encryptionamount will be utilized. If it is set to False, the initiation process will try to import any given values. It will first check if readfromENK is enabled (if so it will import the values from the .txt file) and then check for custom values (if none exist, hardcoded default values will be used. I advise against this, because encrypto relies on the diversity of it's encryption schemes, so using a singular fixed library and/or seed might bring up safety issues.)")
        print("\nNAME:\nreadfromENK\nTYPE:\nBool\nUSECASE:\nif set to True (and createnew is set to false), seed-values will be read from the provided .enk file")
        print("\nNAME:\nimportseed\nTYPE:\nString\nUSECASE:\nparameter used for manual import of a seed. If you insert a packed seed, you must enable seed_ispacked and vice versa. Otherwhise the program will fail. NOTE that it is suggested to not use any spaces when defining this parameter (parameter=value)")
        print("\nNAME:\ncustom_packerlibrary\nTYPE:\nString\nUSECASE:\nparameter used for manual import of the library used to pack the manually imported seed. This parameter is only necessary if the seed you manually provided is packed.  NOTE that it is suggested to not use any spaces when defining this parameter (parameter=value)")
        print("\nNAME:\nseed_ispacked\nTYPE:\nBool\nUSECASE:\nIf you manually import a seed, you will have to set seed_ispacked to the corresponding value depending on if it is packed or not. if the provided seed is packed : seed_ispacked = True ; if it is not packed : seed_ispacked = False")
        print("\nNAME:\nencryptionamount\nTYPE:\nInt\nUSECASE:\nparameter that defines the amount of times your library will encrypt itself. This param is only used when creating a new library and it's default is a random integer.")
        print("\nNAME:\nfilelocation\nTYPE:\nString\nThe path to your mounted .enk file. This can be an absolute path (C:\\myprojects/enkfiles/save.enk) or a relative path (enkfiles/save.enk (if you are currently in the myprojects directory)). If you don't have an .enk file yet, one will be created for you if you execute the 'save' or 'write' command after initiating")
    elif prompt.lower() == "help list":
        print(BLUE+"-- LIST OF ALL COMMANDS WITH HELP DATA --\n"+RESET)
        print(GREY+"type 'help' followed by the entry name to view it (e.g 'help comands')"+RESET)
        print("00 - COMMANDS\n")
        print("01 - INIT(IATE)\n")
        print("02 - SAVE / WRITE\n")
        print("03 - SEEDS\n")
        print("04 - LIBRARIES\n")
        print("-- MORE TO COME --")
    elif prompt.lower() == "explain":
        print("official ENKRIPTO youtube tutorial:\n https://youtu.be/76r2yHeQkC8")
        print("official ENKRIPTO documentation page:\n https://bokrsteski.github.io/Enkripto/")
        ######################
        #PARAM RELATED TOPICS#
        ######################
    elif prompt.lower() == "help save" or prompt.lower() == "help write":
        print("-- ADVANCED HELP MENU - ENTRY 02 --\n")
        print("SAVE / WRITE FUNCTION:\n")
        print("general info:\nthe save function saves your current seed in it's packed form and the library used to pack it in a .enk file of your choice. This allows for easier sharing of your seed-data, so that others can decode your previously encrypted messages easier.\n")
        print("parameters:")
        print("\nNAME:\nfilelocation\nTYPE:\nString\nThe path to your mounted .enk file This can be an absolute path (C:\\myprojects/enkfiles/save.enk) or a relative path (enkfiles/save.enk (if you are currently in the myprojects directory)). If you don't have an .enk file yet, one will be created for you if you execute the 'save' command after initiating")
    elif prompt.lower() == "help seeds":
        print("-- ADVANCED HELP MENU - ENTRY 03 --\n")
        print("SEEDS:\n")
        print("a seed is a set of numeric values that enable enkripto to replicate any library without actually having to import it.\nThis, for one, increases security, because the library itself is never shared, and furthermore increases convenience because it is transferrable via a .txt file or can just be copied due to it's small size.\nA seed can either be packed or raw. Packing your seed adds extra levels of security, but makes it longer. It is advised to share packed seeds via txt because of their length, but raw seeds can easily be copied.\nif you're having trouble spotting raw or packed seeds:\nraw seeds look somewhat like this: 123.4567.890 . They are fairly small and consist purely of numbers and dots.\npacked seeds look like a scrambled text: dfsizt2u673598$& . this makes it extremely easy to differentiate betweeen the two.")
    elif prompt.lower() == "help libraries":
        print("-- ADVANCED HELP MENU - ENTRY 04 --\n")
        print("LIBRARIES:\n")
        print("a library is a version of the alphabet, which has been scrambled and mixed to become unreadable. It is used as the scheme for all encryptions and also decodings.\n")
    # CHECKING FOR .params REQUESTS
    elif prompt.lower() == "initiate.params" or prompt.lower() == "init.params":
        print("- showing relevant params for initiation process -")
        print(f"createNew = {createNew}")
        print(f"readFromENK = {readFromENK}")
        print(f"fileLocation = {fileLocation}")
        print(f"custompackerlibrary = {custom_PackerLibrary}")
        print(f"importseed = {importseed}")
        print(f"seed_ispacked = {seed_ispacked}")
        print(f"encryptionamount = {encryptionamount}")
        print(f"fileLocation = {fileLocation}")
    elif prompt.lower() == "save.params" or prompt.lower() == "write.params":
        print("- showing relevant params for saving process -")
        print(f"fileLocation = {fileLocation}")
    elif prompt.lower() == "display.params" or prompt.lower() == "displayseed.params":
        print("- showing relevant params for display process -")
        print(f"packMySeed = {packMySeed}")
    elif prompt.lower() == "all.params": 
        try:
            test = SeedInUse1
            print("- showing all params -")
            print(f"createNew = {createNew}")
            print(f"readFromENK = {readFromENK}")
            print(f"fileLocation = {fileLocation}")
            print(f"custompackerlibrary = {custom_PackerLibrary}")
            print(f"importseed = {importseed}")
            print(f"seed_ispacked = {seed_ispacked}")
            print(f"encryptionamount = {encryptionamount}")
            print(f"fileLocation = {fileLocation}")
            print(f"packMySeed = {packMySeed}")
        except NameError:
            print(RED+"ERROR: seed has not been defined yet. Try initiating before saving."+RESET)
        ##########
        #COMMANDS#
        ##########
    # checking for different commands:
    elif prompt.lower() == "resetfile":
        resetFile()
    elif prompt.lower().startswith("initiate") or prompt.lower().startswith("init"):
        params = prompt.lower().removeprefix("initiate").replace(" ","").split(",") if prompt.lower().startswith("initiate") else prompt.lower().removeprefix("init").replace(" ","").split(",")
        caseSensitiveParams = prompt[8:].replace(" ","").split(",")  if prompt.lower().startswith("initiate") else prompt[4:].replace(" ","").split(",")
        casesensitivecounter = 0
        if debug:
            print(params)
        paramexception: bool = False
        if len(params) > 0 and params[0] != "":
            modifiedParamsList = []
            paramexception = False
            for i in params:
                casesensitivecounter =+ 1
                if i.replace(" ","").startswith("createnew="):
                    if checkForBool(i.replace(" ","")) is not None:
                        createNew = checkForBool(i.replace(" ",""))
                        modifiedParamsList.append(f"createnew = {createNew}")
                        with open("preferences.json","w") as file:
                            Preferences["createnew"] = 1 if createNew else 0
                            json.dump(Preferences,file,indent=4)
                    else:
                        paramexception = True
                elif i.replace(" ","").startswith("readfromenk="):
                    if checkForBool(i.replace(" ","")) is not None:
                        readFromENK =checkForBool(i.replace(" ",""))
                        modifiedParamsList.append(f"readFromENK = {readFromENK}")
                        with open("preferences.json","w") as file:
                            Preferences["readfromENK"] = 1 if readFromENK else 0
                            json.dump(Preferences,file,indent=4)
                    else:
                        paramexception = True
                elif i.replace(" ","").startswith("custompackerlibrary=") or i.replace(" ","").startswith("custom_packerlibrary="):
                    libraryScanner = caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]
                    if libraryScanner.count(" ") == 2:
                        custom_PackerLibrary = libraryScanner.replace(" ","",1)
                        modifiedParamsList.append(f"custom_packerlibrary = {custom_PackerLibrary}")
                    elif libraryScanner.count(" ") == 1:
                        custom_PackerLibrary = libraryScanner
                        modifiedParamsList.append(f"custom_packerlibrary = {custom_PackerLibrary}")
                    else:
                        print(RED+"ERROR: lethal spaces detected in custom_packerlibrary! Try defining this parameter without any spaces inbetween (custompackerlibrary=...)"+RESET)
                        paramexception = True
                elif i.replace(" ","").startswith("importseed="):
                    libraryScanner = caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]
                    if libraryScanner.count(" ") == 2:
                        importseed = libraryScanner.replace(" ","",1)
                        modifiedParamsList.append(f"importseed = {importseed}")
                    elif libraryScanner.count(" ") == 1:
                        importseed = libraryScanner
                        modifiedParamsList.append(f"importseed = {importseed}")
                    else:
                        print(RED+"ERROR: lethal spaces detected in custom_packerlibrary! Try defining this parameter without any spaces inbetween (custompackerlibrary=...)"+RESET)
                        paramexception = True
                    if checkForBool(i.replace(" ","")) is not None:
                        seed_ispacked = checkForBool(i.replace(" ",""))
                        modifiedParamsList.append(f"seed_ispacked = {seed_ispacked}")
                    else:
                        paramexception= True
                elif i.replace(" ","").startswith("encryptionamount="):
                    if checkForInt(i.replace(" ","")) is not None:
                        encryptionamount = checkForInt(i.replace(" ",""))
                        modifiedParamsList.append(f"encryptionamount = {encryptionamount}")
                    else:
                        paramexception = True
                elif i.replace(" ","").startswith("filelocation="):
                    if i.replace(" ","").split("=",1)[1].endswith(".enk"):
                        fileLocation = caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]
                        modifiedParamsList.append(f"fileLocation = {fileLocation}")
                        with open("preferences.json","w") as file:
                            Preferences["filelocation"] = fileLocation
                            json.dump(Preferences,file,indent=4)
                    elif "." in i.replace(" ","").split("=",1)[1]:
                        print(RED+f"ERROR: invalid filetype '{"." + caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1].split(".")[1]}'"+RESET)
                        print(YELLOW+"only '.enk' files are allowed to save enkripto data"+RESET)
                        paramexception = True
                    else:
                        print(RED+f"ERROR: invalid filetype '{"." + caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1].split(".")[1]}'"+RESET)
                        print(YELLOW+"only '.enk' files are allowed to save enkripto data"+RESET)
                        paramexception = True
                else:
                    if len(modifiedParamsList) > 0:
                        if debug:
                            print(modifiedParamsList)
                        print(GREEN+"parameters succesfully modified: "+BLUE+f"{" , ".join(modifiedParamsList)}") if len(modifiedParamsList) > 1 else print(f"parameters succesfully modified: {modifiedParamsList[0]}"+RESET)
                    print(RED+f"ERROR: invalid parameter definement ('{i}')"+RESET)
                    paramexception = True
        # safe way of handling exceptions while still respecting other parameter changes, so that every param will be modified except for the one with the faulty value.
        # the process also gets aborted when a parameter definement is faulty, so that execution with wrong or even fatal params can be prevented.
        if paramexception:
            print(YELLOW+"initiation aborted."+RESET)
        else:
            if len(params) > 0 and params[0] != "":
                print(GREEN+"parameters succesfully modified: "+BLUE+f"{" , ".join(modifiedParamsList)}") if len(modifiedParamsList) > 1 else print(f"parameters succesfully modified: {modifiedParamsList[0]}"+RESET)
            makeLibrary()
    #pretty cool tool: essentially just like bash's or linux's "ls". scans current work directory and lists directories and files.
    elif prompt.lower() == "scan" or prompt.lower() =="list" or prompt.lower() =="ls":
        print(GREEN+"displaying files and directories in current directory:"+RESET)
        for file in os.listdir():
            if os.path.isdir(file):
                print(DIRBLUE+f"DIR : {file}"+RESET)
            else:
                print(DIRRED+f"FILE: {file}"+RESET)
    #displays current work directory path.
    elif prompt.lower() =="currentpath" or prompt.lower() =="cwd" or prompt.lower() =="currentdir":
        print(BLUE+"current directory:"+GREEN+f" {os.getcwd()}")
    #resets all parameters to default values.
    elif prompt.lower() =="restoredefaults" or prompt.lower() == "default" or prompt.lower() == "defaults":
        createNew = True
        readFromENK = False
        library1 = createLibrary(normallibrary, random.randint(100,9999999), "init")
        createLibrary(library1 , random.randint(100,9999999) , "commercial")
        for i in range(encryptionamount):
            library1 = createLibrary(library1 , random.randint(100,9999999),"none")
        global commercialseed
        global initseed
        SeedInUse2 = str(initseed) + "." + str(encryptionamount) + "." + str(commercialseed)
        importseed=packSeed(SeedInUse2,True)
        custom_packerLibrary = createLibrary(normallibrary, random.randint(1000,9898),"None")
        seed_ispacked = True
        encryptionamount =random.randint(100,500) 
        packMySeed = True
        print(BLUE+"defaulting...\nsome true values are excluded due to their length:"+RESET)
        print(BLUE+"createnew = "+GREEN+f"{createNew} \n"+BLUE+f"readfromENK = "+GREEN+f"{readFromENK}\n"+BLUE+f"custom_packerlibrary = "+YELLOW+f"(default value)\n"+BLUE+f"importseed = "+YELLOW+f"(default value)\n"+BLUE+f"seed_ispacked = "+GREEN+f"{seed_ispacked}\n"+BLUE+f"encryptionamount = "+BLUE+f"{encryptionamount} "+YELLOW+"(randomized)\n"+BLUE+f"packmyseed = "+GREEN+f"{packMySeed}\n"+BLUE+f"filelocation = "+GREEN+f"{fileLocation}")
        print(GREEN+"defaults restored!"+RESET)
    #exits and tips the program's virtual hat to the user.
    elif prompt.lower() == "exit":
        print(DIRBLUE+"See you next time!"+RESET)
        time.sleep(0.75)
        sys.exit()
    elif prompt.lower() == "viewprefs" or prompt.lower() =="viewpreferences" or prompt.lower() == "showprefs" or prompt.lower() == "showpreferences":
        fetchPreferences(True)
    #saves seed-data to an .enk file.
    elif prompt.lower().startswith("save") or prompt.lower().startswith("write"):
        params = prompt.lower().removeprefix("save").replace(" ","").split(",") if prompt.lower().startswith("save") else prompt.lower().removeprefix("write").replace(" ","").split(",")
        caseSensitiveParams = prompt[9:].split(",") if prompt.lower().startswith("setparams") else prompt[8:].split(",")
        casesensitivecounter = 0
        if debug:
            print(params)
        paramexception = False
        if len(params) > 0 and params[0] != "":
            modifiedParamsList = []
            paramexception = False
            for i in params:
                casesensitivecounter += 1
                if i.replace(" ","").startswith("filelocation="):
                    if i.replace(" ","").split("=",1)[1].endswith(".enk"):
                        fileLocation = caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]
                        modifiedParamsList.append(f"fileLocation = {fileLocation}")
                        with open("preferences.json","w") as file:
                            Preferences["filelocation"] = fileLocation
                            json.dump(Preferences,file,indent=4)
                    elif "." in i.replace(" ","").split("=",1)[1]:
                        print(RED+f"ERROR: invalid filetype '{"." + caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1].split(".")[1]}'"+RESET)
                        print(YELLOW+"only '.enk' files are allowed to save enkripto data"+RESET)
                        paramexception = True
                    else:
                        print(RED+f"ERROR: invalid filetype '{"." + caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1].split(".")[1]}'"+RESET)
                        print(YELLOW+"only '.enk' files are allowed to save enkripto data"+RESET)
                        paramexception = True
                else:
                    if len(modifiedParamsList) > 0:
                        if debug:
                            print(modifiedParamsList)
                            # HERE HERE HERE HERE HERE HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                            print(GREEN+"parameters succesfully modified: "+BLUE+f"{" , ".join(modifiedParamsList)}") if len(modifiedParamsList) > 1 else print(f"parameters succesfully modified: {modifiedParamsList[0]}"+RESET)
                    print(RED+f"invalid parameter definement ('{i}')"+RESET)
                    paramexception = True
        if paramexception:
            print(YELLOW+"process aborted."+RESET)
        else:
            if len(params) > 0 and params[0] != "":
                print(GREEN+"parameters succesfully modified: "+BLUE+f"{" , ".join(modifiedParamsList)}") if len(modifiedParamsList) > 1 else print(f"parameters succesfully modified: {modifiedParamsList[0]}"+RESET)
            writeToENK()
    elif prompt.lower().startswith("mktxt"):
        params = prompt.lower().removeprefix("mktxt").split(",")
        if debug:
            print(params)
        paramexception = False
        if len(params) > 0 and params != "":
            modifiedParamsList = []
            paramexception = False
            contents = ""
            mktxtname = None
            for i in params:
                if i.replace(" ","").startswith("contents="):
                    contents = i.split("=",1)[1]
                elif i.replace(" ","").startswith("name="):
                    mktxtname =  i.replace(" ","").split("=",1)[1]
                else:
                    print(RED+f"invalid parameter definement ('{i}')"+RESET)
                    paramexception = True
            if paramexception:
                print(YELLOW+"initiation aborted."+RESET)
            elif mktxtname is not None:
                if contents == "":
                    print(YELLOW+"WARNING: contents not defined. creating empty txt..."+RESET)
                else:
                    print(BLUE+"creating txt..."+RESET)
                print(mktxt(mktxtname,contents))
            else:
                print(RED+"ERROR: filename not defined! \nuse 'name=' to name the file. the '.txt' extension is not necessary, as it is auto-added"+RESET)
        else:
            print(RED+"ERROR: filename not defined! \nuse 'name=' to name the file. the '.txt' extension is not necessary, as it is auto-added"+RESET)

    #displays the seed.
    elif prompt.lower().startswith("displayseed") or prompt.lower().startswith("display"):
        params = prompt.lower().removeprefix("displayseed").replace(" ","").split(",") if prompt.lower().startswith("displayseed") else prompt.lower().removeprefix("display").replace(" ","").split(",")
        if debug:
            print(params)
        paramexception = False
        if len(params) > 0 and params[0] != "":
            modifiedParamsList = []
            paramexception = False
            for i in params:
                if i.replace(" ","").startswith("packmyseed=") or i.replace(" ","").startswith("pack="):
                    packMySeed = checkForBool(i.replace(" ",""))
                    modifiedParamsList.append(f"packMySeed = {packMySeed}")
                else:
                    if len(modifiedParamsList) > 0:
                        if debug:
                            print(modifiedParamsList)
                        print(GREEN+"parameters succesfully modified: "+BLUE+f"{" , ".join(modifiedParamsList)}") if len(modifiedParamsList) > 1 else print(f"parameters succesfully modified: {modifiedParamsList[0]}"+RESET)
                    print(RED+f"invalid parameter definement ('{i}')"+RESET)
                    paramexception = True
        if paramexception:
            print(YELLOW+"initiation aborted."+RESET)
        else:
            if len(params) > 0 and params[0] != "":
                print(GREEN+"parameters succesfully modified: "+BLUE+f"{" , ".join(modifiedParamsList)}") if len(modifiedParamsList) > 1 else print(f"parameters succesfully modified: {modifiedParamsList[0]}"+RESET)
            displaySeed()
    #sets parameters to custom values. as long as their type and content is allowed. This isn't that kind of playground.
    elif prompt.lower().startswith("setparams") or prompt.lower().startswith("setparam"):
        params = prompt.lower().removeprefix("setparams").replace(" ","").split(",") if prompt.lower().startswith("setparams") else prompt.lower().removeprefix("setparam").replace(" ","").split(",")
        caseSensitiveParams = prompt[9:].split(",") if prompt.lower().startswith("setparams") else prompt[8:].split(",")
        casesensitivecounter = 0
        if debug:
            print(params)
        paramexception: bool = False
        if len(params) > 0 and params[0] != "":
            modifiedParamsList = []
            paramexception = False
            for i in params:
                casesensitivecounter =+ 1
                if i.replace(" ","").startswith("createnew="):
                    if checkForBool(i.replace(" ","")) is not None:
                        createNew = checkForBool(i.replace(" ",""))
                        modifiedParamsList.append(f"createnew = {createNew}")
                        with open("preferences.json","w") as file:
                            Preferences["createnew"] = 1 if createNew else 0
                            json.dump(Preferences,file,indent=4)
                    else:
                        paramexception = True
                elif i.replace(" ","").startswith("packmyseed=") or i.replace(" ","").startswith("pack="):
                    packMySeed = checkForBool(i.replace(" ",""))
                    modifiedParamsList.append(f"packMySeed = {packMySeed}")
                elif i.replace(" ","").startswith("readfromENK="):
                    if checkForBool(i.replace(" ","")) is not None:                        
                        readFromENK =checkForBool(i.replace(" ",""))
                        modifiedParamsList.append(f"readFromENK = {readFromENK}")
                        with open("preferences.json","w") as file:
                            preference[2] = 1 if readFromENK else 0
                            json.dump(Preferences,file,indent=4)
                    else:
                        paramexception = True
                elif i.replace(" ","").startswith("custompackerlibrary=") or i.replace(" ","").startswith("custom_packerlibrary="):
                    libraryScanner = caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]
                    if libraryScanner.count(" ") == 2:
                        custom_PackerLibrary = libraryScanner.replace(" ","",1)
                        modifiedParamsList.append(f"custom_packerlibrary = {custom_PackerLibrary}")
                    elif libraryScanner.count(" ") == 1:
                        custom_PackerLibrary = libraryScanner
                        modifiedParamsList.append(f"custom_packerlibrary = {custom_PackerLibrary}")
                    else:
                        print(RED+"ERROR: lethal spaces detected in custom_packerlibrary! "+YELLOW+"Try defining this parameter without any spaces inbetween (parameter=value)"+RESET)
                        paramexception = True
                elif i.replace(" ","").startswith("importseed="):
                    libraryScanner = caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]
                    if libraryScanner.count(" ") == 2:
                        importseed = libraryScanner.replace(" ","",1)
                        modifiedParamsList.append(f"importseed = {importseed}")
                    elif libraryScanner.count(" ") == 1:
                        importseed = libraryScanner
                        modifiedParamsList.append(f"importseed = {importseed}")
                    else:
                        print(RED+"ERROR: lethal spaces detected in importseed! "+YELLOW+"Try defining this parameter without any spaces inbetween (parameter=value)"+RESET)
                        paramexception = True
                elif i.replace(" ","").startswith("seed_ispacked=") or i.replace(" ","").startswith("seedispacked="):
                    if checkForBool(i.replace(" ","")) is not None:
                        seed_ispacked = checkForBool(i.replace(" ",""))
                        modifiedParamsList.append(f"seed_ispacked = {seed_ispacked}")
                    else:
                        paramexception= True
                elif i.replace(" ","").startswith("debug="):
                    if checkForBool(i.replace(" ","")) is not None:
                        debug = checkForBool(i.replace(" ",""))
                        modifiedParamsList.append(f"debug = {debug}")
                    else:
                        paramexception= True
                elif i.replace(" ","").startswith("encryptionamount="):
                    if checkForInt(i.replace(" ","")) is not None:
                        encryptionamount = checkForInt(i.replace(" ",""))
                        modifiedParamsList.append(f"encryptionamount = {encryptionamount}")
                    else:
                        paramexception = True
                elif i.replace(" ","").startswith("filelocation="):
                    if i.replace(" ","").split("=",1)[1].endswith(".enk"):
                        fileLocation = caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]
                        modifiedParamsList.append(f"fileLocation = {fileLocation}")
                        with open("preferences.json","w") as file:
                            Preferences["filelocation"] = fileLocation
                            json.dump(Preferences,file,indent=4)
                    elif "." in i.replace(" ","").split("=",1)[1]:
                        print(RED+f"ERROR: invalid filetype '{"." + caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1].split(".")[1]}'"+RESET)
                        print(YELLOW+"only '.enk' files are allowed to save enkripto data"+RESET)
                        paramexception = True
                    else:
                        print(RED+f"ERROR: invalid filetype '{i.replace(" ","").split("=",1)[1]}'"+RESET)
                        print(YELLOW+"only '.enk' files are allowed to save enkripto data"+RESET)
                        paramexception = True
                else:
                    if len(modifiedParamsList) > 0:
                        if debug:
                            print(modifiedParamsList)
                        print(RED+f"ERROR: invalid parameter definement ('{i}')"+RESET)
                        paramexception = True
            if len(params) > 0 and params[0] != "":
                if len(modifiedParamsList) > 0:
                    print(GREEN+"parameters succesfully modified: "+BLUE+f"{" , ".join(modifiedParamsList)}") if len(modifiedParamsList) > 1 else print(GREEN+"parameters succesfully modified: "+BLUE+f"{modifiedParamsList[0]}"+RESET)
                else:
                    print(RED+"ERROR:invalid or empty parameters provided."+RESET)
            else:
                print(RED+"ERROR: no parameters provided."+RESET)
    #encrypts the in the parameter provided message or file. msg= for raw text and target= for txts.
    elif prompt.lower().startswith("encrypt") or prompt.lower().startswith("encode"):
        params = prompt.lower().removeprefix("encrypt").split(",") if prompt.lower().startswith("encrypt") else prompt.lower().removeprefix("encode").split(",")
        caseSensitiveParams = prompt[7:].split(",")  if prompt.lower().startswith("encrypt") else prompt[6:].split(",")
        casesensitivecounter = 0
        if debug:
            print(params)
        paramexception: bool = False
        if len(params) > 0 and params[0] != "":
            modifiedParamsList = []
            paramexception = False
            for i in params:
                casesensitivecounter =+ 1
                if i.replace(" ","").startswith("msg="):
                    if library != "":
                        if caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1] != "" and " ":
                            print(BLUE+"encrypting..."+RESET)
                            print(GREEN+execute("encrypt", caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1], library,True)+RESET)
                        else:
                            print(RED+"ERROR: can't encrypt emptiness, broh... (msg was set to nothing)" + RESET)
                    else:
                        print(RED+"ERROR: no current library exists! "+YELLOW+"Please initiate first."+RESET)
                elif i.replace(" ","").startswith("target="):
                    if caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1].endswith(".txt"):
                        if library != "" and library is not None:
                            try:
                                print(f"encoding {caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]}...")
                                with open(caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1],"r") as file:
                                    target = file.read().replace(r"""
""", "²")
                                newContents = execute("encrypt", target, library, False)
                                if newContents is not None:
                                    with open(caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1],"w") as file:
                                        file.write(newContents)
                                        print(f"{caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]} successfully encoded!")
                            except FileNotFoundError:
                                print(RED+f"ERROR: File "+YELLOW+f"'{caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]}'"+RED+" does not exist in this directory."+RESET)
                        else:
                            print(RED+"ERROR: no current library exists! "+YELLOW+"Please initiate first."+RESET)
                    elif "." in caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]:
                        print(RED+"ERROR: Invalid file type "+YELLOW+f"'{caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1].split(".")[1]}'"+RESET)
                    else:
                        print(RED+"ERROR: invalid file type "+YELLOW+f"'{caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]}'"+RESET)
                else:
                    print(RED+f"ERROR: invalid parameter definement ('{i}')"+RESET)
                    paramexception = True
        else:
            print(RED+"no target message or file provided. "+YELLOW+"aborting..."+RESET)
    #deciphers the in the parameter provided message or file. msg= for raw text and target= for txts.
    elif prompt.lower().startswith("decipher") or prompt.lower().startswith("decode"):
        params = prompt.lower().removeprefix("decipher").split(",") if prompt.lower().startswith("decipher") else prompt.lower().removeprefix("decode").split(",")
        caseSensitiveParams = prompt[8:].split(",")  if prompt.lower().startswith("decipher") else prompt[6:].split(",")
        casesensitivecounter = 0
        if debug:
            print(params)
        paramexception: bool = False
        if len(params) > 0 and params[0] != "":
            modifiedParamsList = []
            paramexception = False
            for i in params:
                casesensitivecounter =+ 1
                if i.replace(" ","").startswith("msg="):
                    if library != "":
                        if caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1] != "" and " ":
                            print(BLUE+"decoding..."+RESET)
                            print(GREEN+execute("decipher", caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1], library,True)+RESET)
                        else:
                            print(RED+"ERROR: can't decipher emptiness, broh... (msg was set to nothing)" + RESET)
                    else:
                        print(RED+"ERROR: no current library exists! "+YELLOW+"Please initiate first."+RESET)
                elif i.replace(" ","").startswith("target="):
                    if caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1].endswith(".txt"):
                        if library != "" and library is not None:
                            try:
                                print(BLUE+"decoding "+GREEN+f"{caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]}"+BLUE+"..."+RESET)
                                with open(caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1],"r") as file:
                                    target = file.read()
                                newContents = execute("decipher", target, library, False)
                                if newContents is not None:
                                    with open(caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1],"w") as file:
                                        file.write(newContents.replace("²", r"""
"""))
                                print(GREEN+f"{caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]} successfully decoded!"+RESET)
                            except FileNotFoundError:
                                print(RED+"ERROR: File "+YELLOW+f"'{caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]}'"+RED+" does not exist in this directory."+RESET)
                        else:
                            print(RED+"ERROR: no current library exists! "+YELLOW+"Please initiate first."+RESET)
                    elif "." in caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]:
                        print(RED+"ERROR: Invalid file type "+YELLOW+f"'{caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1].split(".")[1]}'"+RESET)
                    else:
                        print(RED+"ERROR: invalid file type "+YELLOW+f"'{caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1]}'"+RESET)
                else:
                    print(RED+f"ERROR: invalid parameter definement ('{i}')"+RESET)
                    paramexception = True
        else:
            print(RED+"ERROR: no target message or file provided. aborting..."+RESET)
    elif prompt.lower().startswith("autoquery") or prompt.lower().startswith("aq"):
        params = prompt.lower().removeprefix("decipher").split(",") if prompt.lower().startswith("decipher") else prompt.lower().removeprefix("decode").split(",")
        caseSensitiveParams = prompt[8:].split(",")  if prompt.lower().startswith("decipher") else prompt[6:].split(",")
        casesensitivecounter = 0
        if debug:
            print(params)
        paramexception: bool = False
        if len(params) > 0 and params[0] != "":
            modifiedParamsList = []
            paramexception = False
            for i in params:
                casesensitivecounter =+ 1
                if i.replace(" ","").startswith("create"):
                    AQcreator()
    else:
        print(RED+"ERROR: unknown query: '"+YELLOW+f"{prompt.lower().split(" ")[0]}"+RED+"'"+RESET)

# to be honest i don't know what these used to do but they're great for reminiscing:
# createNew = True
# readFromENK = False
# custom_PackerLibrary = "$M+EIaA{5ßGCWxL-2mhBqkjX 8?(d6SO4p]\;zw²eo)u_<l|!§tFVQ[R.v'>`TZ=P#³r3/}NK:bH1~&UJsDY*g,7i%n90fcy"
# importseed = "171}8k1kSS}oW}8o}²8&k"
# seed_ispacked = True
# encryptionamount =random.randint(100,500) 
# packMySeed = True
