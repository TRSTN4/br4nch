# load.folder

To load an folder, use the **following function:**

> br4nch.**load**.**folder**(*branch*, *directory*, *header=""*, *include=""*, *exclude=""*, *unused=True*, *folder_priority=True*)

**Required arguments:**

- branch - This is the argument where you specify the name of the new branch(es) that will be created.
- directory - This is the argument where you specify the path to the folder that will be displayed.

**Optional arguments:**

- header - This is the argument where you specify the header name for the branch(es).
- include - This is the argument where you specify the file extension(s) that will be displayed.
- exclude - This is the argument where you specify the file extension(s) that won't be displayed.
- unused - If this argument is 'False', all directories with no content will not be displayed.
- folder_priority - If this argument is 'False', the files will be displayed at the top instead of the directories.

Here's an example:

```python
br4nch.load.folder(branch="MyFolder", directory="D:/Vault")

br4nch.display.branch(branch="MyFolder")
D:/Vault
┣━ Documents
┃  ┣━ Important.txt
┃  ┗━ Passwords.txt
┣━ Downloads
┃  ┗━ Game.zip
┣━ Videos
┃  ┣━ Uploaded
┃  ┃  ┗━ First_Upload.mp4
┃  ┣━ CoolGameplay.mp4
┃  ┗━ MyFirstVideo.mp4
┣━ Identity.txt
┗━ VoiceRecording.mp3
```

Using the include argument:

```python
br4nch.load.folder(branch="MyFolder", directory="D:/Vault", include="txt")

br4nch.display.branch(branch="MyFolder")
D:/Vault
┣━ Documents
┃  ┣━ Important.txt
┃  ┗━ Passwords.txt
┣━ Downloads
┣━ Videos
┃  ┗━ Uploaded
┗━ Identity.txt
```

Using the exclude argument:

```python
br4nch.load.folder(branch="MyFolder", directory="D:/Vault", exclude="txt")

br4nch.display.branch(branch="MyFolder")
D:/Vault
┣━ Documents
┣━ Downloads
┃  ┗━ Game.zip
┣━ Videos
┃  ┣━ Uploaded
┃  ┃  ┗━ First_Upload.mp4
┃  ┣━ CoolGameplay.mp4
┃  ┗━ MyFirstVideo.mp4
┗━ VoiceRecording.mp3
```

**Possible errors:**

These are the errors that may pop up when the function is used incorrectly. For more information about errors, head to [errors](../../guides/errors.md).

- InstanceStringError
- InvalidBranchNameError
- NotExistingDirectoryError
- DuplicateBranchError

