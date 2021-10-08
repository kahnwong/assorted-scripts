def med_needed(name, amount_needed, amount_existed):
    to_buy = amount_needed - amount_existed
    print(name)
    print("=" * 10)
    print("Need:", amount_needed)
    print("Existed:", amount_existed)

    if to_buy <= 0:
        print("NO NEED TO GET")
    else:
        print("GET:", to_buy)
    print("\n")


med_needed("Amlodipine (5 MG)", 34, 2)
med_needed("Atorvastatin (20 MG)", 34, 19)
med_needed("Bisoprolol Fumarate (2.5 MG)", 34, 17)
med_needed("Doxazosin Mesylate (2 MG)", 34, 4)


# need 34
