#NoEnv 
#SingleInstance , Force
; #IfWinActive  Path of Exile

; parameter
; SetMouseDelay 150
; SetWorkingDir %A_ScriptDir% 
; SendMode, Input
ConfigINI := %A_scriptdir%\config.ini
sys_flag := 0

ifnotexist,%ConfigINI%{
	IniWrite, 0	, %ConfigINI%, ConfirmPos, xx
	IniWrite, 0	, %ConfigINI%, ConfirmPos, yy
	IniWrite, 0	, %ConfigINI%, RerollPos, xx
	IniWrite, 0	, %ConfigINI%, RerollPos, yy
}

; F1 => sys ON
$F1::
	sys_flag := 1
	return

; F2 => sys OFF
$F2::
	sys_flag := 0
	return

; CapsLock hold => click
~*$CapsLock::
	if (sys_Flag = 0)
		return
	
	Loop{
	    if !GetKeyState("CapsLock", "P")
	        break
		
	    Sleep 10
	    Click
	}

	return

; shift + 1
$+1::
	if (sys_flag = 0)
		return

	else{
		Click
		Loop, 13{
			Send {WheelDown 1}
		}
		
		MouseGetPos xx, yy
		rCordXX = %xx%
		rCordYY = %yy%
		BlockInput, MouseMove
		IniRead, CordXX, Config.ini, ConfirmPos, xx
		IniRead, CordYY, Config.ini, ConfirmPos, yy
		MouseMove, CordXX , CordYY , 0
		
		Click
		Sleep 200
		Loop, 8{
			Send {WheelDown 1}
		}
		
		Click
		Sleep 200
		Click
		
		MouseMove, rCordXX , rCordYY , 0	
		BlockInput, MouseMoveOff
	}
	
	return

; shift + 2
$+2::
	if (sys_flag = 0)
		return

	else{
		BlockInput, MouseMove
		MouseGetPos xx, yy
		rCordXX = %xx%
		rCordYY = %yy%
		IniRead, CordXX, Config.ini, RerollPos, xx
		IniRead, CordYY, Config.ini, RerollPos, yy
		MouseMove, CordXX , CordYY , 0
		
		Sleep 200
		Click
		Sleep 200
		
		MouseMove, rCordXX , rCordYY , 0
		BlockInput, MouseMoveOff
	}
	
	return

; shift + F9
$+F9::
	MouseGetPos xx, yy
	IniWrite, %xx%, %ConfigINI%, ConfirmPos, xx
	IniWrite, %yy%,	%ConfigINI%, ConfirmPos, yy
	
	return

; shift + F10
$+F10::
	MouseGetPos xx, yy
	IniWrite, %xx%,	%ConfigINI%, RerollPos, xx
	IniWrite, %yy%,	%ConfigINI%, RerollPos, yy

	return
