; initial undone
; 

#NoEnv 
#SingleInstance , Force
SetWorkingDir %A_ScriptDir% 

configini = %A_scriptdir%\src\config.ini
sys_flag := 0

; F1 => sys ON
$F1::
	sys_flag := 1
	return

; F2 => sys OFF
$F2::
	sys_flag := 0
	return

; CapsLock hold => click
*$CapsLock::
	if (sys_Flag = 0)
		return
	
	local_sleep := 20
	Loop{
	    if !GetKeyState("CapsLock", "P")
	        break
		
	    Click
		Sleep local_sleep
	}

	return

; ! => alt
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
		IniRead, CordXX, %configini%, ConfirmPos, xx
		IniRead, CordYY, %configini%, ConfirmPos, yy
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
		IniRead, CordXX, %configini%, RerollPos, xx
		IniRead, CordYY, %configini%, RerollPos, yy
		MouseMove, CordXX , CordYY , 0
		
		Sleep 200
		Click
		Sleep 200
		
		MouseMove, rCordXX , rCordYY , 0
		BlockInput, MouseMoveOff
	}
	
	return

; shift + r => scouring + alc
$+R::
	if (sys_flag = 0)
		return

	local_sleep := 20
	IniRead, scouring_x, %configini%, currency_scouring, scouring_x
	IniRead, scouring_y, %configini%, currency_scouring, scouring_y
	IniRead, alc_x, %configini%, currency_alc, alc_x
	IniRead, alc_y, %configini%, currency_alc, alc_y
	MouseGetPos, mouse_x, mouse_y
	
	BlockInput, MouseMove
	
	MouseMove, scouring_x , scouring_y , 0
	Send {Click Right}
	Sleep local_sleep

	MouseMove, mouse_x , mouse_y , 0	
	Send  {Click}
	Sleep local_sleep
	
	MouseMove, alc_x , alc_y , 0	
	Send {Click Right}
	Sleep local_sleep

	MouseMove, mouse_x , mouse_y , 0	
	Send {Click}
	Sleep local_sleep
	
	BlockInput, MouseMoveOff

	return

