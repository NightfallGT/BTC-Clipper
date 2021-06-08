# BTC-Clipper 

## About
a BTC Clipper or a "Bitcoin Clipper" is a type of malware designed to target cryptocurrency transactions. 

It operates by replacing the recipient cryptocurrency wallet addresses with ones owned by the cyber criminals. This tool demonstrates how certain 
cyber criminals redirect cryptocurrency transactions by replacing clipboard data. When users copy the addresses of cryptowallets that they wish 
to use to transfer bitcoin to, the copied information is stealthily replaced by the attacker's. 

When the clipboard data is pasted, the addresses belong to the criminals' cryptocurrency wallets instead of being the  cryptocurrency wallet for
the intended recipient.

This is a project created to make it easier for malware analysts or ordinary users to understand how Bitcoin clippers work and can be used for 
analysis, research, reverse engineering, or review.

Please be sure to know what you're doing (such as knowing how to remove it) because when the .py file is run because it does modify some stuff in your system such as your
Startup registry.

## Demonstration 

![gif video (1)](https://user-images.githubusercontent.com/75003671/107109844-67b4c400-687e-11eb-8c48-823db42d1808.gif)

## Features
- AUTO STARTUP (PATH FOR .py  + REGISTRY ENTRY)
- SELF DESTRUCT
- REPLICATE AND HIDE
- No external Python modules required
- Add self destruct message

## How to use
1. Change BTC_ADDRESS to wallet address. 
2. Change self destruct message
3. Run -> ```python btcClip.py```

## How it works

When the .py file is run it automatically self destructs and replicates itself to the user's %APPDATA% folder (C:\Users\username\AppData\Roaming). 

1. Replicates the .py file

![Picture 1 ](https://i.ibb.co/6P1WGDM/Screenshot-80.png)

It then adds itself
to the user's Startup registry (HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run) so that it can run again when the PC is turned on. 

2. Adds to the startup registry

![Picture 2 ](https://i.ibb.co/Pzxrf9X/Screenshot-81.png)


### How to delete

1. Navigate to C:\Users\user\AppData\Roaming or you can type %appdata% on the top of the folder.

![Picture 3 ](https://i.ibb.co/3F4YMzP/Screenshot-82.png)

2. then delete btcClip.py

3. To delete from the registry, open up the Registry Editor for Windows and navigate to > HKEY_LOCAL_MACHINE > SOFTWARE > Microsoft > Windows > CurrentVersion > Run
4. Then right click it and delete


## Contact
Dm me on telegram @nightfallx for coding services (btc only)
