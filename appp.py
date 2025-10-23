def broke(quarters, m1, m2, m3):
    M1 = 35 - m1
    M2 = 100 - m2
    M3 = 10 - m3
    Martha = quarters
    numplays = 0
    while True:
        if Martha > 0:
            Martha -= 1
            M1 -= 1
            numplays += 1
            if M1 == 0:
                M1 += 35
                Martha += 30
            M2 -= 1
            numplays += 1
            if M2 == 0:
                Martha += 60
                M2 += 100
                Martha -= 1
            M3 -= 1
            numplays += 1
            if M3 == 0:
                Martha += 9
                M3 += 10
                Martha -= 1
            else:
                print(f"Martha played {numplays} before going broke")
                break
broke(10,9,5,9)


