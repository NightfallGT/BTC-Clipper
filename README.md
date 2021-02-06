# BTC-Clipper | PROOF OF CONCEPT
## THIS TOOL SHOULD ONLY BE USED FOR EDUCATIONAL PURPOSES ONLY

## About
a BTC Clipper or a "Bitcoin Clipper" is a type of malware designed to target cryptocurrency transactions. 

It operates by replacing the recipient cryptocurrency wallet addresses with ones owned by the cyber criminals. This tool demonstrates how certain 
cyber criminals redirect cryptocurrency transactions by replacing clipboard data. When users copy the addresses of cryptowallets that they wish 
to use to transfer bitcoin to, the copied information is stealthily replaced by the attacker's. 

When the clipboard data is pasted, the addresses belong to the criminals' cryptocurrency wallets instead of being the  cryptocurrency wallet for
the intended recipient.

This is a project created to make it easier for malware analysts or ordinary users to understand how Bitcoin clippers work and can be used for 
analysis, research, reverse engineering, or review.

Please be sure to know what you're doing because when the .py file is run (such as knowing how to remove it) because it does modify some stuff in your system such as your
Startup registry.

## Demonstration 
![GIF Demo](https://s2.gifyu.com/images/gif-video.gif)

## How it works

When the .py file is run it automatically self destructs and replicates itself to the user's %APPDATA% folder (C:\Users\username\AppData\Roaming). 

- Replicated the .py file

![Picture 1 ](https://i.ibb.co/6P1WGDM/Screenshot-80.png)

It then adds itself
to the user's Startup registry (HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run) so that it can run again when the PC is turned on. 

- In the startup registry

![Picture 2 ](https://i.ibb.co/Pzxrf9X/Screenshot-81.png)


### How to delete

- Navigate to C:\Users\user\AppData\Roaming or you can type %appdata% on the top of the folder.

![Picture 3 ](https://i.ibb.co/3F4YMzP/Screenshot-82.png)

- then delete btcClip.py

- To delete from the registry, open up the Registry Editor for Windows and navigate to > HKEY_LOCAL_MACHINE > SOFTWARE > Microsoft > Windows > CurrentVersion > Run
- Then right click it and delete


