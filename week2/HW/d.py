shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()
    for order in orders:
        if not is_existing_target_number_binary(order,menus):
            return False
    return True

def is_existing_target_number_binary(target, array):
    curren_min=0
    current_max=len(array)-1
    current_guess=(current_max+curren_min)//2

    while curren_min<=current_max:
        if array[current_guess]==target:
            return True
        if array[current_guess]<target:
            curren_min=current_guess+1
        else:
            current_max=current_guess-1
        current_guess=(current_max+curren_min)//2
    return False




result = is_available_to_order(shop_menus, shop_orders)
print(result)