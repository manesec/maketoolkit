import curses,time
import sys
from curses import curs_set, wrapper

#####################################################################
#                               UI
#####################################################################
def UI_item(stdscr,title,subtitle,user_function,):
    user_select = 0
    user_select_page = 0

    while(True):
        stdscr.clear()
        stdscr.keypad(True)
        stdscr.addstr(title)
        rows, cols = stdscr.getmaxyx()
        
        stdscr.addstr(2,0,subtitle,curses.A_BOLD)
        up_down_button = False

        box_top = 4
        box_bottom = rows
        box_high = box_bottom - box_top
        box_item = 0
        
        if (len(user_function) > box_high+1):
            up_down_button = True

            last_index = (user_select_page+1)*(box_high-1)
            if (last_index > len(user_function)):
                last_index = len(user_function)

            display_item_list = user_function[user_select_page*(box_high-1):last_index]

            if (user_select >= len(display_item_list) -1):
                user_select = len(display_item_list) -1

            for item_name,_,__ in display_item_list:
                if (box_item == user_select):
                    stdscr.addstr(3 + box_item,2,item_name,curses.A_REVERSE)
                else:
                    stdscr.addstr(3 + box_item,2,item_name)
                box_item += 1

            stdscr.addstr(box_bottom-1,0,"<%s/%s>"%(user_select_page,(len(user_function)//(box_high-1))),curses.A_BOLD)
            
        else:
            up_down_button = False

            for item_name,_,__ in user_function:
                if (box_item == user_select):
                    stdscr.addstr(3 + box_item,2,item_name,curses.A_REVERSE)
                else:
                    stdscr.addstr(3 + box_item,2,item_name)
                box_item += 1

        stdscr.move(rows-1,cols-1)
        stdscr.refresh()

        # Key events
        input_key = stdscr.getch()
        #print(input_key)
        #sys.exit(0)
        if (input_key == curses.KEY_LEFT):
            user_select_page = user_select_page - 1
            if (user_select_page < 0):
                user_select_page = 0          

        if (input_key == curses.KEY_RIGHT):
            user_select_page = user_select_page + 1
            if (user_select_page > (len(user_function)//(box_high-1))):
                user_select_page = len(user_function)//(box_high-1)
                
        if (input_key in [curses.KEY_UP,119]):
            user_select = user_select - 1
            if (user_select<=0):
                user_select = 0

        if (input_key in [curses.KEY_DOWN,115]):
            if (up_down_button):
                if (user_select >= (box_high-2)):
                    user_select = (box_high-2)
                else:
                    user_select = user_select + 1
            else:
                user_select = user_select + 1
                if (user_select>=len(user_function)):
                    user_select = len(user_function) - 1
        
        if (input_key == curses.KEY_ENTER) or (input_key == 10) or (input_key == 13):
            if (up_down_button):
                if (user_function[user_select_page*(box_high -1) + user_select][1] == "<back>"):
                    break
                (user_function[user_select_page*(box_high -1) + user_select][1])(stdscr,user_function[2])
            else:
                if (user_function[user_select][1] == "<back>"):
                    break
                (user_function[user_select][1])(stdscr,user_function[2])
    stdscr.keypad(False)            
            
#####################################################################
#                               FUNCTION
#####################################################################
def sys_exit(_,__):
    import sys
    print("Bye! by @manesec.")
    sys.exit(0)

#####################################################################
#                               Selecter
#####################################################################    
def select_1_install(stdscr,_):
    import os,sys
    Tools_list = []
    Tools_list.append(["< Back","<back>",None])
    for path,_,files in os.walk("/var/lib/mkt/Tools/Source/"):
        for file in files:
            if (file.find(".mkt")!=0):
                tools_name = (path + "/" + file)
                tools_name = tools_name [len("/var/lib/mkt/Tools/Source/"):-4]
                Tools_list.append([tools_name,sys_exit,None])
    print(Tools_list)
    wrapper(UI_item,"# MKT > Tools Manager","Please select tools",Tools_list)

    return

def select_install():
    return

def main():
    user_function = [
        ["Tools Manager",select_1_install,None],
        ["Search Databases Manager",select_1_install,None],
        ["Script Runner",select_1_install,None]

    ]
    wrapper(UI_item,"# MKT > Home","Please select function:",user_function)



main()