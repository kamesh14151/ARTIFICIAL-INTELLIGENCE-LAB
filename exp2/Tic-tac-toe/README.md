# Tic-Tac-Toe using Minimax Algorithm

## Ex No: 2(c) — Adversarial Search and Game Playing

---

## Aim

To implement a Tic-Tac-Toe game using the **Minimax algorithm** where the AI plays optimally against a human player.

---

## Algorithm

1. Initialize an empty 3×3 board.
2. Display the board and let the **User (X)** enter a move.
3. Check if the user has won or if the board is full (draw). If yes, end the game.
4. Use the **Minimax function** to determine the **best move** for the AI (O):
   - If the current state is a terminal state (win/draw), return the score (+1, -1, or 0).
   - If it is the **AI's turn (MAX)**, choose the move with the **maximum** score.
   - If it is the **User's turn (MIN)**, choose the move with the **minimum** score.
   - Recursively evaluate all possible future moves.
5. AI makes the best move found by Minimax.
6. Check if the AI has won or if the board is full (draw). If yes, end the game.
7. Repeat steps 2–6 until the game ends.
8. Display the winner or announce a draw.

---

## Program

```python
import math

board = [' '] * 9

def print_board():
    print()
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---+---+---")
    print()

def check_winner(b, player):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(b[a]==b[c1]==b[c2]==player for a,c1,c2 in wins)

def is_full(b):
    return ' ' not in b

def minimax(b, is_max):
    if check_winner(b, 'O'):
        return 1
    if check_winner(b, 'X'):
        return -1
    if is_full(b):
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                best = max(best, minimax(b, False))
                b[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                best = min(best, minimax(b, True))
                b[i] = ' '
        return best

def best_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            val = minimax(board, False)
            board[i] = ' '
            if val > best_val:
                best_val = val
                move = i
    return move

def play():
    print("Tic-Tac-Toe: You are X, AI is O")
    print("Positions: 1-9 (left-to-right, top-to-bottom)")

    while True:
        print_board()

        # User move
        while True:
            try:
                pos = int(input("Enter your move (1-9): ")) - 1
                if 0 <= pos <= 8 and board[pos] == ' ':
                    break
                print("Invalid move. Try again.")
            except ValueError:
                print("Enter a number between 1 and 9.")

        board[pos] = 'X'

        if check_winner(board, 'X'):
            print_board()
            print("Congratulations! You win!")
            break
        if is_full(board):
            print_board()
            print("It's a Draw!")
            break

        # AI move
        print("AI is thinking...")
        ai_pos = best_move()
        board[ai_pos] = 'O'
        print(f"AI plays at position {ai_pos + 1}")

        if check_winner(board, 'O'):
            print_board()
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print_board()
            print("It's a Draw!")
            break

play()
```

---

## Output

```
Tic-Tac-Toe: You are X, AI is O
Positions: 1-9 (left-to-right, top-to-bottom)

   |   |   
---+---+---
   |   |   
---+---+---
   |   |   

Enter your move (1-9): 5
AI is thinking...
AI plays at position 1

 O |   |   
---+---+---
   | X |   
---+---+---
   |   |   

Enter your move (1-9): 9
AI is thinking...
AI plays at position 3

 O |   | O 
---+---+---
   | X |   
---+---+---
   |   | X 

Enter your move (1-9): 7
AI is thinking...
AI plays at position 2

 O | O | O 
---+---+---
   | X |   
---+---+---
 X |   | X 

AI wins! Better luck next time.
```

---

## Result

The Tic-Tac-Toe game using the **Minimax algorithm** was successfully implemented. The AI evaluates all possible future game states recursively and always plays the optimal move, making it unbeatable.
