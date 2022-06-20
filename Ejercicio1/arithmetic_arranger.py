def arithmetic_arranger(problems, resolve):
#problems = ["32 + 8", "1 + 3801", "9999 + 9999", "523 + 49"]
#resolve = True
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    #Valido cantidad de problemas que puede resolver la función
    if len(problems) > 5: 
        print("Error: Too many problems.")
        return
    #Separo con un split donde hay espacios para tener los valores y el operador    
    for problem in problems:
        #print(problem)
        problem_det = problem.split(" ")
        result = ""
        #Valido que los valores solo puedan recibir integer para resolver el problema
        if not isInteger(problem_det[0]) or not isInteger(problem_det[2]):
            print("Error: Numbers must only contain digits.")
            return
        #Valido que cada valor ingresado no debe superar los cuatro dígitos        
        if len(problem_det[0]) > 4 or len(problem_det[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return
        #Valido que las operaciones a realizar sólo sean sumas o restas 
        if resolve:
            if problem_det[1] == "+":
                result = int(problem_det[0]) + int(problem_det[2])
            elif problem_det[1] == "-":
                result = int(problem_det[0]) - int(problem_det[2])
            else:
                print("Error: Operator must be '+' or '-'.")
                return  
        #Verifico el largo de los valores con el operador para poder saber cuanto espacio va a ocupar cada cuenta
        len1 = len(problem_det[0])
        len2 = len(problem_det[2])
        lenr = len(str(result))

        if len1 > len2:
            max_len = len1
        elif len2 > lenr:
            max_len = len2
        else:
            max_len = lenr
        #Le asigno valor a cada línea 
        #print(problem_det[0], problem_det[1], problem_det[2], result)
        cur_len = max_len + 2
        line1 = line1 + ("".rjust(cur_len + 2, " ") + problem_det[0])[cur_len * -1:] + "    "
        line2 = line2 + problem_det[1] + " " + ("".rjust(max_len, " ") + problem_det[2])[max_len * -1:] + "    "
        line3 = line3 + "".rjust(cur_len, "-") + "    "
        line4 = line4 + ("".rjust(cur_len + 2, " ") + str(result))[cur_len * -1:] + "    "

    print(line1)
    print(line2)
    print(line3)
    print(line4)

def isInteger(number):
    try:
        int(number)
        return True
    except:
        return False 

