import random
import os
os.system("mode con: cols=120 lines=100")
os.system("color 04")
normallibrary="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ß!§$%&/()?`+*~#'<>|²³}]{[.-;_: ="
throwawaylibrary=normallibrary
library:str=""
print(r'''
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
                                                                $$$$$                                     ''')
print("-- ENKRIPTO v.0.2 --\ntype 'help' to see a list of commands or a command's function")

#MADE IN A DAY - EXPECT ERRORS AND BUGS


                    ###############
                    # DICTIONARY: #
                    ###############

# seed: the seed is a series of numbers that indicate procedures and parameters for the script to replicate the original circumstances. This way, the same en/decoding scheme can be used on different devices and/or instances.
# pack : packing refers to the extra encryption of the seed. it is encrypted (with a custom or default) library and then shuffled (by a custom or random amount). these are extra safety measures to allow the seed to be transferred safely
# library-layers : library-layers are shuffled versions of the alphabet ; An indefinite amount of them can be created, with each one of them encrypting itself using the previous one's properties. The last created layer is always the library that will be used for the main en-/de-coding.



                        ###########
                        # PARAMS: #
                        ###########

# createNew:  if True, creates new seed. readFromtxt,custom_Packer, importseed and seed_ispacked will be ignored, as these functions are used for importing existing seeds.
# readFromtxt: if you have a txt containing your data, enable this. otherwhise disable.
# custom_PackerLibrary: only used if readFromtx = False, custom library that was used to pack this seed
# importseed: only used if readFromtx = False ; the seed you used, if it is packed, enable seed_ispacked. otherwhise disable.  A packed seed looks like this :  11QT'`V>'`TQV[>nQ[Vn    ; An unpacked seed looks like this:   902138.231.2079187
# seed_ispacked: set to true if the seed you provided is packed, otherwhise set to false
# encryptionamount: amount of encryption layers
# PackMySeed: if True, packs the seed before displaying. set this to True if you want an extra layer of encryption. This will encrypt and shuffle the seed with a custom or default library. if false, displays pure seed

createNew: bool = True
readFromtxt: bool = False
custom_PackerLibrary: str = r"O~m]c&³?b3v|$1a(<j%!xY/By2+{:;P=4`_r8l}hCitW.fgKow>F[LkzqA7ßVIJQ6'D-usUd9EHRTGS0 n²#Xe5)*§pMZN"
importseed: str = r"171}8k1kSS}oW}8o}²8&k"
seed_ispacked: bool = True
encryptionamount: int =random.randint(100,500) 
packMySeed: bool = True
fileLocation:str = "packerLibrary.txt"

debug = False

# used to exit upon self-raised errors
def StopFunc(func: str):
    print(f"'{func}' Function execution aborted.")

# use this to either reset or create the txt file with default values
def resetFile():
    with open(fileLocation,"w",encoding="utf-8") as file:
        file.write(r"171}8k1kSS}oW}8o}²8&k@O~m]c&³?b3v|$1a(<j%!xY/By2+{:;P=4`_r8l}hCitW.fgKow>F[LkzqA7ßVIJQ6'D-usUd9EHRTGS0 n²#Xe5)*§pMZN")
    print("file reset")

# restores correct order in seeds.
def cleanse(providedSeed):
        cleanedSeed = ""
        try:
            formatter = int(providedSeed[:2])
        except ValueError:
            print("ERROR in Cleanse() ; invalid seed imported")
            return None
        rest = (providedSeed[2:])
        for u in range(formatter):
            rest = rest[-1] + rest[:-1]
        cleanedSeed = rest
        return cleanedSeed
#this function is called by makeLibrary() to create each commercial and the initial layer(s)
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
def execute(method:str ="encrypt", message:str = "lorem ipsum", library:str = r"O~m]c&³?b3v|$1a(<j%!xY/By2+{:;P=4`_r8l}hCitW.fgKow>F[LkzqA7ßVIJQ6'D-usUd9EHRTGS0 n²#Xe5)*§pMZN", outputMode:bool = False):
    if method == "encrypt":
        encrypted_message = ""
        if outputMode:
            print("provided message to encrypt:")
            print(message)
        if debug:
            print(normallibrary)
        for i in message:
            try:
                location = normallibrary.index(i)
            except ValueError:
                return print(f"ERROR: the Enkripto library currently does not support use of the character '{i}'. Please make sure to leave this particular character out during your next attempt")
            encrypted_message += library[location]
        if outputMode:
            print("encrypted message:")
            return encrypted_message
    elif method == "decrypt" or method == "decipher":
        decrypted_message = ""
        if outputMode:
            print("provided message to decode:")
            print("message")
        if debug:
            print(library)
        for i in message:
            try:
                location = library.index(i)
            except ValueError:
                return print(f"ERROR: the Enkripto library currently does not support use of the character '{i}'. Please make sure to leave this particular character out during your next attempt")
            decrypted_message += normallibrary[location]
        if outputMode:
            print("decoded message:")
            return decrypted_message
    else:
        return print(f"invalid param '{method}'")

# this is the initial creation and definition of important variables
def makeLibrary():
    global SeedInUse1
    global importseed
    global library
    if createNew:
        print("creating new seed...")
        library = createLibrary(normallibrary, random.randint(100,9999999), "init")
        createLibrary(library , random.randint(100,9999999) , "commercial")
        for i in range(encryptionamount):
            library = createLibrary(library , random.randint(100,9999999),"none")
        SeedInUse1 = str(initseed) + "." + str(encryptionamount) + "." + str(commercialseed)
        print("layers:")
        print(encryptionamount)
        print("library in use:")
        print(library)
        print("seed in use:")
        print(SeedInUse1)
    elif readFromtxt or importseed:
        if readFromtxt:
            try:
                with open(fileLocation,"r",encoding="utf-8") as file:
                    content = file.read()
                    importseed = content.split("@")[0]
                    if seed_ispacked:
                        packerLibrary = content.split("@")[1]
            except FileNotFoundError:
                print("no packerLibrary file exists. creating new Default...")
                with open(fileLocation,"w",encoding="utf-8") as file:
                    file.write(r"171}8k1kSS}oW}8o}²8&k@O~m]c&³?b3v|$1a(<j%!xY/By2+{:;P=4`_r8l}hCitW.fgKow>F[LkzqA7ßVIJQ6'D-usUd9EHRTGS0 n²#Xe5)*§pMZN")
                    importseed = "16{V*`{*fs`A;sV*;{{s{"
                    if seed_ispacked:
                        packerLibrary = r"O~m]c&³?b3v|$1a(<j%!xY/By2+{:;P=4`_r8l}hCitW.fgKow>F[LkzqA7ßVIJQ6'D-usUd9EHRTGS0 n²#Xe5)*§pMZN"
            except IndexError:
                print("ERROR in txtReader1 ; packerlibrary file format is invalid.")
                StopFunc("init")
                return
        else:
            print(f"reading {fileLocation} disabled. reading manual seed...")
            if seed_ispacked:
                if len(custom_PackerLibrary) == len(normallibrary):
                    packerLibrary = custom_PackerLibrary
                else:
                    print("no/invalid custom_PackerLibrary provided. creating new Default...")
                    packerLibrary = r"O~m]c&³?b3v|$1a(<j%!xY/By2+{:;P=4`_r8l}hCitW.fgKow>F[LkzqA7ßVIJQ6'D-usUd9EHRTGS0 n²#Xe5)*§pMZN"
        print("provided seed: " + importseed)
        if seed_ispacked:
            if cleanse(importseed) is not None:
                cleansedSeed = cleanse(importseed)
                print("cleansed seed: " + cleansedSeed)
                CleansedAndDecodedSeed = execute("decrypt", cleansedSeed,packerLibrary)
                print("decoded seed: " + CleansedAndDecodedSeed)
            else:
                StopFunc("init")
                return
        try:
            getinitseed , getencryptionamount, getCommercialSeed = CleansedAndDecodedSeed.split(".") if seed_ispacked else cleansedSeed.split(".")
        except ValueError:
            print("ERROR in getSeedValues ; invalid seed provided!")
            return
        try:
            getinitseed = int(getinitseed)
            getencryptionamount = int(getencryptionamount)
            getCommercialSeed = int(getCommercialSeed)
        except ValueError:
            print("ERROR in convertSeedValues ; invalid seed provided!")
            StopFunc("init")
            return
        library=createLibrary(normallibrary, getinitseed, "init")
        createLibrary(library, getCommercialSeed, "commercial")
        for i in range(getencryptionamount):
            library = createLibrary(library, random.randint(100,9999999), "commercial")
        SeedInUse1 = CleansedAndDecodedSeed if seed_ispacked else cleansedSeed
        print("library in use:")
        print(library)
        print("seed in use:")
        print(SeedInUse1)
        print("encryption layer amount:")
        print(encryptionamount)


#this function packs all seeds provided (see dictionary)
#params:
# UsedSeed: the seed you want to pack
def packSeed(UsedSeed: str,outputMode: bool):
    global packerLibrary
    if readFromtxt:
        try:
            with open(fileLocation,"r",encoding="utf-8") as file:
                packerLibrary = file.read().split("@")[1]
        except FileNotFoundError:
            if outputMode:
                print("no packerLibrary file exists. creating new Default...")
            with open(fileLocation,"w",encoding="utf-8") as file:
                file.write(r"171}8k1kSS}oW}8o}²8&k@O~m]c&³?b3v|$1a(<j%!xY/By2+{:;P=4`_r8l}hCitW.fgKow>F[LkzqA7ßVIJQ6'D-usUd9EHRTGS0 n²#Xe5)*§pMZN")
                packerLibrary = r"O~m]c&³?b3v|$1a(<j%!xY/By2+{:;P=4`_r8l}hCitW.fgKow>F[LkzqA7ßVIJQ6'D-usUd9EHRTGS0 n²#Xe5)*§pMZN"
        except IndexError:
            if outputMode:
                print("ERROR in txtReader2 ; packerlibrary file format is invalid.")
            return None 
        else:
            if outputMode:
                print("invalid custom_PackerLibrary")
            return None
    elif len(custom_PackerLibrary) == len(normallibrary):
        packerLibrary = custom_PackerLibrary
    else:
        if outputMode:
            print("no custom_packerLibrary exists. creating new Default...")
        with open(fileLocation,"w",encoding="utf-8") as file:
            file.write(r"171}8k1kSS}oW}8o}²8&k@O~m]c&³?b3v|$1a(<j%!xY/By2+{:;P=4`_r8l}hCitW.fgKow>F[LkzqA7ßVIJQ6'D-usUd9EHRTGS0 n²#Xe5)*§pMZN")
            packerLibrary = r"O~m]c&³?b3v|$1a(<j%!xY/By2+{:;P=4`_r8l}hCitW.fgKow>F[LkzqA7ßVIJQ6'D-usUd9EHRTGS0 n²#Xe5)*§pMZNy"
    encryptedSeed = execute("encrypt", UsedSeed, packerLibrary)
    shuffleBy = random.randint(0, len(encryptedSeed)-1)
    for e in range(shuffleBy):
        encryptedSeed += encryptedSeed[0]
        encryptedSeed = encryptedSeed[1:]
    return "0" + str(shuffleBy) + encryptedSeed if len(str(shuffleBy)) == 1 else str(shuffleBy) + encryptedSeed

#displays the seed, duh. either packed or raw
def displaySeed():
    print("displaying seed in use...")
    if packMySeed:
        if packSeed(SeedInUse1,False) is not None:
            print("seed is packed:")
            print("--->   " + packSeed(SeedInUse1,False) + "   <---")
        else:
            StopFunc("displayseed")
            return
    else:
        print("seed is unpacked:")
        print(SeedInUse1)

#transfers your current seed and packerlibrary to the txt file, overwrites previous values
def writeToTXT():
    print("writing packed seed and packerLibrary into packerlibrary.txt ...")
    try:
        test = SeedInUse1
    except NameError:
        print("seed has not been defined yet. Try initiating before saving.")
        return
    try:
        test1 = packerLibrary
    except NameError:
        print("packerLibrary has not been defined yet. Packing seed...")
    if packSeed(SeedInUse1,False) is not None:
        with open(fileLocation,"w",encoding="utf-8") as file:
            file.write(packSeed(SeedInUse1,True) + "@" + packerLibrary)
    else:
        StopFunc("save/write")
        return
    print("successfully written data to txt")

def checkForBool(item: str):
    if item.split("=")[1] == "true" or item.split("=",1)[1] == "1":
        return True
    if item.split("=")[1] == "false" or item.split("=",1)[1] == "0":
        return False
    print(f"expected Boolean value (true/false/1/0) and got faulty value ('{item}')")
    return None

def checkForInt(item: str):
    try:
        intitem= int(item.split("=",1)[1])
        return intitem
    except ValueError:
        print(f"expected integer value and got faulty value ('{item}')")
        return None
#this is an example of what a workflow could look like:
# resetFile()
# makeLibrary()
# displaySeed()
# print(execute("decipher","5abB{5hbjLmGhb5WW$bh{5BbW b-$xBh"))



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
    prompt = input("NHH: awaiting input >  ")

        #####################
        #HELP RELATED TOPICS#
        #####################
    
    #CHECKING FOR help REQUEST
    if prompt.lower() == "help":
        print("\n-- HELP MENU --")
        print('type "help" followed by a certain command or term to view advanced information about it (type "help list" to view all terms that have help data)\n') 
        print('type "explain" to receive a tutorial on how to use ENKRIPTO\n') # TODO
        print("capitalization doesn't matter\n")
        print("Enkripto uses it's own mini parsing language: NHH - Native Handling Hub\n")
        print("parameters: {parameter_name: parameter_type} ; function aliases: name1 / name2  (either works. just pick the one you prefer)\n")
        print("to see all parameters, type 'all.params'\n")
        print("parameter order does not matter\n")
        print('refrain from using any quotation marks in your prompts. strings are interpreted as such by default and will thus end up containing extra quotations mark in them, making them uninterpretable. if you set your seed to importseed = "123.456.789", the value will be ""123.456.789"".\n')
        print("the underscore ( _ ) can be left out in parameter names ( seed_ispacked = seedispacked )\n")
        print("If parameters are not provided ENKRIPTO will vent to defaults \n")
        print("-- COMMANDS --\n")
        print("resetfile - resets the txt file to default values\n")
        print("initiate / init {createnew: bool} , {readfromtxt: bool} , {filelocation: str} , {custom_packerlibrary: str} , {seed_ispacked: bool} , {encryptionamount: int} , {packmyseed: bool} - initiates ENKRIPTO's library (re)creation process;\n⤤ type 'help initiate' or 'help init' for a parameter explanation\n")
        print("(function).params - shows a function's params and their current values \n") 
        print("save / write {filelocation: str} - packs and saves current seed in a txt.\n⤤ type 'help save' or 'help write' for a parameter explanation\n")
        print("displayseed / display {packmyseed / pack: bool} - displays the current seed in use. if packmyseed / pack is true, it will be displayed as a packed seed. Otherwhise it will be displayed in it's natural form.\n")
        print("scan / list / ls - scans and lists current directory to make locating your save .txt file easier.\n")
        print("currentpath / cwd / currentdir - displays your work directory's path.\n")
        print("restoredefaults / defaults / default - restores all parameters to their default values.\n")
        print("exit - closes the program\n")
        print("setparams / setparam {createnew: bool} , {packmyseed / pack: bool} , {custom_packerlibrary / custompackerlibrary: str} , {importseed: str} , {seed_ispacked / seedispacked: bool} , {debug: bool} , {encryptionamount: int} , {filelocation: str} - command used to change certain parameters without executing any other functions. The debug parameter is a developer tool that shows extra information. Enabling it isn't recommended.\n")
        print("encrypt / encode {msg / target: str} - encrypts the provided target message using your library.\n")
        print("decipher / decode {msg / target: str} - decodes the provided target message using your library.\n")
    #CHECKING FOR help REQUESTS AND FURTHER ARGS
    elif prompt.lower() == "help initiate" or prompt.lower() == "help init":
        print("-- ADVANCED HELP MENU - ENTRY 01 --\n")
        print("INIT(IATE) FUNCTION:\n")
        print("general info:\nthe initiate function is used to kickstart the process of generating your library and seed. It is highly customizeable due to it's variety in different parameters (params). It is imperative that this function has been called before any other functions may run because it sets the baseline for any other further tools this module contains. It can not only create a new library and seed etc. , but it can also be used to import already existing seed-data, either from a .txt file, or using the data's manual input. your choice.\n")
        print("parameters:\n")
        print("NAME:\ncreatenew\nTYPE:\nBool\nUSECASE:\nif set to True, an entirely new seed and library will be generated in the initiation process. given data like readfromtxt, importseed, custompackerlibrary and more will be ignored, however params used solely for creation like encryptionamount will be utilized. If it is set to False, the initiation process will try to import any given values. It will first check if readfromtxt is enabled (if so it will import the values from the .txt file) and then check for custom values (if none exist, hardcoded default values will be used. I advise against this, because encrypto relies on the diversity of it's encryption schemes, so using a singular fixed library and/or seed might bring up safety issues.)")
        print("\nNAME:\nreadfromtxt\nTYPE:\nBool\nUSECASE:\nif set to True (and createnew is set to false), values will be read from the provided .txt file")
        print("\nNAME:\nfilelocation\nTYPE:\nString\nUSECASE:\nthe .txt seed-data file's path. the default is 'packerLibrary.txt' but you can expand the path in any way or even provide a file in a completely different directory.")
        print("\nNAME:\nimportseed\nTYPE:\nString\nUSECASE:\nparameter used for manual import of a seed. If you insert a packed seed, you must enable seed_ispacked and vice versa. Otherwhise the program will fail. NOTE that it is suggested to not use any spaces when defining this parameter (parameter=value)")
        print("\nNAME:\ncustom_packerlibrary\nTYPE:\nString\nUSECASE:\nparameter used for manual import of the library used to pack the manually imported seed. This parameter is only necessary if the seed you manually provided is packed.  NOTE that it is suggested to not use any spaces when defining this parameter (parameter=value)")
        print("\nNAME:\nseed_ispacked\nTYPE:\nBool\nUSECASE:\nIf you manually import a seed, you will have to set seed_ispacked to the corresponding value depending on if it is packed or not. if the provided seed is packed : seed_ispacked = True ; if it is not packed : seed_ispacked = False")
        print("\nNAME:\nencryptionamount\nTYPE:\nInt\nUSECASE:\nparameter that defines the amount of times your library will encrypt itself. This param is only used when creating a new library and it's default is a random integer.")
        print("\nNAME:\nfilelocation\nTYPE:\nString\nThe path to your mounted txt. This can be an absolute path (C:\myprojects/txtfiles/save.txt) or a relative path (txtfiles/save.txt (if you are currently in the myprojects directory)). If you don't have a txt yet, one will be created for you if you execute the 'save' command after initiating")
    elif prompt.lower() == "help list":
        print("-- LIST OF ALL COMMANDS WITH HELP DATA --\n")
        print("01 - INIT(IATE)\n")
        print("02 - SAVE / WRITE\n")
        print("03 - SEEDS\n")
        print("04 - LIBRARIES\n")
        print("-- MORE TO COME --")
    elif prompt.lower() == "explain":
        print("ENKRIPTO tutorial:")
        print("https://youtu.be/76r2yHeQkC8")
        ######################
        #PARAM RELATED TOPICS#
        ######################
    elif prompt.lower() == "help save" or prompt.lower() == "help write":
        print("-- ADVANCED HELP MENU - ENTRY 02 --\n")
        print("SAVE / WRITE FUNCTION:\n")
        print("general info:\nthe save function saves your current seed in it's packed form and the library used to pack it in a .txt file of your choice. This allows for easier sharing of your seed-data, so that others can decode your previously encrypted messages easier.\n")
        print("parameters:")
        print("\nNAME:\nfilelocation\nTYPE:\nString\nThe path to your mounted txt. This can be an absolute path (C:\myprojects/txtfiles/save.txt) or a relative path (txtfiles/save.txt (if you are currently in the myprojects directory)). If you don't have a txt yet, one will be created for you if you execute the 'save' command after initiating")
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
        print(f"readFromtxt = {readFromtxt}")
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
        print("- showing all params -")
        print(f"createNew = {createNew}")
        print(f"readFromtxt = {readFromtxt}")
        print(f"fileLocation = {fileLocation}")
        print(f"custompackerlibrary = {custom_PackerLibrary}")
        print(f"importseed = {importseed}")
        print(f"seed_ispacked = {seed_ispacked}")
        print(f"encryptionamount = {encryptionamount}")
        print(f"fileLocation = {fileLocation}")
        print(f"packMySeed = {packMySeed}")
        ##########
        #COMMANDS#
        ##########
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
                    else:
                        paramexception = True
                elif i.replace(" ","").startswith("readfromtxt="):
                    if checkForBool(i.replace(" ","")) is not None:
                        readFromtxt =checkForBool(i.replace(" ",""))
                        modifiedParamsList.append(f"readFromtxt = {readFromtxt}")
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
                        print("lethal spaces detected in custom_packerlibrary! Try defining this parameter without any spaces inbetween (custompackerlibrary=...)")
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
                        print("lethal spaces detected in importseed! Try defining this parameter without any spaces inbetween (parameter=value)")
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
                    fileLocation = i.replace(" ","").split("=",1)[1]
                    modifiedParamsList.append(f"fileLocation = {fileLocation}")
                else:
                    if len(modifiedParamsList) > 0:
                        if debug:
                            print(modifiedParamsList)
                        print(f"parameters succesfully modified: {" , ".join(modifiedParamsList)}") if len(modifiedParamsList) > 1 else print(f"parameters succesfully modified: {modifiedParamsList[0]}")
                    print(f"invalid parameter definement ('{i}')")
                    paramexception = True
        if paramexception:
            print("initiation aborted.")
        else:
            if len(params) > 0 and params[0] != "":
                print(f"parameters succesfully modified: {" , ".join(modifiedParamsList)}") if len(modifiedParamsList) > 1 else print(f"parameters succesfully modified: {modifiedParamsList[0]}")
            makeLibrary()
    elif prompt.lower() == "scan" or prompt.lower() =="list" or prompt.lower() =="ls":
        print("displaying files and directories in current directory:")
        for file in os.listdir():
            if os.path.isdir(file):
                print(f"DIR : {file}")
            else:
                print(f"FILE: {file}")
    elif prompt.lower() =="currentpath" or prompt.lower() =="cwd" or prompt.lower() =="currentdir":
        print(f"current directory: {os.getcwd()}")
    elif prompt.lower() =="restoredefaults" or prompt.lower() == "default" or prompt.lower() == "defaults":
        createNew = True
        readFromtxt = False
        custom_PackerLibrary = r"O~m]c&³?b3v|$1a(<j%!xY/By2+{:;P=4`_r8l}hCitW.fgKow>F[LkzqA7ßVIJQ6'D-usUd9EHRTGS0 n²#Xe5)*§pMZN"
        importseed = r"171}8k1kSS}oW}8o}²8&k"
        seed_ispacked = True
        encryptionamount =random.randint(100,500) 
        packMySeed = True
        fileLocation = "packerLibrary.txt"
        print("defaulting...\nsome true values are excluded due to their length:")
        print(f"createnew = {createNew} \nreadfromtxt = {readFromtxt}\ncustom_packerlibrary = (default value)\nimportseed = (defaultvalue)\nseed_ispacked = {seed_ispacked}\nencryptionamount = {encryptionamount} (randomized)\npackmyseed = {packMySeed}\nfilelocation = {fileLocation}")
        print("defaults restored!")
    elif prompt.lower() == "exit":
        print("See you next time!")
        exit()
    elif prompt.lower().startswith("save") or prompt.lower().startswith("write"):
        params = prompt.lower().removeprefix("save").replace(" ","").split(",") if prompt.lower().startswith("save") else prompt.lower().removeprefix("write").replace(" ","").split(",")
        if debug:
            print(params)
        paramexception = False
        if len(params) > 0 and params[0] != "":
            modifiedParamsList = []
            paramexception = False
            for i in params:
                if i.replace(" ","").startswith("filelocation="):
                    fileLocation = i.replace(" ","").split("=",1)[1]
                    modifiedParamsList.append(f"fileLocation = {fileLocation}")
                else:
                    if len(modifiedParamsList) > 0:
                        if debug:
                            print(modifiedParamsList)
                        print(f"parameters succesfully modified: {" , ".join(modifiedParamsList)}") if len(modifiedParamsList) > 1 else print(f"parameters succesfully modified: {modifiedParamsList[0]}")
                    print(f"invalid parameter definement ('{i}')")
                    paramexception = True
        if paramexception:
            print("initiation aborted.")
        else:
            if len(params) > 0 and params[0] != "":
                print(f"parameters succesfully modified: {" , ".join(modifiedParamsList)}") if len(modifiedParamsList) > 1 else print(f"parameters succesfully modified: {modifiedParamsList[0]}")
            writeToTXT()
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
                        print(f"parameters succesfully modified: {" , ".join(modifiedParamsList)}") if len(modifiedParamsList) > 1 else print(f"parameters succesfully modified: {modifiedParamsList[0]}")
                    print(f"invalid parameter definement ('{i}')")
                    paramexception = True
        if paramexception:
            print("initiation aborted.")
        else:
            if len(params) > 0 and params[0] != "":
                print(f"parameters succesfully modified: {" , ".join(modifiedParamsList)}") if len(modifiedParamsList) > 1 else print(f"parameters succesfully modified: {modifiedParamsList[0]}")
            displaySeed()
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
                    else:
                        paramexception = True
                elif i.replace(" ","").startswith("packmyseed=") or i.replace(" ","").startswith("pack="):
                    packMySeed = checkForBool(i.replace(" ",""))
                    modifiedParamsList.append(f"packMySeed = {packMySeed}")
                elif i.replace(" ","").startswith("readfromtxt="):
                    if checkForBool(i.replace(" ","")) is not None:                        
                        readFromtxt =checkForBool(i.replace(" ",""))
                        modifiedParamsList.append(f"readFromtxt = {readFromtxt}")
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
                        print("lethal spaces detected in custom_packerlibrary! Try defining this parameter without any spaces inbetween (parameter=value)")
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
                        print("lethal spaces detected in importseed! Try defining this parameter without any spaces inbetween (parameter=value)")
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
                    fileLocation = i.replace(" ","").split("=",1)[1]
                    modifiedParamsList.append(f"fileLocation = {fileLocation}")
                else:
                    if len(modifiedParamsList) > 0:
                        if debug:
                            print(modifiedParamsList)
                        print(f"invalid parameter definement ('{i}')")
                        paramexception = True
            if len(params) > 0 and params[0] != "":
                if len(modifiedParamsList) > 0:
                    print(f"parameters succesfully modified: {" , ".join(modifiedParamsList)}") if len(modifiedParamsList) > 1 else print(f"parameters succesfully modified: {modifiedParamsList[0]}")
                else:
                    print("invalid parameters provided.")
            else:
                print("no parameters provided.")
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
                if i.replace(" ","").startswith("msg=") or i.replace(" ","").startswith("target="):
                    if library != "":
                        print("encrypting...")
                        print("ENCRYPTED MESSAGE:")
                        print(execute("encrypt", caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1], library,True))
                    else:
                        print("no current library exists! Please initiate first.")
                else:
                    print(f"invalid parameter definement ('{i}')")
                    paramexception = True
        else:
            print("no target message provided. aborting...")
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
                if i.replace(" ","").startswith("msg=") or i.replace(" ","").startswith("target="):
                    if library != "":
                        print("decoding...")
                        print("DECODED MESSAGE:")
                        print(execute("decipher", caseSensitiveParams[casesensitivecounter - 1].split("=",1)[1], library,True))
                    else:
                        print("no current library exists! Please initiate first.")
                else:
                    print(f"invalid parameter definement ('{i}')")
                    paramexception = True
        else:
            print("no target message provided. aborting...")
# createNew = True
# readFromtxt = False
# custom_PackerLibrary = "$M+EIaA{5ßGCWxL-2mhBqkjX 8?(d6SO4p]\;zw²eo)u_<l|!§tFVQ[R.v'>`TZ=P#³r3/}NK:bH1~&UJsDY*g,7i%n90fcy"
# importseed = "171}8k1kSS}oW}8o}²8&k"
# seed_ispacked = True
# encryptionamount =random.randint(100,500) 
# packMySeed = True
