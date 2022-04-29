# load.Folder

To load a folder, use the **following function:**

> br4nch.**load**.**Folder**(*new_tree*, *folder_path*, *header=""*, *include=""*, *exclude=""*, *unused=True*, *folder_priority=True*)

**Required argument(s):**

- *new_tree* - The name for the new tree(s) that will be created for the imported folder.
- *folder_path* - The path of the folder that will be imported.

**Optional argument(s):**

- *header* - The header name for the tree(s).
- *include* - The file extension(s) that will be displayed.
- *exclude* - The file extension(s) that won't be displayed.
- *unused* - If this argument is 'False', all directories with no content will not be displayed.
- *folder_priority* - If this argument is 'False', the files will be displayed at the top instead of the directories.

**Guide:**

> To import the contents of a folder, specify the new name for the tree in the `new_tree` argument and specify the path of the location of the folder in the `folder_path` argument.
>
> ```python
> >>> br4nch.load.Folder(new_tree="MyFolder", folder_path="D:/Vault")
> 
> >>> br4nch.display.Tree(new_tree="MyFolder")
> D:/Vault
> ┣━ Documents
> ┃ˑˑ┣━ Important.txt
> ┃ˑˑ┗━ Passwords.txt
> ┣━ Downloads
> ┃ˑˑ┗━ Game.zip
> ┣━ Photos
> ┣━ Videos
> ┃ˑˑ┣━ Uploaded
> ┃ˑˑ┃ˑˑ┗━ First_Upload.mp4
> ┃ˑˑ┣━ CoolGameplay.mp4
> ┃ˑˑ┗━ MyFirstVideo.mp4
> ┣━ Identity.txt
> ┗━ VoiceRecording.mp3
> ```
>
> To use a header other than the provided path, specify the name for the header in the `header` argument.
>
> ```python
> >>> br4nch.load.Folder(new_tree="MyFolder", folder_path="D:/Vault", header="My Header!")
> 
> >>> br4nch.display.Tree(new_tree="MyFolder")
> My Header!
> ┣━ Documents
> ┃ˑˑ┣━ Important.txt
> ┃ˑˑ┗━ Passwords.txt
> ┣━ Downloads
> ┃ˑˑ┗━ Game.zip
> ┣━ Photos
> ┣━ Videos
> ┃ˑˑ┣━ Uploaded
> ┃ˑˑ┃ˑˑ┗━ First_Upload.mp4
> ┃ˑˑ┣━ CoolGameplay.mp4
> ┃ˑˑ┗━ MyFirstVideo.mp4
> ┣━ Identity.txt
> ┗━ VoiceRecording.mp3
> ```
>
> To filter only files with a certain extension, put the extension in the `include` argument.
>
> ```python
> >>> br4nch.load.Folder(new_tree="MyFolder", folder_path="D:/Vault", include="txt")
> 
> >>> br4nch.display.Tree(new_tree="MyFolder")
> D:/Vault
> ┣━ Documents
> ┃ˑˑ┣━ Important.txt
> ┃ˑˑ┗━ Passwords.txt
> ┣━ Downloads
> ┣━ Photos
> ┣━ Videos
> ┃ˑˑ┗━ Uploaded
> ┗━ Identity.txt
> ```
>
> To filter out only files with a certain extension, put the extension in the `exclude` argument.
>
> ```python
> >>> br4nch.load.Folder(new_tree="MyFolder", folder_path="D:/Vault", exclude="txt")
> 
> >>> br4nch.display.Tree(new_tree="MyFolder")
> D:/Vault
> ┣━ Documents
> ┣━ Downloads
> ┃ˑˑ┗━ Game.zip
> ┣━ Photos
> ┣━ Videos
> ┃ˑˑ┣━ Uploaded
> ┃ˑˑ┃ˑˑ┗━ First_Upload.mp4
> ┃ˑˑ┣━ CoolGameplay.mp4
> ┃ˑˑ┗━ MyFirstVideo.mp4
> ┗━ VoiceRecording.mp3
> ```
>
> To filter out folders that contain no files, set the `unused` argument to `False`.
>
> ```python
> >>> br4nch.load.Folder(new_tree="MyFolder", folder_path="D:/Vault", unused=False)
> 
> >>> br4nch.display.Tree(new_tree="MyFolder")
> D:/Vault
> ┣━ Documents
> ┃ˑˑ┣━ Important.txt
> ┃ˑˑ┗━ Passwords.txt
> ┣━ Downloads
> ┃ˑˑ┗━ Game.zip
> ┣━ Videos
> ┃ˑˑ┣━ Uploaded
> ┃ˑˑ┃ˑˑ┗━ First_Upload.mp4
> ┃ˑˑ┣━ CoolGameplay.mp4
> ┃ˑˑ┗━ MyFirstVideo.mp4
> ┣━ Identity.txt
> ┗━ VoiceRecording.mp3
> ```
>
> To put the folders under the other files, set the `folder_priority` argument to `False`.
>
> ```python
> >>> br4nch.load.Folder(new_tree="MyFolder", folder_path="D:/Vault", folder_priority=False)
> 
> >>> br4nch.display.Tree(new_tree="MyFolder")
> D:/Vault
> ┣━ Identity.txt
> ┣━ VoiceRecording.mp3
> ┣━ Documents
> ┃ˑˑ┣━ Important.txt
> ┃ˑˑ┗━ Passwords.txt
> ┣━ Downloads
> ┃ˑˑ┗━ Game.zip
> ┣━ Photos
> ┗━ Videos
> ˑˑˑ┣━ CoolGameplay.mp4
> ˑˑˑ┣━ MyFirstVideo.mp4
> ˑˑˑ┗━ Uploaded
> ˑˑˑˑˑˑ┗━ First_Upload.mp4
> ```
>
> To load multiple trees in the same function call, you can use a list for the `new_tree` argument.
>
> ```python
> >>> br4nch.load.Folder(new_tree=["MyFolder", "MyFolderTwo"], folder_path="D:/Vault")
> 
> >>> br4nch.display.Tree(new_tree=["MyFolder", "MyFolderTwo"])
> D:/Vault
> ┣━ Documents
> ┃ˑˑ┣━ Important.txt
> ┃ˑˑ┗━ Passwords.txt
> ┣━ Downloads
> ┃ˑˑ┗━ Game.zip
> ┣━ Photos
> ┣━ Videos
> ┃ˑˑ┣━ Uploaded
> ┃ˑˑ┃ˑˑ┗━ First_Upload.mp4
> ┃ˑˑ┣━ CoolGameplay.mp4
> ┃ˑˑ┗━ MyFirstVideo.mp4
> ┣━ Identity.txt
> ┗━ VoiceRecording.mp3
> D:/Vault
> ┣━ Documents
> ┃ˑˑ┣━ Important.txt
> ┃ˑˑ┗━ Passwords.txt
> ┣━ Downloads
> ┃ˑˑ┗━ Game.zip
> ┣━ Photos
> ┣━ Videos
> ┃ˑˑ┣━ Uploaded
> ┃ˑˑ┃ˑˑ┗━ First_Upload.mp4
> ┃ˑˑ┣━ CoolGameplay.mp4
> ┃ˑˑ┗━ MyFirstVideo.mp4
> ┣━ Identity.txt
> ┗━ VoiceRecording.mp3
> ```
>
> To include multiple extensions in the same function call, you can use a list for the `include` argument.
>
> ```python
> >>> br4nch.load.Folder(new_tree="MyFolder", folder_path="D:/Vault", include=["txt", "mp4"])
> 
> >>> br4nch.display.Tree(new_tree="MyFolder")
> D:/Vault
> ┣━ Documents
> ┃ˑˑ┣━ Important.txt
> ┃ˑˑ┗━ Passwords.txt
> ┣━ Downloads
> ┣━ Photos
> ┣━ Videos
> ┃ˑˑ┣━ Uploaded
> ┃ˑˑ┃ˑˑ┗━ First_Upload.mp4
> ┃ˑˑ┣━ CoolGameplay.mp4
> ┃ˑˑ┗━ MyFirstVideo.mp4
> ┗━ Identity.txt
> ```
>
> To exclude multiple extensions in the same function call, you can use a list for the `exclude` argument.
>
> ```python
> >>> br4nch.load.Folder(new_tree="MyFolder", folder_path="D:/Vault", exclude=["txt", "mp4"])
> 
> >>> br4nch.display.Tree(new_tree="MyFolder")
> D:/Vault
> ┣━ Documents
> ┣━ Downloads
> ┃ˑˑ┗━ Game.zip
> ┣━ Photos
> ┣━ Videos
> ┃ˑˑ┗━ Uploaded
> ┗━ VoiceRecording.mp3
> ```

**Possible error(s):**
These are the errors that may pop up when the function is used incorrectly.
*For more information about errors, head to [errors](../../guides/errors.md).*

- *InstanceStringError*
- *InvalidBranchNameError*
- *NotExistingDirectoryError*
- *DuplicateBranchError*

