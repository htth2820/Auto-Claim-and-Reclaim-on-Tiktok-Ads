
$file = FileOpen(@ScriptDir & '\id.txt')
$id = FileReadLine($file,1)
WinWaitActive("Open")
WinActivate("Open")
Send("C:\Tiktok\")
Send("{ENTER}")
Sleep(200)
Send("{TAB}")
Send("{TAB}")
Send("{TAB}")
Sleep(200)
Send("{TAB}")
Send("{TAB}")
Send("{TAB}")
Sleep(200)
Send("{TAB}")
Send("{TAB}")
Send($id)
Sleep(3000)
Send("{TAB}")
Send("{TAB}")
Send("{TAB}")
Sleep(200)
Send("{Space}")
Sleep(200)
Send("{ENTER}")
