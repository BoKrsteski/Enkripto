import random
import sys

normallibrary="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ß!§$%&/()=?` +*~#'<>|²³}]{[,.-;_:"
throwawaylibrary=normallibrary
print("-- cryptero v.0.1 --")
print("")


#                           s@S$$S@s                    ,@S$$S.               s@S$$S@s                    
#    ,sS$S@go_              $$$$$$$'       ,sS$S@S$s,_  $$$$$$$    ,sS$S@go,  $$$$$$$'         ,sS$S@go,  
#  ,s$$$$$$$$$$,sS$S@S$s,_  `$$$$$'  .,$$$$$$$$$  o$$$s,`$$$$P'  ,s$$$$$$$$$, `$$$$$,        ,s$$$$$$$$$, 
#  $$$$$' )$$$s$$$$$  $$$$s, $$$$$  $$$$$²'$$$$l `$$$$$P         $$$$$$l$$$$s $$$$$$%S$S;    $$$$$$l$$$$s 
#  $$$$' o$$$P'$$$$l   `$$$$ $$$$$%$s²"`_  $$$$$  `"""" od$$$bo. $$$$l' `$$$$,`$$$$$"²╙'     $$$$l' `$$$$,
#  $$$$,$"'"   $$$$$   ,$$$$ $$$$iP²╙$$$$$,$$$$$$       .l$$$i   $$$$$   $$$$$ l$$$i         $$$$,   $$$$$
#  $$$$$s.,$$$$$$$$$$  $$$$$ $$$$$   `$$$$$$$$$$$       $$$$$$,o.$$$$$ .,$$$$  $$$$$, _,b$$$$$$$$$s.,$$$$ 
#   `²$$$$$$$²' `²$$$  $$$$$ $$$$$   ,$$$$$`$²$$$       4$$$$$$b)$$$$$ $$$$²'  $$$$$$Sb$$$$$' `²$$$$$$$²' 
#      `"²"`           `²$ⁿ' `²$$$  ,$$$$$'  `""         `4$$$$" $$$$$ `$`     `²$²"^²$$$²'      `"²"`    
#                                   gV$$²'                       $$$$$                                    
#                                                                $$$$$                                    
#                                                                $$$$$                                             

#MADE IN A DAY - EXPECT ERRORS AND BUGS


                    ###############
                    # DICTIONARY: #
                    ###############

# seed: the seed is a series of numbers that indicate procedures and parameters for the script to replicate the original circumstances. This way, the same en/decoding scheme can be used on different devices.
# pack : packing refers to the extra encryption of the seed. it is encrypted (with a custom or default) library and then shuffled (by a custom or random amount). these are extra safety measures to allow the seed to be transferred safely
# library-layers : library-layers are shuffled versions of the alphabet ; An indefinite amount of them can be created, with each one of them encrypting itself using the previous one's properties. The last created layer is always the library that will be used for the main en-/de-coding.



                        ###########
                        # PARAMS: #
                        ###########

# createNew:  if True, creates new seed. readFromtxt,custom_Packer, importseed and seed_ispacked will be ignored, as these functions are used for importing existing seeds.
# readFromtxt: if you have a txt containing your data, enable this. otherwhise disable.
# custom_PackerLibrary: only used if readFromtx = False, custom library that was used to pack this seed
# importseed: the seed you used, if it is packed, enable seed_ispacked. otherwhise disable.  A packed seed looks like this :  11QT'`V>'`TQV[>nQ[Vn    ; An unpacked seed looks like this:   902138.231.2079187
# seed_ispacked: set to true if the seed you provided is packed, otherwhise set to false
# encryptionamount: amount of encryption layers
# PackMySeed: if True, packs the seed before displaying. set this to True if you want an extra layer of encryption. This will encrypt and shuffle the seed with a custom or default library. if false, displays pure seed

createNew = False
readFromtxt = False
custom_PackerLibrary = "$M+EIaA{5ßGCWxL-2mhBqkjX 8?(d6SO4p]\;zw²eo)u_<l|!§tFVQ[R.v'>`TZ=P#³r3/}NK:bH1~&UJsDY*g,7i%n90fcy"
importseed = "06QnR'>n'V[R'TQV>.[>v"
seed_ispacked = True
encryptionamount =random.randint(100,500) 
packMySeed = True



# used to exit upon self-raised errors
def endProgram():
    raise Exception("program was stopped")

# use this to either reset or create the txt file with default values
def resetFile():
    with open("packerLibrary.txt","w",encoding="utf-8") as file:
        file.write("16{V*`{*fs`A;sV*;{{s{@$M+EIaA{5ßGCWxL-2mhBqkjX 8?(d6SO4p]\;zw²eo)u_<l|!§tFVQ[R.v'>`TZ=P#³r3/}NK:bH1~&UJsDY*g,7i%n90fcy")
    print("file reset")

# restores correct order in seeds.
def cleanse(providedSeed):
        cleanedSeed = ""
        try:
            formatter = int(providedSeed[:2])
        except ValueError:
            print("ERROR in Cleanse() ; invalid seed imported")
            endProgram()
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
def execute(method:str ="encrypt", message:str = "lorem ipsum", library:str = "$M+EIaA{5ßGCWxL-2mhBqkjX 8?(d6SO4p]\;zw²eo)u_<l|!§tFVQ[R.v'>`TZ=P#³r3/}NK:bH1~&UJsDY*g,7i%n90fcy"):
    if method == "encrypt":
        encrypted_message = ""
        for i in message:
            location = normallibrary.index(i)
            encrypted_message += library[location]
        return encrypted_message
    elif method == "decrypt" or method == "decipher":
        decrypted_message = ""
        for i in message:
            location = library.index(i)
            decrypted_message += normallibrary[location]
        return decrypted_message
    else:
        return print(f"invalid param '{method}'")

# this is the initial creation and definition of important variables
def makeLibrary():
    global SeedInUse1
    global importseed
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
                with open("packerLibrary.txt","r",encoding="utf-8") as file:
                    content = file.read()
                    importseed = content.split("@")[0]
                    if seed_ispacked:
                        packerLibrary = content.split("@")[1]
            except FileNotFoundError:
                print("no packerLibrary file exists. creating new Default...")
                with open("packerLibrary.txt","w",encoding="utf-8") as file:
                    file.write("16{V*`{*fs`A;sV*;{{s{@$M+EIaA{5ßGCWxL-2mhBqkjX 8?(d6SO4p]\;zw²eo)u_<l|!§tFVQ[R.v'>`TZ=P#³r3/}NK:bH1~&UJsDY*g,7i%n90fcy")
                    importseed = "16{V*`{*fs`A;sV*;{{s{"
                    if seed_ispacked:
                        packerLibrary = "$M+EIaA{5ßGCWxL-2mhBqkjX 8?(d6SO4p]\;zw²eo)u_<l|!§tFVQ[R.v'>`TZ=P#³r3/}NK:bH1~&UJsDY*g,7i%n90fcy"
            except IndexError:
                print("ERROR in txtReader1 ; packerlibrary file format is invalid.")
                endProgram()
        else:
            print("reading PackerLibrary disabled. reading manual seed...")
            if seed_ispacked:
                if custom_PackerLibrary:
                    packerLibrary = custom_PackerLibrary
                else:
                    print("no custom_PackerLibrary provided. creating new Default...")
                    packerLibrary = "$M+EIaA{5ßGCWxL-2mhBqkjX 8?(d6SO4p]\;zw²eo)u_<l|!§tFVQ[R.v'>`TZ=P#³r3/}NK:bH1~&UJsDY*g,7i%n90fcy"
        print("provided seed: " + importseed)
        if seed_ispacked:
            cleansedSeed = cleanse(importseed)
            print("cleansed seed: " + cleansedSeed)
            CleansedAndDecodedSeed = execute("decrypt", cleansedSeed,packerLibrary)
            print("decoded seed: " + CleansedAndDecodedSeed)
        try:
            getinitseed , getencryptionamount, getCommercialSeed = CleansedAndDecodedSeed.split(".") if seed_ispacked else cleansedSeed.split(".")
        except ValueError:
            print("ERROR in getSeedValues ; invalid seed provided!")
            endProgram()
        try:
            getinitseed = int(getinitseed)
            getencryptionamount = int(getencryptionamount)
            getCommercialSeed = int(getCommercialSeed)
        except ValueError:
            print("ERROR in convertSeedValues ; invalid seed provided!")
            endProgram()
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
def packSeed(UsedSeed: str):
    global packerLibrary
    if readFromtxt:
        try:
            with open("packerLibrary.txt","r",encoding="utf-8") as file:
                packerLibrary = file.read().split("@")[1]
        except FileNotFoundError:
            print("no packerLibrary file exists. creating new Default...")
            with open("packerLibrary.txt","w",encoding="utf-8") as file:
                file.write("16{V*`{*fs`A;sV*;{{s{@$M+EIaA{5ßGCWxL-2mhBqkjX 8?(d6SO4p]\;zw²eo)u_<l|!§tFVQ[R.v'>`TZ=P#³r3/}NK:bH1~&UJsDY*g,7i%n90fcy")
                packerLibrary = "$M+EIaA{5ßGCWxL-2mhBqkjX 8?(d6SO4p]\;zw²eo)u_<l|!§tFVQ[R.v'>`TZ=P#³r3/}NK:bH1~&UJsDY*g,7i%n90fcy"
        except IndexError:
            print("ERROR in txtReader2 ; packerlibrary file format is invalid.")
            endProgram()
            with open("packerLibrary.txt","w",encoding="utf-8") as file:
                file.write(custom_PackerLibrary)
                packerLibrary = custom_PackerLibrary
        else:
            print("invalid custom_PackerLibrary")
            endProgram()
    else:
        print("no custom_packerLibrary exists. creating new Default...")
        with open("packerLibrary.txt","w",encoding="utf-8") as file:
            file.write("16{V*`{*fs`A;sV*;{{s{@$M+EIaA{5ßGCWxL-2mhBqkjX 8?(d6SO4p]\;zw²eo)u_<l|!§tFVQ[R.v'>`TZ=P#³r3/}NK:bH1~&UJsDY*g,7i%n90fcy")
            packerLibrary = "$M+EIaA{5ßGCWxL-2mhBqkjX 8?(d6SO4p]\;zw²eo)u_<l|!§tFVQ[R.v'>`TZ=P#³r3/}NK:bH1~&UJsDY*g,7i%n90fcy"
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
        print("seed is packed:")
        print("--->   " + packSeed(SeedInUse1) + "   <---")
    else:
        print("seed is unpacked:")
        print(SeedInUse1)
      
#transfers your current seed and packerlibrary to the txt file, overwrites previous values
def writeToTXT():
    print("writing packed seed and packerLibrary into packerlibrary.txt ...")
    with open("packerLibrary.txt","w",encoding="utf-8") as file:
        file.write(packSeed(SeedInUse1) + "@" + packerLibrary)
    print("successfully written data to txt")


#this is an example of what a workflow could look like:
resetFile()
makeLibrary()
displaySeed()
print(execute("decipher","5abB{5hbjLmGhb5WW$bh{5BbW b-$xBh"))
