from lpsolve55 import *


# lp = lpsolve('make_lp', 0, 5)
# lpsolve('set_verbose' , lp , IMPORTANT)
# ret = lpsolve('set_obj_fn', lp, [3, 24, 18, 20, 23])  #euro
# ret = lpsolve('set_minim', lp)
# ret = lpsolve('add_constraint', lp, [110, 205, 160, 420, 260], GE, 2000)  # kcal
# ret = lpsolve('add_constraint', lp, [4, 32, 13, 4, 14], GE, 155)  # prot
# ret = lpsolve('add_constraint', lp, [2, 12, 54, 22, 80], GE, 800)  #  calc
# lpsolve( 'solve' , lp)
# print(lpsolve('get_objective', lp))
# print(lpsolve( 'get_variables' , lp )[0])
# print(lpsolve( 'get_constraints' , lp )[0])


def optireg(prixLait):
    lp = lpsolve('make_lp', 0, 5)
    lpsolve('set_verbose', lp, IMPORTANT)
    ret = lpsolve('set_obj_fn', lp, [3, 24, prixLait, 20, 23])  # euro
    ret = lpsolve('set_minim', lp)
    ret = lpsolve('add_constraint', lp, [110, 205, 160, 420, 260], GE, 2000)  # kcal
    ret = lpsolve('add_constraint', lp, [4, 32, 13, 4, 14], GE, 155)  # prot
    ret = lpsolve('add_constraint', lp, [2, 12, 54, 22, 80], GE, 800)  # calc
    lpsolve('solve', lp)
    print("\nObjectif:")
    print(lpsolve('get_objective', lp))
    print("\nVariables:")
    print(lpsolve('get_variables', lp)[0])
    print("\nContraintes:")
    print(lpsolve('get_constraints', lp)[0])

for i in range(15,20):
    print("\nPrix du lait:", i)
    optireg(i)
