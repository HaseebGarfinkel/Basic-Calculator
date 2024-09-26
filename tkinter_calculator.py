import tkinter

window = tkinter.Tk()
window.title("Simple Calculator")
window.geometry("390x375")
window.resizable(0, 0)
text = tkinter.Text(master=window, height = 1, width = 20, font = ("Times New Roman", 30))
text.grid(column = 0, row = 0, columnspan = 4)
text.insert(tkinter.END,"0")

first_press = True
operation_complete = False
undefined = False
operation = ["", "", ""]

def numbers(num):
    global undefined
    global operation_complete
    global first_press
    global operation

    if first_press:
        text.delete("1.0", tkinter.END)
        first_press = False

    if undefined:
        text.delete("1.0", tkinter.END)
        operation[0] = num
        undefined = False

    elif operation[1] != "":
        operation[2] += num
    elif operation_complete == False:
        operation[0] += num
    else:
        operation[0] = num

    operation_complete = False
    text.insert(tkinter.END, num)
    print(operation)

def decimal():
    global operation

    if operation[1] == "":
        if "." not in operation[0]:
            operation[0] += "." 
            text.delete("1.0", tkinter.END)
            text.insert(tkinter.END, operation[0])
    else:
        if "." not in operation[2]:
            operation[2] += "." 
            text.delete("1.0", tkinter.END)
            text.insert(tkinter.END, operation[2])

def operator(op):
    global undefined
    global operation
    global operation_complete
    if operation[0] != "" and operation[1] == "/" and operation[2] == "0":
        text.delete("1.0", tkinter.END)
        text.insert(tkinter.END, "UNDEFINED")
        undefined = True
        operation[0] = ""
        operation[1] = ""
        operation[2] = ""
    elif operation[0] != "" and operation[1] != "" and operation[2] != "":
        answer = calculator()
        text.delete("1.0", tkinter.END)
        text.insert(tkinter.END, str(answer))
        operation[0] = str(answer)
        operation[1] = str(op)
        operation[2] = ""
        return

    if operation[0] != "":
        operation[1] = op 
        text.delete("1.0", tkinter.END)
        print(operation)
        operation_complete = False

def calculator():
    global undefined
    global operation_complete
    global first_press
    global operation

    if operation[0] != "" and operation[1] == "/" and operation[2] == "0":
        text.delete("1.0", tkinter.END)
        text.insert(tkinter.END, "UNDEFINED")
        operation[0] = ""
        operation[1] = ""
        operation[2] = ""
        first_press = True
        operation_complete = False
        undefined = True
        print(operation)

    elif operation[0] == "None" or operation[2] == "None":
        text.delete("1.0", tkinter.END)
        text.insert(tkinter.END, "UNDEFINED")
        undefined = True
        operation[0] = ""
        operation[1] = ""
        operation[2] = ""

    elif operation[0] != "" and operation[1] != "" and operation[2] != "":
        if operation[1] == "+":
            answer = float(operation[0]) + float(operation[2])
    

        elif operation[1] == "-":
            answer = float(operation[0]) - float(operation[2])
       

        elif operation[1] == "x":
            answer = float(operation[0]) * float(operation[2])
            

        elif operation[1] == "/":
            answer = float(operation[0]) / float(operation[2])
            
        first_press = True
        text.delete("1.0", tkinter.END)
        text.insert(tkinter.END, answer)
        
        operation[0] = str(answer)
        operation[1] = ""
        operation[2] = ""
        operation_complete = True
        return answer
        
    else:
        text.delete("1.0", tkinter.END)
        operation[0] = ""
        operation[1] = ""
        operation[2] = ""
        operation_complete = False

button_7 = tkinter.Button(command = lambda: numbers("7"), text = "7", font = ("Times New Roman", 30), width = 4)
button_7.grid(column = 0, row = 2)

button_8 = tkinter.Button(command = lambda: numbers("8"), text = "8", font = ("Times New Roman", 30), width = 4)
button_8.grid(column = 1, row = 2)

button_9 = tkinter.Button(command = lambda: numbers("9"), text = "9", font = ("Times New Roman", 30), width = 4)
button_9.grid(column = 2, row = 2)

button_4 = tkinter.Button(command = lambda: numbers("4"), text = "4", font = ("Times New Roman", 30), width = 4)
button_4.grid(column = 0, row = 3)

button_5 = tkinter.Button(command = lambda: numbers("5"), text = "5", font = ("Times New Roman", 30), width = 4)
button_5.grid(column = 1, row = 3)

button_6 = tkinter.Button(command = lambda: numbers("6"), text = "6", font = ("Times New Roman", 30), width = 4)
button_6.grid(column = 2, row = 3)

button_1 = tkinter.Button(command = lambda: numbers("1"), text = "1", font = ("Times New Roman", 30), width = 4)
button_1.grid(column = 0, row = 4)

button_2 = tkinter.Button(command = lambda: numbers("2"), text = "2", font = ("Times New Roman", 30), width = 4)
button_2.grid(column = 1, row = 4)

button_3 = tkinter.Button(command = lambda: numbers("3"), text = "3", font = ("Times New Roman", 30), width = 4)
button_3.grid(column = 2, row = 4)

button_0 = tkinter.Button(command = lambda: numbers("0"), text = "0", font = ("Times New Roman", 30), width = 4)
button_0.grid(column = 0, row = 5)

button_dot = tkinter.Button(command = decimal, text = ".", font = ("Times New Roman", 30), width = 4)
button_dot.grid(column = 1, row = 5)

button_equal = tkinter.Button(command = calculator, text = "=", font = ("Times New Roman", 30), width = 4)
button_equal.grid(column = 2, row = 5)

button_divide = tkinter.Button(command = lambda: operator("/"), text = "/", font = ("Times New Roman", 30), width = 4)
button_divide.grid(column = 3, row = 2)

button_multiply = tkinter.Button(command = lambda: operator("x"), text = "x", font = ("Times New Roman", 30), width = 4)
button_multiply.grid(column = 3, row = 3)

button_minus = tkinter.Button(command = lambda: operator("-"), text = "-", font = ("Times New Roman", 30), width = 4)
button_minus.grid(column = 3, row = 4)

button_plus = tkinter.Button(command = lambda: operator("+"), text = "+", font = ("Times New Roman", 30), width = 4)
button_plus.grid(column = 3, row = 5)



window.mainloop()
