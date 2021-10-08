def ipv4_checker(ipv4):
    counter = [sum(0 <= int(ip) <= 225 for ip in ipv4.split("."))]

    if counter[0] == 4:
        print(ipv4, "is a valid IPV4 address")
    else:
        print(ipv4, "is NOT a valid IPV4 address")


ipv4_checker("192.168.0")
ipv4_checker("192.168.0.1")
