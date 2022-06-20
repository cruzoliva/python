def arithmetic_arranger(problems, resolve):
#problems = ["32 + 8", "1 + 3801", "9999 + 9999", "523 + 49"]
#resolve = True
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    if len(problems) > 5: 
        print("Error: Too many problems.")
        return
    
    for problem in problems:
        #print(problem)
        problem_det = problem.split(" ")
        result = ""

        if not isInteger(problem_det[0]) or not isInteger(problem_det[2]):
            print("Error: Numbers must only contain digits.")
            return
        
        if len(problem_det[0]) > 4 or len(problem_det[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return

        if resolve:
            if problem_det[1] == "+":
                result = int(problem_det[0]) + int(problem_det[2])
            elif problem_det[1] == "-":
                result = int(problem_det[0]) - int(problem_det[2])
            else:
                print("Error: Operator must be '+' or '-'.")
                return  

        len1 = len(problem_det[0])
        len2 = len(problem_det[2])
        lenr = len(str(result))

        if len1 > len2:
            max_len = len1
        elif len2 > lenr:
            max_len = len2
        else:
            max_len = lenr

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

