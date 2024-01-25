# DeSmuME-Video-BRS
Auto-setup record and SRAM for RNG manipulation aka shiny hunting / VGC hunting in DeSmuME emulator.

## Instructions
Launch the script with Python:
- py "./start bsr.py"
The script will prompt you to select the DeSmuME executable, ROM, and save file. Once all three are set, it will automatically launch the emulator. Use the following hotkey commands:
- `Ctrl+Alt+Shift+S`: Select the emulator window.
- `Ctrl+Alt+Shift+R`: Restart RNG (has first-time setup).
- `Ctrl+Alt+Shift+E`: Launch a new emulator instance but keep the script running.

Ensure the emulator is the active window before using hotkeys to avoid unintended input in other windows.

## Current Compatibility
- Python 3.12.1

## Intended Versions
- [Good Enough] DeSmuME-VS2019-x64-Release
- [Good Enough] DeSmuME_0.9.11_x64.exe

## To-Do
- [Active] Detect if SRAM is already set up.
- [not_important] Video save location query.
## Planned Features (in no particular order)
- [ ] Compilation into an executable for easier distribution and usage on Windows, possibly MacOS and Linux. (bash would be nice for linux but v hard :/)
- [ ] auto window detection for smoother operation across different system configurations.
- [ ] Automated checks for SRAM setup to reduce manual steps.
- [ ] Gui for easier setup and usage.
- [ ] Ai gui detection
- [ ] rng reporter and pokefinder gui
- [ ] Expanded compatibility with different versions of DeSmuME.
- [ ] Additional hotkeys for extended control and functionality.
- [ ] Optimization for speed and resource usage.
- [ ] Error handling improvements to cover edge cases and unusual scenarios.
- [ ] Detailed logging for troubleshooting and user support.


## Completed
- [Complete] Make README.
- [Complete] Make GitHub repo.
- [Good enough] Window detection.
Feel free to read the code. Suggestions for improvements or contributions are welcome. Contact me if you have ideas or want to help.
