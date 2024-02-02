'''
    Project     : AutoTask-VMKC
    File        : cursor.py
    Description : Show cursor coordinate for all time. In order to modify the arguments manually.
    Author      : lysheng (@TJ-CVRSG)
    Date        : 2024-02-02
    Version     : 1.0
'''


import ctypes
import vmkc


if __name__ == "__main__":    
    while True:
        point = vmkc.CTypePoint()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
        print("\rCursor @ (%d, %d)  \t\t\t\t" % (int(point.x), int(point.y)), end = '')
