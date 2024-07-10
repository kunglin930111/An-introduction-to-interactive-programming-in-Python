import simplegui

intervals = 100
cnt = 0
total_stops = 0
correct_stops = 0
stop = True

def format(t):
    tenth_of_a_sec = (t) % 10
    sec = int(t / 10) % 10
    mins = int(t / 600) % 600
    ten_of_a_min = int(t / 100) % 6
    display_number = str(mins) + ":" + str(ten_of_a_min) + str(sec) + "." + str(tenth_of_a_sec)
    return display_number
pass
    
def Start():
    global cnt, stop
    stop = False
    timer.start()
    
def Stop():
    global total_stops, correct_stops, stop
    if stop == False :
        if cnt % 10 == 0 and cnt != 0 :
            correct_stops += 1
            total_stops += 1
        elif cnt != 0 :
            total_stops += 1
    stop = True
    timer.stop()
    
def Reset():
    global cnt, correct_stops, total_stops
    cnt = 0
    stop = True
    total_stops = 0
    correct_stops = 0
    timer.stop()

def tick():
    global cnt
    cnt += 1

def draw(canvas):
    text = format(cnt)
    canvas.draw_text( text, (80, 125), 42, "white")
    canvas.draw_text(str(correct_stops) + '/' + str(total_stops), (190,30), 24, "pink")
    
frame = simplegui.create_frame("Stopwatch game", 250, 250)
frame.set_canvas_background('green')

frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(intervals, tick)

frame.start()
Reset()
