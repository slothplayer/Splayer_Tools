; ifnotexist,%ConfigINI%{
; 	IniWrite, 0, %configini%, ConfirmPos, mouse_x
; 	IniWrite, 0, %configini%, ConfirmPos, mouse_y
; 	IniWrite, 0, %configini%, RerollPos, mouse_x
; 	IniWrite, 0, %configini%, RerollPos, mouse_y
; }

; shift + R => scouring position
$+R::
	MouseGetPos mouse_x, mouse_y
	IniWrite, %mouse_x%, %configini%, currency_scouring, scouring_x
	IniWrite, %mouse_y%, %configini%, currency_scouring, scouring_y
	
	return

; ctrl + R => alc position
$^R::
	MouseGetPos mouse_x, mouse_y
	IniWrite, %mouse_x%, %configini%, currency_alc, alc_x
	IniWrite, %mouse_y%, %configini%, currency_alc, alc_y
	
	return

; shift + F9
$+F9::
	MouseGetPos mouse_x, mouse_y
	IniWrite, %mouse_x%, %configini%, ConfirmPos, mouse_x
	IniWrite, %mouse_y%, %configini%, ConfirmPos, mouse_y
	
	return

; shift + F10
$+F10::
	MouseGetPos mouse_x, mouse_y
	IniWrite, %mouse_x%, %configini%, RerollPos, mouse_x
	IniWrite, %mouse_y%, %configini%, RerollPos, mouse_y

	return
