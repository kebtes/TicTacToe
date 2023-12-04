from tabulate import tabulate

class TicTacToe:   
    def __init__(self) -> None:
        self.row1 = ["_","_","_"]
        self.row2 = ["_","_","_"]
        self.row3 = ["_","_","_"]

    def check_space(self, location):
        empty = True
    
        if location < 4:
            row = 1
        elif location < 7:
            row = 2
        elif location < 10:
            row = 3
    
        if row == 1:
            index = location - 1
            if self.row1[index] == "_":
                pass
            else: empty = False
        elif row == 2:
            index = location - 4
            if self.row2[index] == "_":
                pass
            else: empty = False
        else:
            index = location - 7
            if self.row3[index] == "_":
                pass
            else: empty = False
    
        return empty

    def board_updater(self, location = None, value = None):
        row = 0
        index = 0

        if location != None and value != None:
            location = int(location)
            # row check
            if location < 4:
                row = 1
            elif location < 7:
                row = 2
            elif location < 10:
                row = 3

            # index find and update
            if row == 1:
                index = location - 1
                self.row1[index] = value

            elif row == 2:
                index = location - 4
                self.row2[index] = value

            else:
                index = location - 7
                self.row3[index] = value

            return [self.row1,self.row2,self.row3]
        else: 
            return [self.row1,self.row2,self.row3]
    
    def draw_check(self, l1,l2,l3):
        isDraw = False
        blank_space = False

        rows = [l1,l2,l3]
        for row in rows:
            for item in row:
                if item == "_":
                    blank_space = True
                    break

        if not blank_space and not self.win_check(self.row1,self.row2,self.row3):
            isDraw = True

        return isDraw

    def win_check(self, l1,l2,l3):
        isWin = False

        def check_all_elements(lst):
            check_for_x = all(elmnt == "X" for elmnt in lst)
            check_for_o = all(elmnt == "O" for elmnt in lst)

            if check_for_x or check_for_o:
                return True
            else: return False

        # HORIZONTAL CHECK
        result_row_1 = check_all_elements(l1)
        result_row_2 = check_all_elements(l2)
        result_row_3 = check_all_elements(l3)

        # VERTICAL CHECK
        column_1 = [l1[0],l2[0],l3[0]]
        column_2 = [l1[1],l2[1],l3[1]]
        column_3 = [l1[2],l2[2],l3[2]]

        result_column_1 = check_all_elements(column_1)
        result_column_2 = check_all_elements(column_2)
        result_column_3 = check_all_elements(column_3)

        # DIAGONAL CHECK
        diag_1 = [l1[0],l2[1],l3[2]]
        diag_2 = [l1[2],l2[1],l3[0]]

        result_diag_1 = check_all_elements(diag_1)
        result_diag_2 = check_all_elements(diag_2)

        all_poss =  [result_column_1, result_column_2, result_column_3,
                    result_row_1, result_row_2, result_row_3,
                    result_diag_1, result_diag_2]

        isWin = any(all_poss)

        def who_won():    
            # WINNER CHECK
            while True:
                if result_row_1:
                    winner = l1[0]
                elif result_row_2:
                    winner = l2[0]
                elif result_row_3:
                    winner = l3[0]

                if result_column_1:
                    winner = column_1[0]
                elif result_column_2:
                    winner = column_2[0]
                elif result_column_3:
                    winner = column_3[0]

                if result_diag_1:
                    winner = diag_1[0]
                elif result_diag_2:
                    winner = diag_2[0]

                if winner:
                    return winner

        if isWin: return who_won()
        else: return None

    def game_play(self):
        choices = ["X","O"]
        print("*******************************************************\n"
            "*                                                     *\n"
            "*                WELCOME TO TIC-TAC-TOE               *\n"
            "*                                                     *\n"
            "*******************************************************")

        while True:
            try:
                player_1 = str(input("Make a choice, X or O?: ").strip()).upper()
                player_2 = [x for x in choices if x != player_1][0]

                if player_1 not in choices:
                    raise ValueError
                break

            except ValueError:
                print("Invalid input")

        players = [player_1, player_2]
        player = player_1
        print(f"First player choice: {player_1} \nSecond player choice: {player_2[0]}")
        rows = self.board_updater()

        #gameplay
        while True:
            print(tabulate(rows, tablefmt="grid"))

            while True:
                try:
                    location = input(f"Player {player}, please enter a location: ")
                    if int(location) > 9 or int(location) < 1:
                        raise ValueError
                    if self.check_space(int(location)) == False:
                        print("Spot already taken!")
                        continue
                    break

                except ValueError:
                    print("Please enter a valid location")

            rows = self.board_updater(location, player)
            player = [x for x in players if x != player][0]

            win = self.win_check(self.row1,self.row2,self.row3)
            draw = self.draw_check(self.row1,self.row2,self.row3)

            if win:
                print(tabulate(rows, tablefmt="grid"))
                print(f"*******************************************************\n"
                       "*                                                     *\n"
                       "*                TIC-TAC-TOE - GAME OVER!             *\n"
                       f"*                WINNER IS:  {win}                        *\n"
                       "*                                                     *\n"
                       "*******************************************************")
                break
            if draw:
                print(tabulate(rows, tablefmt="grid"))
                print(f"*******************************************************\n"
                       "*                                                     *\n"
                       "*                 TIC-TAC-TOE - DRAW GAME!            *\n"
                       "*                                                     *\n"
                       "*******************************************************")
                break


tictactoe = TicTacToe()
tictactoe.game_play()