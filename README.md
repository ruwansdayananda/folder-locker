---
title: "folder-locker"
tags: ""
---

# 1. Introduction

This program can protect users' data by locking directories with a strong password that the user can define. 

:::note
This is only tested with Windows 10
:::

# 2. Steps to setup

1. First, find the **'bin'** directory in this repository and navigate it inside.
2. Find the executable file of **'locker.exe'**.(Navigate to the folder of latest version)
3. Download it to your personal computer.
4. Place it in a directory anywhere you want.
5. Run the application.
6. First, it will ask for a master password from you. Would you please give it a strong password?


:::important
The **master password** is the password used to authenticate the user when the folder is locked.
:::

7. After you set the master password, the program will create a new directory called **'Private'**, consisting of **'config.json'**.

:::danger
Don't delete or modify the file 'config.json'.
:::

8. Put all your private files inside the **'Private'** directory.
9. Then, run the **'locker.exe'** again and give it the confirmation to lock the folder.

:::note
'Private' directory, which includes your private files will disappear after this is done. 
:::

10. When you want to unlock the 'Private' folder, run the **'locker.exe'** again and give the **master password**.

:::important
Repeat steps 9 and 10 when you want to lock and unlock your private files, respectively.
:::
