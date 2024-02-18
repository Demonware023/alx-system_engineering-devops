TASK: Command line for the win
======================================================

DESCRIPTION -

CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!
============================================================================

TASK REQUIREMENTS
======================================================

Create a screenshot, showing that you completed the required levels
Push this screenshot with the right name to GitHub, in either the PNG or JPEG format

In addition to completing the project tasks and submitting the required screenshots to GitHub, you are also required to demonstrate the use of the SFTP (Secure File Transfer Protocol) command-line tool to move your local screenshots to the sandbox environment.

The screenshoots of completed level should be inside the dir /root/alx-system_engineering-devops/command_line_for_the_win/
============================================================================

TASK SOLUTION - HOW TO UPLOAD FILES USING SFTP
=======================================================

1. Open a terminal or command prompt on your local machine.

2. I used the SFTP command-line tool(This can be found on the sandbox in your intranet) to establish a connection to the sandbox environment. You will need the password provided to you for the sandbox environment.

3. Once connected to the SFTP server, i navigated to the directory command_line_for_the_win(/root/alx-system_engineering-devops/command_line_for_the_win/) to upload the screenshots.

4. Using the SFTP 'put' command to upload the screenshots from my local machine to the sandbox environment. I was able to navigate to my local file system from the remote system using the following commands 'lls, lcd' and more to get to the directory the screenshots to upload were located. These commands are the normal unix commands but the 'l' before it will indicate you want to access information from your local file system.

5. After uploading the necessary files/screenshots, i used the SFTP command 'bye' to exit the SFTP remote server/shell.
