def ui():        
    print("How Many Dogs Do You Have?")
    global num
    num = input()
    logic(num)

def logic(num):
    try:
        if int(num)>3:
            print ("That is Soo Many Dogs!!!")
            ui()
        elif int(num)<0:
            print ("You Cant Have Negative Numbers.")
            ui()
        else:
            print ("That Is Just Right")
    except ValueError:
        print ("Enter a Number Please.")
        ui()
       
ui()
