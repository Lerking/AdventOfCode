DOUBLES = ['00','11','22','33','44','55','66','77','88','99']
TRIPPLES = ['222','333','444','555','666','777','888','999']
passwords = []

def check_double():
    for pw in range(356261, 846303):
        for d in DOUBLES:
            if d in str(pw):
                passwords.append(pw)

def check_increase(n):
    global passwords
    index = 0
    test = False
    temp = []
    for p in n:
        prev = ""
        checks = []
        for i in str(p):
            if prev is None:
                prev = i
                index += 1
                continue
            if i >= prev:
                checks.append(True)
            else:
                checks.append(False)
            prev = i
        if False in checks:
            continue
        else:
            temp.append(p)
    passwords = temp
    return

def check_larger_group(p):
    global passwords
    ok = False
    temp = []
    for pp in p:
        for n in range(0,10):
            if str(pp).count(str(n)) > 2:
                for t in DOUBLES:
                    if str(pp).endswith(t) and str(n) in t:
                        ok = False
                        break
                    else:
                        ok = True
                if ok == False:
                    break
        if ok == True:
            temp.append(pp)
        ok = False
    passwords = temp
    return
    

                

def check_passwords():
    check_double()
    check_increase(passwords)
    check_larger_group(passwords)

if __name__ == "__main__":
    
    check_passwords()

    # Number of unique passwords
    print(len(set(passwords))) #day 4, part 1