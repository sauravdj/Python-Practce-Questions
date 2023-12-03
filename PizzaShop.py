def get_menu(filename):
    located = open(filename, "r")
    num_of_sets = located.readline()
    num_of_sets = int(num_of_sets)
    menu = {}
    for i in range(num_of_sets):
        line = located.readline()
        line = line.strip()
        items = line.split()
        name_item = items[0]
        price_item = float(items[1])
        menu[name_item] = price_item

    located.close()
    print(menu) 
    return menu


def print_receipt(item, total):
    with open("receipt.txt", "w") as fw:
        fw.write("Receipt\n")
        # for i in range(len(item)):
        #     print(str(item[i]) + "\n")
        #     fw.write("$.2f" % total)

        for i in range(len(item)):
            fw.write(item[i] + "\n")
        fw.write(f"Total: ${total:.2f}\n")        

    fw.close()


def main():
    print("Welcome!")
   # file = str(input("What menu would you like to load?\n"))
    print("menu loaded")
    menu = get_menu("C:\\Users\\Saurav\\Desktop\\brainFuse\\Java Codes\\Python codes\\sample.txt")

    orders = []
    total = 0

    for key in menu:
        print(key.title())

    item = input("What would you like to order?\n")
    item = item.lower()

    while (item != "end"):

        if item in menu: 
            order_item = f"{item} @ ${menu[item]:.2f}" 
            orders.append(order_item) 
            total += menu[item]

            print("Added")
        else:
            print("This is not in the menu")

            for key in menu:
                print(key.title())
            item = input("What would you like to order?\n")
            item = item.lower()

        print_receipt(orders, total)
        print("Goodbye")


main()
