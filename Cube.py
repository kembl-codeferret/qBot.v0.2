# this the cube emulation biatch

class Piece:
    def __init__(self, pos, ori):
        self.pos = pos  # position - where the piece is
        self.ori = ori  # orientation - how the piece is rotated

    def move(self, pos, ori):
        self.pos = pos # new pos
        self.ori = ori # new ori

# cube is held with green in front and white on top
# piece number starts at 0 with wbo corner and goes across from l to r when solved

# position is equal to the pieces number when solved, otherwise correlating to where the piece is on the cube

# corner orientation is 0 when the w or y face of the piece is on the w or y face of the cube
    # from there orientation is the number of clockwise rotations from 0

# edge orientation is 0 when one or more of the faces of the piece is on the same or opposite face of the cube
    # otherwise orientation is 1

class Cube:
    def __init__(self):
        self.pieces = [Piece(n, 0) for n in range(26)]
        # creates a list of pieces with three values: the piece number, position, and orientation
        print("cube formed")

    # find what piece is in a certain position
    def locate(self, pos):
        for i in self.pieces:
            if i.pos == pos:
                return i

    @staticmethod
    def flipcheck(piece, axis):
        if axis == "X": # R/L
            if piece == 1 or piece == 7 or piece == 18 or piece == 24:
                if piece.ori == 1:
                    return 0
                else:
                    return 1
            else:
                return piece.ori
        elif axis == "Y": # U/D
            if piece == 9 or piece == 11 or piece == 14 or piece == 16:
                if piece.ori == 1:
                    return 0
                else:
                    return 1
            else:
                return piece.ori
        elif axis == "Z": # F/B
            if piece == 3 or piece == 5 or piece == 20 or piece == 22:
                if piece.ori == 1:
                    return 0
                else:
                    return 1
            else:
                return piece.ori

    def run_slice(self, string):
        for i in string.split(" "):
            self.turn(i)

    def turn(self, side):
        match side:
            # Right side
            case "R": # moving pos {2c 5e 8c 11e 16e 19c 22e 25c} -> {19c 11e 2c 22e 5e 25c 16e 8c}
                moving = list(self.locate(n) for n in [2, 5, 8, 11, 16, 19, 22, 25])
                to = [19, 11, 2, 22, 5, 25, 16, 8]
                axis = "X"

                moving[0].move(to[0], moving[0].ori - 1) # 2 -> 19
                moving[1].move(to[1], self.flipcheck(moving[1], axis)) # 5 -> 11
                moving[2].move(to[2], moving[2].ori + 1) # 8 -> 2
                moving[3].move(to[3], self.flipcheck(moving[3], axis)) # 11 -> 22
                moving[4].move(to[4], self.flipcheck(moving[4], axis)) # 16 -> 5
                moving[5].move(to[5], moving[5].ori + 1) # 19 -> 25
                moving[6].move(to[6], self.flipcheck(moving[6], axis)) # 22 -> 16
                moving[7].move(to[7], moving[7].ori - 1) # 25 -> 8

            case "R'":  # moving pos {2c 5e 8c 11e 16e 19c 22e 25c} -> {8c 16e 25c 5e 22e 2c 11e 19c}
                moving = list(self.locate(n) for n in [2, 5, 8, 11, 16, 19, 22, 25])
                to = [8, 16, 25, 5, 22, 2, 11, 19]
                axis = "X"

                moving[0].move(to[0], moving[0].ori - 1)  # 2 -> 8
                moving[1].move(to[1], self.flipcheck(moving[1], axis))  # 5 -> 16
                moving[2].move(to[2], moving[2].ori + 1)  # 8 -> 25
                moving[3].move(to[3], self.flipcheck(moving[3], axis))  # 11 -> 5
                moving[4].move(to[4], self.flipcheck(moving[4], axis))  # 16 -> 22
                moving[5].move(to[5], moving[5].ori + 1)  # 19 -> 2
                moving[6].move(to[6], self.flipcheck(moving[6], axis))  # 22 -> 11
                moving[7].move(to[7], moving[7].ori - 1)  # 25 -> 19

            case "R2":  # moving pos {2c 5e 8c 11e 16e 19c 22e 25c} -> {25c 22e 19c 16e 11e 8c 5e 2c}
                moving = list(self.locate(n) for n in [2, 5, 8, 11, 16, 19, 22, 25])
                to = [25, 22, 19, 16, 11, 8, 5, 2]

                moving[0].move(to[0], moving[0].ori)  # 2 -> 25
                moving[1].move(to[1], moving[1].ori)  # 5 -> 22
                moving[2].move(to[2], moving[2].ori)  # 8 -> 19
                moving[3].move(to[3], moving[3].ori)  # 11 -> 16
                moving[4].move(to[4], moving[4].ori)  # 16 -> 11
                moving[5].move(to[5], moving[5].ori)  # 19 -> 8
                moving[6].move(to[6], moving[6].ori)  # 22 -> 5
                moving[7].move(to[7], moving[7].ori)  # 25 -> 2

            # Left Side
            case "L":
                moving = list(self.locate(n) for n in [0, 3, 6, 9, 14, 17, 20, 23])
                to = [6, 14, 23, 3, 20, 0, 9, 17]
                axis = "X"

                moving[0].move(to[0], moving[0].ori + 1)
                moving[1].move(to[1], self.flipcheck(moving[1], axis))
                moving[2].move(to[2], moving[2].ori - 1)
                moving[3].move(to[3], self.flipcheck(moving[3], axis))
                moving[4].move(to[4], self.flipcheck(moving[4], axis))
                moving[5].move(to[5], moving[5].ori - 1)
                moving[6].move(to[6], self.flipcheck(moving[6], axis))
                moving[7].move(to[7], moving[7].ori + 1)

            case "L'":
                moving = list(self.locate(n) for n in [0, 3, 6, 9, 14, 17, 20, 23])
                to = [17, 9, 0, 20, 3, 23, 14, 6]
                axis = "X"

                moving[0].move(to[0], moving[0].ori + 1)
                moving[1].move(to[1], self.flipcheck(moving[1], axis))
                moving[2].move(to[2], moving[2].ori - 1)
                moving[3].move(to[3], self.flipcheck(moving[3], axis))
                moving[4].move(to[4], self.flipcheck(moving[4], axis))
                moving[5].move(to[5], moving[5].ori - 1)
                moving[6].move(to[6], self.flipcheck(moving[6], axis))
                moving[7].move(to[7], moving[7].ori + 1)

            case "L2":
                moving = list(self.locate(n) for n in [0, 3, 6, 9, 14, 17, 20, 23])
                to = [23, 20, 6, 14, 9, 6, 3, 0]

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], moving[1].ori)
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], moving[3].ori)
                moving[4].move(to[4], moving[4].ori)
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], moving[6].ori)
                moving[7].move(to[7], moving[7].ori)

            # Front Side
            case "F":
                moving = list(self.locate(n) for n in [6, 7, 8, 14, 16, 23, 24, 25])
                to = [8, 16, 25, 7, 24, 6, 14, 23]
                axis = "Z"

                moving[0].move(to[0], moving[0].ori + 1)
                moving[1].move(to[1], self.flipcheck(moving[1], axis))
                moving[2].move(to[2], moving[2].ori - 1)
                moving[3].move(to[3], self.flipcheck(moving[3], axis))
                moving[4].move(to[4], self.flipcheck(moving[4], axis))
                moving[5].move(to[5], moving[5].ori - 1)
                moving[6].move(to[6], self.flipcheck(moving[6], axis))
                moving[7].move(to[7], moving[7].ori + 1)

            case "F'":
                moving = list(self.locate(n) for n in [6, 7, 8, 14, 16, 23, 24, 25])
                to = [23, 14, 6, 24, 7, 25, 16, 8]
                axis = "Z"

                moving[0].move(to[0], moving[0].ori + 1)
                moving[1].move(to[1], self.flipcheck(moving[1], axis))
                moving[2].move(to[2], moving[2].ori - 1)
                moving[3].move(to[3], self.flipcheck(moving[3], axis))
                moving[4].move(to[4], self.flipcheck(moving[4], axis))
                moving[5].move(to[5], moving[5].ori - 1)
                moving[6].move(to[6], self.flipcheck(moving[6], axis))
                moving[7].move(to[7], moving[7].ori + 1)

            case "F2":
                moving = list(self.locate(n) for n in [6, 7, 8, 14, 16, 23, 24, 25])
                to = [25, 24, 23, 16, 14, 8, 7, 6]

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], moving[1].ori)
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], moving[3].ori)
                moving[4].move(to[4], moving[4].ori)
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], moving[6].ori)
                moving[7].move(to[7], moving[7].ori)

            # Back Side
            case "B":
                moving = list(self.locate(n) for n in [0, 1, 2, 9, 11, 17, 18, 19])
                to = [17, 9, 0, 18, 1, 19, 11, 2]
                axis = "Z"

                moving[0].move(to[0], moving[0].ori - 1)
                moving[1].move(to[1], self.flipcheck(moving[1], axis))
                moving[2].move(to[2], moving[2].ori + 1)
                moving[3].move(to[3], self.flipcheck(moving[3], axis))
                moving[4].move(to[4], self.flipcheck(moving[4], axis))
                moving[5].move(to[5], moving[5].ori + 1)
                moving[6].move(to[6], self.flipcheck(moving[6], axis))
                moving[7].move(to[7], moving[7].ori - 1)

            case "B'":
                moving = list(self.locate(n) for n in [0, 1, 2, 9, 11, 17, 18, 19])
                to = [2, 11, 19, 1, 18, 0, 9, 17]
                axis = "Z"

                moving[0].move(to[0], moving[0].ori - 1)
                moving[1].move(to[1], self.flipcheck(moving[1], axis))
                moving[2].move(to[2], moving[2].ori + 1)
                moving[3].move(to[3], self.flipcheck(moving[3], axis))
                moving[4].move(to[4], self.flipcheck(moving[4], axis))
                moving[5].move(to[5], moving[5].ori + 1)
                moving[6].move(to[6], self.flipcheck(moving[6], axis))
                moving[7].move(to[7], moving[7].ori - 1)

            case "B2":
                moving = list(self.locate(n) for n in [0, 1, 2, 9, 11, 17, 18, 19])
                to = [19, 18, 17, 11, 9, 2, 1, 0]

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], moving[1].ori)
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], moving[3].ori)
                moving[4].move(to[4], moving[4].ori)
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], moving[6].ori)
                moving[7].move(to[7], moving[7].ori)

            # Up Side
            case "U":
                moving = list(self.locate(n) for n in [0, 1, 2,
                                                       3,    5,
                                                       6, 7, 8])
                to = [2, 5, 8, 1, 7, 0, 3, 6]
                axis = "Y"

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], self.flipcheck(moving[1], axis))
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], self.flipcheck(moving[3], axis))
                moving[4].move(to[4], self.flipcheck(moving[4], axis))
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], self.flipcheck(moving[6], axis))
                moving[7].move(to[7], moving[7].ori)

            case "U'":
                moving = list(self.locate(n) for n in [0, 1, 2, 3, 5, 6, 7, 8])
                to = [6, 3, 0, 7, 1, 8, 5, 2]
                axis = "Y"

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], self.flipcheck(moving[1], axis))
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], self.flipcheck(moving[3], axis))
                moving[4].move(to[4], self.flipcheck(moving[4], axis))
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], self.flipcheck(moving[6], axis))
                moving[7].move(to[7], moving[7].ori)

            case "U2":
                moving = list(self.locate(n) for n in [0, 1, 2, 3, 5, 6, 7, 8])
                to = [8, 7, 6, 5, 3, 2, 1, 0]

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], moving[1].ori)
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], moving[3].ori)
                moving[4].move(to[4], moving[4].ori)
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], moving[6].ori)
                moving[7].move(to[7], moving[7].ori)

            # Down Side
            case "D":
                moving = list(self.locate(n) for n in [17, 18, 19, 20, 22, 23, 24, 25])
                to = [23, 20, 17, 24, 18, 25, 22, 19]
                axis = "Y"

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], self.flipcheck(moving[1], axis))
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], self.flipcheck(moving[3], axis))
                moving[4].move(to[4], self.flipcheck(moving[4], axis))
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], self.flipcheck(moving[6], axis))
                moving[7].move(to[7], moving[7].ori)

            case "D'":
                moving = list(self.locate(n) for n in [17, 18, 19, 20, 22, 23, 24, 25])
                to = [19, 22, 25, 18, 24, 17, 20, 23]
                axis = "Y"

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], self.flipcheck(moving[1], axis))
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], self.flipcheck(moving[3], axis))
                moving[4].move(to[4], self.flipcheck(moving[4], axis))
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], self.flipcheck(moving[6], axis))
                moving[7].move(to[7], moving[7].ori)

            case "D2":
                moving = list(self.locate(n) for n in [17, 18, 19, 20, 22, 23, 24, 25])
                to = [25, 24, 23, 22, 20, 19, 18, 17]

                moving[0].move(to[0], moving[0].ori)
                moving[1].move(to[1], moving[1].ori)
                moving[2].move(to[2], moving[2].ori)
                moving[3].move(to[3], moving[3].ori)
                moving[4].move(to[4], moving[4].ori)
                moving[5].move(to[5], moving[5].ori)
                moving[6].move(to[6], moving[6].ori)
                moving[7].move(to[7], moving[7].ori)
        for i in self.pieces:
            while i.ori < 0:
                i.ori += 3
            while i.ori > 2:
                i.ori -= 3

