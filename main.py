# fml here we go again

from Cube import Cube

c = Cube()  # this is the cube :)
run = True

print("welcome to qBot")
while run:
    cmd = input("input command\n")
    match cmd.split(" ")[0]:
        case "close":
            print("thank you for using qBot!")
            run = False
        case "print":
            for i in c.pieces:
                print(i.pos, i.ori)
        case "scramble":
            pass
        case "solve":
            pass
        case "f2l":
            pass
        case "debug":  # R' F R F' R U' R' U R U' R' U2 R U' R' U2 R' F R F' R U' R' U R U' R' U2 R U R2 U' R2 U' R2 U2 R2 U R' F' R U R' U' R' F R2 U' R' U2 should return the cube to solved from solved
            c.run_slice("B' L B L' B D' B' D B D' B' D2 B D' B' D2 B' L B L' B D' B' D B D' B' D2 B D B2 D' B2 D' B2 D2 B2 D B' L' B D B' D' B' L B2 D' B' D2")