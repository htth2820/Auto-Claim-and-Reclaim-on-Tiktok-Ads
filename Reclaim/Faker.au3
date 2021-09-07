#RequireAdmin
#include <File.au3>


Dim $aCountry[100]
Global $line = _FileCountLines(@ScriptDir&'\aCountry.txt')
For $i = 0 To $line
	$aCountry[$i] = FileReadLine(@ScriptDir&'\aCountry.txt', $i)
Next

WinActivate('Technitium MAC Address Changer v6 - by Shreyas Zare')
ControlClick('Technitium MAC Address Changer v6 - by Shreyas Zare', '', "[CLASS:ThunderRT6CommandButton; INSTANCE:7]", 'left', 1)
ControlClick('Technitium MAC Address Changer v6 - by Shreyas Zare', '', "[CLASS:ThunderRT6CommandButton; INSTANCE:6]", 'left', 1)
WinWaitActive('MAC Address Changed Successfully')
ControlClick('MAC Address Changed Successfully', '', "[CLASS:Button; INSTANCE:1]", 'left', 1)

Sleep(45000)

WinActivate('Hotspot Shield')
MouseClick('left',@DesktopWidth*0.42595, @DesktopHeight*0.43229, 1)
;Sleep(1000)
;MouseClick('left', 545, 577, 1)
Send($aCountry[Random(0, $line, 1)])
Sleep(1000)
Send('{DOWN}')
Sleep(1000)
Send('{ENTER}')



