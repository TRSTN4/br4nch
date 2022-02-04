# load.folder

To load an folder, use the **following function:**

> br4nch.**load**.**folder**(*branch*, *directory*, *header=""*, *include=""*, *exclude=""*, *unused=True*, *folder_priority=True*)

**Required argument(s):**

- branch - The name for the new branch(es) that will be created for the imported folder.
- directory - The path of the folder that will be imported.

**Optional argument(s):**

- header - The header name for the branch(es).
- include - The file extension(s) that will be displayed.
- exclude - The file extension(s) that won't be displayed.
- unused - If this argument is 'False', all directories with no content will not be displayed.
- folder_priority - If this argument is 'False', the files will be displayed at the top instead of the directories.

**Guide:**

> To import the contents of a folder, specify the name for the branch in the `branch` argument and specify the path of the location of the folder in the `directory` argument.
>
> ```python
> >>> br4nch.load.folder(branch="MyFolder", directory="D:/Vault")
> 
> >>> br4nch.display.branch(branch="MyFolder")
> D:/Vault
> ┣━ Documents
> ┃‎‎┣━ Important.txt
> ┃‎‎┗━ Passwords.txt
> ┣━ Downloads
> ┃‎‎┗━ Game.zip
> ┣━ Photos
> ┣━ Videos
> ┃‎‎┣━ Uploaded
> ┃‎‎┃‎‎┗━ First_Upload.mp4
> ┃‎‎┣━ CoolGameplay.mp4
> ┃‎‎┗━ MyFirstVideo.mp4
> ┣━ Identity.txt
> ┗━ VoiceRecording.mp3
> ```
>
> To use a header other than the provided path, specify the name for the header in the `header` argument.
>
> ```python
> >>> br4nch.load.folder(branch="MyFolder", directory="D:/Vault", header="My Header!")
> 
> >>> br4nch.display.branch(branch="MyFolder")
> My Header!
> ┣━ Documents
> ┃‎‎┣━ Important.txt
> ┃‎‎┗━ Passwords.txt
> ┣━ Downloads
> ┃‎‎┗━ Game.zip
> ┣━ Photos
> ┣━ Videos
> ┃‎‎┣━ Uploaded
> ┃‎‎┃‎‎┗━ First_Upload.mp4
> ┃‎‎┣━ CoolGameplay.mp4
> ┃‎‎┗━ MyFirstVideo.mp4
> ┣━ Identity.txt
> ┗━ VoiceRecording.mp3
> ```
>
> To filter only files with a certain extension, put the extension in the `include` argument.
>
> ```python
> >>> br4nch.load.folder(branch="MyFolder", directory="D:/Vault", include="txt")
> 
> >>> br4nch.display.branch(branch="MyFolder")
> D:/Vault
> ┣━ Documents
> ┃‎‎┣━ Important.txt
> ┃‎‎┗━ Passwords.txt
> ┣━ Downloads
> ┣━ Photos
> ┣━ Videos
> ┃‎‎┗━ Uploaded
> ┗━ Identity.txt
> ```
>
> To filter out only files with a certain extension, put the extension in the `exclude` argument.
>
> ```python
> >>> br4nch.load.folder(branch="MyFolder", directory="D:/Vault", exclude="txt")
> 
> >>> br4nch.display.branch(branch="MyFolder")
> D:/Vault
> ┣━ Documents
> ┣━ Downloads
> ┃‎‎┗━ Game.zip
> ┣━ Photos
> ┣━ Videos
> ┃‎‎┣━ Uploaded
> ┃‎‎┃‎‎┗━ First_Upload.mp4
> ┃‎‎┣━ CoolGameplay.mp4
> ┃‎‎┗━ MyFirstVideo.mp4
> ┗━ VoiceRecording.mp3
> ```
>
> To filter out folders that contain no files, set the `unused` argument to `False`.
>
> ```python
> >>> br4nch.load.folder(branch="MyFolder", directory="D:/Vault", unused=False)
> 
> >>> br4nch.display.branch(branch="MyFolder")
> D:/Vault
> ┣━ Documents
> ┃‎‎┣━ Important.txt
> ┃‎‎┗━ Passwords.txt
> ┣━ Downloads
> ┃‎‎┗━ Game.zip
> ┣━ Videos
> ┃‎‎┣━ Uploaded
> ┃‎‎┃‎‎┗━ First_Upload.mp4
> ┃‎‎┣━ CoolGameplay.mp4
> ┃‎‎┗━ MyFirstVideo.mp4
> ┣━ Identity.txt
> ┗━ VoiceRecording.mp3
> ```
>
> To put the folders under the other files, set the `folder_priority` argument to `False`.
>
> ```python
> >>> br4nch.load.folder(branch="MyFolder", directory="D:/Vault", folder_priority=False)
> 
> >>> br4nch.display.branch(branch="MyFolder")
> D:/Vault
> ┣━ Identity.txt
> ┣━ VoiceRecording.mp3
> ┣━ Documents
> ┃‎‎┣━ Important.txt
> ┃‎‎┗━ Passwords.txt
> ┣━ Downloads
> ┃‎‎┗━ Game.zip
> ┣━ Photos
> ┗━ Videos
> ‎‎‎┣━ CoolGameplay.mp4
> ‎‎‎┣━ MyFirstVideo.mp4
> ‎‎‎┗━ Uploaded
>    ‎‎‎‎‎‎┗━ First_Upload.mp4
> ```
>
> To load multiple branches in the same function call, you can use a list for the `branch` argument.
>
> ```python
> >>> br4nch.load.folder(branch=["MyFolder", "MyFolderTwo"], directory="D:/Vault")
> 
> >>> br4nch.display.branch(branch=["MyFolder", "MyFolderTwo"])
> D:/Vault
> ┣━ Documents
> ┃‎‎┣━ Important.txt
> ┃‎‎┗━ Passwords.txt
> ┣━ Downloads
> ┃‎‎┗━ Game.zip
> ┣━ Photos
> ┣━ Videos
> ┃‎‎┣━ Uploaded
> ┃‎‎┃‎‎┗━ First_Upload.mp4
> ┃‎‎┣━ CoolGameplay.mp4
> ┃‎‎┗━ MyFirstVideo.mp4
> ┣━ Identity.txt
> ┗━ VoiceRecording.mp3
> D:/Vault
> ┣━ Documents
> ┃‎‎┣━ Important.txt
> ┃‎‎┗━ Passwords.txt
> ┣━ Downloads
> ┃‎‎┗━ Game.zip
> ┣━ Photos
> ┣━ Videos
> ┃‎‎┣━ Uploaded
> ┃‎‎┃‎‎┗━ First_Upload.mp4
> ┃‎‎┣━ CoolGameplay.mp4
> ┃‎‎┗━ MyFirstVideo.mp4
> ┣━ Identity.txt
> ┗━ VoiceRecording.mp3
> ```
>
> To include multiple extensions in the same function call, you can use a list for the `include` argument.
>
> ```python
> >>> br4nch.load.folder(branch="MyFolder", directory="D:/Vault", include=["txt", "mp4"])
> 
> >>> br4nch.display.branch(branch="MyFolder")
> D:/Vault
> ┣━ Documents
> ┃‎‎┣━ Important.txt
> ┃‎‎┗━ Passwords.txt
> ┣━ Downloads
> ┣━ Photos
> ┣━ Videos
> ┃‎‎┣━ Uploaded
> ┃‎‎┃‎‎┗━ First_Upload.mp4
> ┃‎‎┣━ CoolGameplay.mp4
> ┃‎‎┗━ MyFirstVideo.mp4
> ┗━ Identity.txt
> ```
>
> To exclude multiple extensions in the same function call, you can use a list for the `exclude` argument.
>
> ```python
> >>> br4nch.load.folder(branch="MyFolder", directory="D:/Vault", exclude=["txt", "mp4"])
> 
> >>> br4nch.display.branch(branch="MyFolder")
> D:/Vault
> ┣━ Documents
> ┣━ Downloads
> ┃‎‎┗━ Game.zip
> ┣━ Photos
> ┣━ Videos
> ┃‎‎┗━ Uploaded
> ┗━ VoiceRecording.mp3
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
For more information about errors, head to [errors](../../guides/errors.md).

- *InstanceStringError*
- *InvalidBranchNameError*
- *NotExistingDirectoryError*
- *DuplicateBranchError*

