# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# x = True
# y = False
# z = True

def check_truth(bool_x, bool_y, bool_z):
    if not(bool_x or bool_y or bool_z) == (not(bool_x) and not(bool_y) and not(bool_z)):
        return True
    else:
        return False

if check_truth (True, True, True) and check_truth (False, False, False) and check_truth (True, True, False) and check_truth (True, False, True)\
    and check_truth(False, True, True) and check_truth(True, False, False) and check_truth (False, True, False) and check_truth (False, False, True):
    print(True)
else:
    print(False)