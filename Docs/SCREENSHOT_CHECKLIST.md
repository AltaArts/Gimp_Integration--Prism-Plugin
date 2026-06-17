# Screenshot Checklist

Drop all screenshots into `Docs/DocsImages/` using the exact filenames listed below.
Once placed, they will appear automatically in the docs with no further edits needed.

---

## README.md

| Filename | What to show |
|----------|-------------|
<!-- | `Gimp_Icon.png` | The GIMP 3 application icon (for the title inline image).  Can be any small square icon, e.g. the wilber icon or the GIMP .ico file. | -->



<!-- | `Gimp_Prism_Overview.png` | GIMP 3 open with the Prism menu visible in the menu bar.  A good "hero" overview shot of the full GIMP window with a project image loaded and the Prism menu dropped down. |

---

## Docs/Installation.md

| Filename | What to show |
|----------|-------------|
| `Adding_Plugin.png` | Prism Settings → Plugins tab.  The gear icon is open, showing the search path dialogue with additional paths and the **Add existing plugin** (plus icon) button highlighted. |
| `Plugin_Folder.png` | The file browser after clicking "Add existing plugin", navigated to the `Gimp` plugin folder so the folder is selected/highlighted. |
| `Autoload.png` | Prism Settings → Plugins tab showing the Gimp plugin entry in the plugin list with its **Autoload** checkbox set. |
| `Add_DCC_Apps.png` | Prism Settings → DCC Apps → Gimp tab, showing the executable path field populated with the GIMP 3 executable (e.g. `gimp-3.0.exe`). | -->

---

## Docs/Interface.md

| Filename | What to show |
|----------|-------------|
| `Prism_Menu.png` | The GIMP 3 menu bar with the **Prism** menu dropped open, showing all six items: "1 - Save Version", "2 - Save Comment", "3 - Open Project Browser", "4 - Open State Manager", "5 - Open Prism Settings", "6 - Reset Prism". |
| `Settings_Overview.png` | Prism Settings → DCC Apps → Gimp tab, showing both the **Bridge Port Out (Gimp -> Prism)** and **Bridge Port In (Prism -> Gimp)** spinboxes with their default values (50600 and 50601). |

---

## Docs/Exporting.md

| Filename | What to show |
|----------|-------------|
| `SM_Render_Overview.png` | The Prism State Manager open in GIMP with a Gimp_Render state selected/expanded.  Show the full state panel: image specs (resolution, color mode, bit depth, gamma), format selector, scale dropdown, and format-specific settings visible. |
| `SM_Render_AlphaFill.png` | The Gimp_Render state with a JPEG (or other non-alpha) format selected on an image that has alpha.  Show the **Alpha Background Fill** color picker widget that appears below the format settings. |
| `SM_Render_PSD.png` | The Gimp_Render state with `.psd` selected as the format, showing the **Export as Scenefile** checkbox option that appears for PSD exports. |

---

## Docs/Importing.md

| Filename | What to show |
|----------|-------------|
| `SM_Import_Overview.png` | The Prism State Manager open in GIMP with a Gimp Import state selected/expanded.  Show the full state panel: the imported layer path, current version label, latest version label, the **Layer Name** field, and the **Browse** / **Import Latest Version** buttons. |
| `SM_Import_MediaBrowser.png` | The Prism Media Browser popup that opens when creating a new import state (or clicking Browse), showing the project media tree with identifiers and versions visible. |

---

## Summary (all files in order)

```
Docs/DocsImages/
    Gimp_Icon.png                  ← README title icon
    Gimp_Prism_Overview.png        ← README hero overview
    Adding_Plugin.png              ← Installation
    Plugin_Folder.png              ← Installation
    Autoload.png                   ← Installation
    Add_DCC_Apps.png               ← Installation
    Prism_Menu.png                 ← Interface
    Settings_Overview.png          ← Interface
    SM_Render_Overview.png         ← Exporting
    SM_Render_AlphaFill.png        ← Exporting
    SM_Render_PSD.png              ← Exporting
    SM_Import_Overview.png         ← Importing
    SM_Import_MediaBrowser.png     ← Importing
```

**Total: 13 screenshots.**
