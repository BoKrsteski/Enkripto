# Enkripto
NOTE: this project does work, but currently has no frontend. all params have to be defined by setting the variables.
Also expect bugs, this was made in a day.

it can encode an decode (or encrypt/decipher, call it what you like) any messages using a seed/library-layer system.

library-layers are shuffled versions of the alphabet ; An indefinite amount of them can be created, with each one of them encrypting itself using the previous one's properties. The last created layer is always the library that will be used for the main en-/de-coding.

so that all the layers don't need to be shared and to provide extra safety, a seed is being generated that is able of reproducing the library-layers.

this seed is then packed, meaning it is also encrypted and shuffled.

the packed seed and the library used to pack the seed can then be saved in a txt file. This way you can share the txt with anyone you want to have the same encryption scheme as you.

libraryPacker.txt already contains default values and could thus be used for direct import.
