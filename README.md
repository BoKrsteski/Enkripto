# Enkripto

Enkripto is an encryption project based around one main idea: randomness.

Instead of using one fixed encryption scheme for everyone, Enkripto uses randomly generated data to create an individual scheme for each setup. The main idea behind the project is to explore what happens when randomness becomes a much bigger part of the encryption process.

Enkripto is also designed to work completely locally. No internet connection is required for the actual encryption or decryption process.

## How Enkripto Works

Enkripto uses a Seed as the input for generating and reconstructing its encryption scheme.

The Seed itself is not the encryption scheme. It contains the information Enkripto needs to recreate the corresponding scheme when it is needed.

There are around **10¹⁵⁰ possible schemes**, which makes the possible combinations extremely large.

I am intentionally not explaining every part of how the system works here. Some parts of Enkripto are better left inside the project rather than being completely explained in the README.

## Native Handling Hub

The **Native Handling Hub (NHH)** is a part of Enkripto's internal system.

It is used for handling different parameters and operations inside Enkripto. This includes things such as parameters, aliases and capitalization rules.

NHH is also part of the internal language and structure of Enkripto. More details may be documented later as the project continues to grow.

## Preferences

Enkripto uses a `Preferences.json` file to store local preferences.

This includes things like the location of the Seed file and other settings that are needed when Enkripto starts.

The Seed itself is not stored inside the preferences file. Instead, the file contains the information Enkripto needs to find the Seed.

## Offline

One thing I wanted to keep important with Enkripto is that it does not need an internet connection.

Encryption and decryption can happen completely locally. The data does not need to be uploaded to a server or sent to some external service just to be processed.

This also makes Enkripto usable in situations where there is no internet connection available.

## Possible Use Cases

Enkripto can be used to communicate safely per file or text transfer. there's many way so transfer encrypted data. you could send the encrypted text or file via a messenger of your liking, transfer the file via USB and more.

It can also be interesting for people who want to experiment with different ideas around randomness and encryption.

Another possible use case is working in an offline environment where an internet connection is unavailable or intentionally avoided.

## Why Enkripto?

There are already a lot of very good encryption systems out there, so I did not want Enkripto to just be another implementation of something that already exists.

The project started with a different question:

**What if the encryption scheme itself was generated using randomness?**

That is basically the idea I wanted to explore with Enkripto.

This does not mean that established encryption systems are bad or insecure. Algorithms such as AES and ChaCha20 have been researched and reviewed for years. Enkripto is still an independent and experimental project, so it should be viewed in that context.

## TXT File Encryption

Direct TXT file encryption and decryption is planned for an upcoming version.

Currently, text has to be provided directly to Enkripto. In the future, the goal is to simply select a TXT file and let Enkripto handle the encryption or decryption directly.

For example, instead of copying the contents of a file into Enkripto, you will be able to give Enkripto the file itself.

This is one of the next things I want to work on.

## Releases

Enkripto currently provides builds for **Windows x64** and **Linux x64**.

The releases are built automatically using GitHub Actions. Creating a version tag such as `v1.1.0` starts the build process and creates the corresponding release.

The releases contain the platform specific builds as well as SHA 256 checksums.

The Linux version is provided as a `.tar.gz` archive containing the Enkripto executable.

## Contributors

Just me, Bo Krsteski. A 16 year old student who loves to make little programs in his freetime.
## Project Status

**Current version: `v1.1.0`**

Enkripto is still actively being developed.

The current version includes the core encryption system, Seed based scheme reconstruction, the Native Handling Hub and local preferences.

Direct TXT file encryption and decryption is planned for a future release.

## License

I don't mind if you share it or anything. Just give credit and don't act like it's yours.
