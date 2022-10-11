mult = '*'
div = '/'
plus = '+'
minus = '-'

evaluation = '2 + 2 * 2 / 2'
eval_lst = evaluation.split()
res = 0
i = 0
while len(eval_lst) != 1:
    while True:
        print(i, eval_lst)
        el = eval_lst[i]
        if el == mult or el == div:
            if el == mult:
                res = float(eval_lst[i - 1]) * float(eval_lst[i + 1])
            else:
                res = float(eval_lst[i - 1]) / float(eval_lst[i + 1])
            eval_lst[i] = str(res)
            eval_lst.pop(i + 1)
            eval_lst.pop(i - 1)
            i = 0
        if mult or div not in eval_lst:
            break
        else:
            i += 1

    while True:
        if plus or minus in eval_lst:
            print(i, eval_lst)
            el = eval_lst[i]
            if el == plus or el == minus:
                if el == plus:
                    res = float(eval_lst[i - 1]) + float(eval_lst[i + 1])
                else:
                    res = float(eval_lst[i - 1]) - float(eval_lst[i + 1])
                eval_lst[i] = str(res)
                eval_lst.pop(i + 1)
                eval_lst.pop(i - 1)
                i = 0
                continue
            i += 1
        else:
            break

print(res)

# evalution = evalution.replace(' ', '')
# num_list = []
# num = ''
# for char in evalution:
#     if char.isdigit():
#         num = num + char
#         print(num)
#     else:
#         num_list.append(int(num))
#         num_list.append(char)
#         num = ''
# num_list.append(int(num))
