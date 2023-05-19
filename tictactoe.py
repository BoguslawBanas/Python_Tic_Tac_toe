class Move:
    def __init__(self, x, y, sign):
        self.x=x
        self.y=y
        self.sign=sign
        
class Player:
    def __init__(self, name, sign):
        self.name=name
        self.sign=sign
        
    def get_move(self): 
        print("Gracz: ", self.name)
        x, y = map(int, input().split(" "))
        return Move(x, y, self.sign)  
        
    
class Board:
    def __init__(self):
        self.board = [['_', '_', '_'] for i in range(3)]
        
    def __str__(self):
        return self.get_state()
        
    def get_state(self):
        state =""
        for row in self.board:
            state += "".join(row) + "\n"
        return state
    
    def get_field(self, x, y):
        return self.board[x][y]
        
    def set_field(self, move):
        if self.board[move.x][move.y]=="_":
            self.board[move.x][move.y]=move.sign
            return True
        print("Powtorz ruch!")
        return False
        
class Game:
    def __init__(self):
        self.board = Board()
        self.winning_sign = None
        
    def play(self, player1, player2):
        players = (player1, player2)
        current_player = 0
        while not self.game_over():
            while True:
                move = players[current_player].get_move()
                if self.board.get_field(move.x, move.y)=='_': break
            self.board.set_field(move)
            current_player = (current_player+1) % 2
            print(self.board)
        if self.winning_sign is None:
            print("Nikt nie wygral!")
        elif self.winning_sign == player1.sign:
            print("Wygral ", player1.name, "!")
        else: 
            print("Wygral ", player2.name, "!")    
                        
    def game_over(self):
        for row in range(3):
            if self.board.get_field(row, 0) ==\
                self.board.get_field(row, 1) ==\
                self.board.get_field(row, 2) and\
                self.board.get_field(row, 0) != "_":
                    self.winning_sign=self.board.get_field(row, 0)
                    return True
                
        for column in range(3):
            if self.board.get_field(0, column) ==\
                self.board.get_field(1, column) ==\
                self.board.get_field(2, column) and\
                self.board.get_field(0, column) != "_":
                    self.winning_sign=self.board.get_field(0, column)
                    return True
                
        if self.board.get_field(0, 0) ==\
                self.board.get_field(1, 1) ==\
                self.board.get_field(2, 2) and\
                self.board.get_field(0, 0) != "_":
                    self.winning_sign=self.board.get_field(0, 0)
                    return True
                
        if self.board.get_field(0, 2) ==\
                self.board.get_field(1, 1) ==\
                self.board.get_field(2, 0) and\
                self.board.get_field(0, 2) != "_":
                    self.winning_sign=self.board.get_field(0, 2)
                    return True
                
        if self.is_next_move_possible:
            return False
        
        return False
        
    def is_next_move_possible(self):
        for row in range(3):
            for column in range(3):
                if self.board.get_field(row, column) == '_':
                    return True
        return False
        
p1=input()
p2=input()
player_1 = Player(p1, "o")
player_2 = Player(p2, "x")

game = Game()
game.play(player_1, player_2)
        