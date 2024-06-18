# linuAV (Linux Anti-Virus)

# Description
LinuAV is designed for Anyone who values SECURITY above all else.. It is a very powerful Command-line interface tool built for Linux, that finds ALL new malware including: worms, viruses, Trojans, rootkits, spyware, adware, etc. If it is executable linuAV will find it. LinuAV utilizes a "baseline" .txt file that it creates indexing all executable files in "/" dir aka root folder. (You may also input a folder of your choosing. it does not need to be of the whole file system). The baseline file is considered a to be a clean image of a file system. When you think you have been infected use linuAV to scan your file system against the baseline file, if there are any new executable files that were not in your baseline will be output as potential malware with a full path for further investigation.

# Features:
- Make File: Used for the creation of the baseline.txt file and scanfile.txt which are stored in the same directory as the tool.
- scan files: Used to scan linux file systems for new malware.
- help: Useful help message and step by step directions of how to use linuAV.
- "q" for quit: exits the program.

# Requirements:
- Must have Linux. 

# Installation:
Download here: [Releases](https://github.com/jmb-ops/linuAV/releases/tag/v1.0.0).
- navigate to your Downloads folder.
- `move` linuAV to wherever you want to store it.
- `unzip linuAV-1.0.1`
- `python3 linuav` or
- `chmod +x linuav` then
- `./linuav`

# Screenshot:
![Screenshot_2024-06-17_12_48_10](https://github.com/jmb-ops/linuAV/assets/135682697/f5fe2c95-1e6c-4644-822d-f4a9476101fb)

# Compatibility:
This tool has been tested on Kali Linux and Kali Purple.

# Video:
- A link below to a Youtube video demoing the software

click: [LinuAV-watch](https://youtu.be/0ljiuFnMa-4)
