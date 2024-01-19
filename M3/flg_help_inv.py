from armario_FUNCIONES import*
list = []
flg_000 = True
while flg_000:

    print(menu_help_inv)
    prompt(list)

    opcion1 = input()  # en blanco pendiente
    list.append(opcion1)
    if not opcion1.replace(" ", "").isalpha():
        # print('Invalid action')
        list.append('Invalid action')

    elif opcion1.lower() == 'back':
        clear_screen()
        flg_000 = False


    else:
        # print('Invalid action')
        list.append('Invalid action')

