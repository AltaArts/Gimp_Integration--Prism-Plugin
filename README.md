# **Gimp Intergration for Prism Pipeline 2**
A Gimp intergration to be used with version 2 of Prism Pipeline 

Prism automates and simplifies the workflow of animation and VFX projects.

You can find more information on the website:

https://prism-pipeline.com/


## **Notes**

- Gimp 2 versions are supported.  Gimp 3 (2.99) support will be added in the future.
- Prism and Gimp communicate through a socket.  The port listed in the Gimp tab in Prism's DCC settings must be available, and any anti-virus must allow the port to be used.





## **Installation**

This plugin is for Windows only, as Prism2 only supports Windows at this time.

You can either download the latest stable release version from: [Latest Release](https://github.com/AltaArts/DeleteFunctions--Prism-Plugin/releases/latest)             TODO

or download the current code zip file from the green "Code" button above or on [Github](https://github.com/JBreckeen/DeleteFunctions--Prism-Plugin/tree/main)                   TODO

Copy the directory named "Gimp" to a directory of your choice, or a Prism2 plugin directory.

Prism's default plugin directories are: *{installation path}\Plugins\Apps* and *{installation Path}\Plugins\Custom*.

It is suggested to have the Gimp plugin with the other DCC plugins in: *{drive}\ProgramData\Prism2\plugins*

You can add the additional plugin search paths in Prism2 settings.  Go to Settings->Plugins and click the gear icon.  This opens a dialogue and you may add additional search paths at the bottom.

Once added, you can either restart Prism2, or select the "Add existing plugin" (plus icon) and navigate to where you saved the Gimp folder.

INSERT

Afterwards, you can select the Plugin autoload as desired:

INSERT

Then to add the intergration, go to the "DCC Apps" -> "Gimp" tab.  Then click the "add" button and navigate to the folder containing the gimp executable



## **Usage**




## **Issues / Suggestions**

For any bug reports or suggestions, please add to the GitHub repo.
