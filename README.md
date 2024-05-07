# **Gimp Integration for Prism Pipeline 2**
A Gimp integration to be used with version 2 of Prism Pipeline 

Prism automates and simplifies the workflow of animation and VFX projects.

You can find more information on the website:

https://prism-pipeline.com/


## **Notes**

- Gimp2 versions are supported.  Gimp3 (2.99) support will be added in the future.
- Prism and Gimp communicate through a socket.  The port listed in the Gimp tab in Prism's DCC settings must be available, and any anti-virus must allow the port to be used.
- Hint: if you click an Prism Menu item such as "State Manager" and nothing happens, you probaly need to start the server. If message display is active, there will be a reminder shown.
- Hint: clicking a Prism action from the menu loads an instance of Prism, and thus there is a slight delay for the actions such as requesting the Project Browser or State Manager.
- As of now, .png, .exr, .jpg, and .psd exports are supported.  More formats will be added.

- Gimp saves .exr's in full-float 32bit zip compression only.  

- To aid is use, tooltips are provided throughout.




## **Installation**

This plugin is for Windows only, as Prism2 only supports Windows at this time.

You can either download the latest stable release version from: [Latest Release](https://github.com/AltaArts/Gimp_Integration--Prism-Plugin/releases/latest)

or download the current code zip file from the green "Code" button above or on [Github](https://github.com/AltaArts/Gimp_Integration--Prism-Plugin)

Copy the directory named "Gimp" to a directory of your choice, or a Prism2 plugin directory.

It is suggested to have the Gimp plugin with the other DCC plugins in: *{drive}\ProgramData\Prism2\plugins*

Prism's default plugin directories are: *{installation path}\Plugins\Apps* and *{installation Path}\Plugins\Custom*.

You can add the additional plugin search paths in Prism2 settings.  Go to Settings->Plugins and click the gear icon.  This opens a dialogue and you may add additional search paths at the bottom.

Once added, select the "Add existing plugin" (plus icon) and navigate to where you saved the Gimp folder.

![Add Existing Plugin](https://github.com/AltaArts/Gimp_Integration--Prism-Plugin/assets/86539171/d86e3b34-d172-4cd8-b238-147ff6a25106)<br/><br/>
![Select Plugin Folder](https://github.com/AltaArts/Gimp_Integration--Prism-Plugin/assets/86539171/8a434886-9520-4048-83d1-e9d7a19e427c)


Afterwards, you can select the Plugin autoload as desired:

![AutoLoad](https://github.com/AltaArts/Gimp_Integration--Prism-Plugin/assets/86539171/1f0295c3-709d-4937-88fb-3d63d43d779c)

To add the integration, go to the "DCC Apps" -> "Gimp" tab.  Then click the "add" button and navigate to the folder containing the Gimp executable - ie "Gimp-2.10.exe".  If there is more than one version of Gimp installed, it is advisable to set the executable in the "Override" box in the DCC settings.


![Intergration](https://github.com/AltaArts/Gimp_Integration--Prism-Plugin/assets/86539171/8c0b64d6-b0c2-44fa-a159-fe7512d9b0c2)


## **Usage**

### **Menu**
Prism functions are accessed through the Prism menu in the top bar of Gimp's UI.  The communication server must be started before Prism functions may be executed.  This opens a socket port between Prism and the Gimp integration only, and there is no data communicated outside the local computer.  You can change the socket number in Settings->DCCs->Gimp if needed.

![Prism Menu](https://github.com/AltaArts/Gimp_Integration--Prism-Plugin/assets/86539171/46afa882-72d0-4153-b7bf-ae9cac63ebfc)


### **Messages / Logging**

Messages can be displayed several ways, with several levels of detail.  Gimp displays messages through the status bar at the bottom, and the "Error Console".

![Gimp Error Console](https://github.com/AltaArts/Gimp_Integration--Prism-Plugin/assets/86539171/67df98e5-ae36-4a11-a60d-dbd3bbfdb3c5)

There are three level of message display, but all messages will always be saved in the log.  With "Log Only", no messages will be displayed in the Gimp UI.  "Minimal" will display some messages that may be useful to the user such as "Starting Server".  "All" will display all messages in the UI. 

![Log Menu](https://github.com/AltaArts/Gimp_Integration--Prism-Plugin/assets/86539171/f0de1aef-72b2-4b4c-bc5f-495414f321a6)

Keep in mind that having "All" messages displayed will show many messages and slightly slow the interface, thus it is suggested to have the message level at "Minimal".  If the Error Console is docked in a widow with other tabs, new messages will move the focus to the Error Console so it is suggested to have the Error Console docked into its own window.

![Suggested UI](https://github.com/AltaArts/Gimp_Integration--Prism-Plugin/assets/86539171/931249ca-6a58-4680-b871-b2e5dbc97b56)


The Gimp log may be viewed by opening the directory with the "open Log" button in Settings->DCCs->Gimp.  The log will update until it reaches the max size limit set in settings, and then will be renamed to "_OLD" with a maximum of those two files.  By default, the logs are saved in the root directory of the Gimp plugin and you can change the save location in the settings.

### **Exporting**

To export (save) images we use the StateManager via a custom Gimp_Render state.  Various output image formats are supported, with more being added.  The current image's details will be displayed along with format-specific settings for each state.  A user has the option to scale the resulting image, or change the color mode and bit depth of the resulting export.  These changes will not alter the scenefile.

![Gimp Render](https://github.com/AltaArts/Gimp_Integration--Prism-Plugin/assets/86539171/25c55eb1-a483-4b23-8739-73e879cd1c1d)



## **Issues / Suggestions**

For any bug reports or suggestions, please add to the GitHub repo.
