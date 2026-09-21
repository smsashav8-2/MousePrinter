Esc::ExitApp

CoordMode Mouse, Screen

global x1 := 0
global y1 := 0
global x2 := 0
global y2 := 0

1::
MouseGetPos x1, y1
ToolTip Top Left Saved
return

2::
MouseGetPos x2, y2
ToolTip Bottom Right Saved
return

F8::

width := x2 - x1
height := y2 - y1

RunWait python convert.py image.png %width% %height%

Loop Read, coords.txt
{
    parts := StrSplit(A_LoopReadLine, ",")

    action := parts[1]
    x := x1 + parts[2]
    y := y1 + parts[3]

    if (action = "DOWN")
    {
        MouseMove x,y,0
        Click Down
    }

    if (action = "MOVE")
    {
        MouseMove x,y,0
    }

    if (action = "UP")
    {
        Click Up
    }
}

Click Up
return