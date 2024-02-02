'''
    Project     : AutoTask-VMKC
    File        : main.py
    Description : Record the operation by mouse and keyborad, then generate the script to auto work. 
    Author      : lysheng (@TJ-CVRSG)
    Date        : 2024-02-02
    Version     : 1.1
'''


import argparse
import ctypes
import os
import vmkc


OPERATION_MENU = [  "Option C | Mouse Click",
                    "Option D | Mouse Double Click",
                    "Option M | Mouse Move (On Mouse Left Key)",
                    "Option B | Press Key BACKSPACE",
                    "Option E | Press Key ENTER",
                    "Option N | Press Key DOWN",
                    "Option L | Press Key UP",
                    "Option S | Press Key SPACE",
                    "Option J | Window Image Judge",
                    "Option Q | QUIT",                 ]


def record_generate(auto_task_name, repeat_times):
    file = open(auto_task_name + ".py", "w")
    file.write("import time\n")
    file.write("import vmkc\n")
    file.write("\n")
    file.write("WORK_TIMES = %s\n" % repeat_times)
    file.write("\n")
    
    file.write("auto_work_time = WORK_TIMES\n")
    file.write("count = 0\n")
    file.write("while (auto_work_time != 0):\n")
    file.write("\tcount += 1\n")
    file.write("\tauto_work_time -= 1\n")
    while True:
        order = input("* Please select the operation : ")
        
        if order.upper() == 'C':
            point = vmkc.CTypePoint()
            ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
            vmkc.mouse.click(int(point.x), int(point.y), vmkc.MOUSEKEY_LEFT)
            file.write("\tprint(\"\\r[%%d] Click at (%s, %s) !  \\t\\t\\t\\t\" %% count, end = '')\n" % (int(point.x), int(point.y)))
            file.write("\tvmkc.mouse.click(%s, %s, %s)\n" % (int(point.x), int(point.y), vmkc.MOUSEKEY_LEFT))
        
        elif order.upper() == 'D':
            point = vmkc.CTypePoint()
            ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
            vmkc.mouse.double_click(int(point.x), int(point.y), vmkc.MOUSEKEY_LEFT)
            file.write("\tprint(\"\\r[%%d] Double click at (%s, %s) !  \\t\\t\\t\\t\" %% count, end = '')\n" % (int(point.x), int(point.y)))
            file.write("\tvmkc.mouse.double_click(%s, %s, %s)\n" % (int(point.x), int(point.y), vmkc.MOUSEKEY_LEFT))
        
        elif order.upper() == 'M':
            while order.upper() != 'S':
                order = input("   | Choose the start point (Press 'S'): ")
            point1 = vmkc.CTypePoint()
            ctypes.windll.user32.GetCursorPos(ctypes.byref(point1))
            while order.upper() != 'E':
                order = input("   | Choose the end point (Press 'E'): ")
            point2 = vmkc.CTypePoint()
            ctypes.windll.user32.GetCursorPos(ctypes.byref(point2))
            vmkc.mouse.move(int(point1.x), int(point1.y), int(point2.x), int(point2.y), vmkc.MOUSEKEY_LEFT)
            file.write("\tprint(\"\\r[%%d] Move from (%s, %s) to (%s, %s) !  \\t\\t\\t\\t\" %% count, end = '')\n" % (int(point1.x), int(point1.y), int(point2.x), int(point2.y)))
            file.write("\tvmkc.mouse.move(%s, %s, %s, %s, %s)\n" % (int(point1.x), int(point1.y), int(point2.x), int(point2.y), vmkc.MOUSEKEY_LEFT))
        
        elif order.upper() == 'B':
            # vmkc.keyboard.press(vmkc.KEY_CODE["backspace"])
            file.write("\tprint(\"\\r[%%d] Press 'BACKSPACE' !  \\t\\t\\t\\t\" %s count, end = '')\n" % '%')
            file.write("\tvmkc.keyboard.press(%s)\n" % vmkc.KEY_CODE["backspace"])
        
        elif order.upper() == 'E':
            # vmkc.keyboard.press(vmkc.KEY_CODE["enter"])
            file.write("\tprint(\"\\r[%%d] Press 'ENTER' !  \\t\\t\\t\\t\" %s count, end = '')\n" % '%')
            file.write("\tvmkc.keyboard.press(%s)\n" % vmkc.KEY_CODE["enter"])
        
        elif order.upper() == 'N':
            # vmkc.keyboard.press(vmkc.KEY_CODE["down"])
            file.write("\tprint(\"\\r[%%d] Press 'ARROWDOWN' !  \\t\\t\\t\\t\" %s count, end = '')\n" % '%')
            file.write("\tvmkc.keyboard.press(%s)\n" % vmkc.KEY_CODE["down"])
        
        elif order.upper() == 'L':
            # vmkc.keyboard.press(vmkc.KEY_CODE["up"])
            file.write("\tprint(\"\\r[%%d] Press 'ARROWUP' !  \\t\\t\\t\\t\" %s count, end = '')\n" % '%')
            file.write("\tvmkc.keyboard.press(%s)\n" % vmkc.KEY_CODE["up"])
        
        elif order.upper() == 'S':
            # vmkc.keyboard.press(vmkc.KEY_CODE["space"])
            file.write("\tprint(\"\\r[%%d] Press 'SPACE' !  \\t\\t\\t\\t\" %s count, end = '')\n" % '%')
            file.write("\tvmkc.keyboard.press(%s)\n" % vmkc.KEY_CODE["space"])
        
        elif order.upper() == 'J':
            while order.upper() != 'S':
                order = input("   | Choose the left-top point (Press 'S'): ")
            point1 = vmkc.CTypePoint()
            ctypes.windll.user32.GetCursorPos(ctypes.byref(point1))
            while order.upper() != 'E':
                order = input("   | Choose the right-bottom point (Press 'E'): ")
            point2 = vmkc.CTypePoint()
            ctypes.windll.user32.GetCursorPos(ctypes.byref(point2))
            print("   | Input the window name : ", end = '')
            judge_name = input()
            judge_std_path = "./tmp/" + auto_task_name + "_" + judge_name + "_std.png"
            judge_tmp_path = "./tmp/" + auto_task_name + "_" + judge_name + "_tmp.png"
            vmkc.screen_grab((int(point1.x), int(point1.y), int(point2.x), int(point2.y)), judge_std_path)
            
            file.write("\tvmkc.screen_grab((%s, %s, %s, %s), \"%s\")\n" % (int(point1.x), int(point1.y), int(point2.x), int(point2.y), judge_tmp_path ))
            file.write("\tprocessed = False\n")
            file.write("\tprint(\"\\r[%%d] Waiting for judgement ...  \\t\\t\\t\\t\" %s count, end = '')\n" % '%')
            file.write("\twhile not processed:\n")
            file.write("\t\tprocessed = vmkc.brute_force_judge(\"%s\", \"%s\")\n" % (judge_std_path, judge_tmp_path ))
            file.write("\t\ttime.sleep(1)\n")
            file.write("\t\tvmkc.screen_grab((%s, %s, %s, %s), \"%s\")\n" % (int(point1.x), int(point1.y), int(point2.x), int(point2.y), judge_tmp_path ))

        elif order.upper() == 'Q':
            break
        
        else:
            continue
        
        file.write("\ttime.sleep(1)\n")
    
    file.write("\tprint(\"\\r[%%d] Finished !  \\t\\t\\t\\t\" %s count, end = '')\n" % '%')
    file.close()
    
    return True


if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description = "Record the auto task worked by vitural mouse-keyboard control.")
    parser.add_argument("--task", type = str, default = "auto-task-demo", help = "The name of the auto task.")
    parser.add_argument("--times", type = int, default = -1, help = "The times you want the task to auto work. (Default is infinity)")
    args = parser.parse_args()
    
    if not os.path.exists("./tmp"):
        os.mkdir("./tmp")

    print("====================AUTOTASK-VMKC===================")
    print()
    for operation in OPERATION_MENU:
        print(operation)
    print()
        
    print("Recording [%s] Start." % args.task)
    ret = record_generate(args.task, args.times)
    if ret:
        print("Recording Task Done.")

    print()
    print("=======================[EXIT]=======================")
