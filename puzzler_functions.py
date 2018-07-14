"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle is the same as view.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    """
    # put the function body here
    
    return puzzle == view


def game_over(puzzle: str, view: str, current_selection: str) -> bool:
    """Return Ture if and only if the puzzle is the same as the
    view or the current selection is QUIT.
    
    current_selection is one of CONSONANT, VOWEL, SOLVE, or QUIT
    
    >>> game_over('banana', 'b^^^^^', QUIT)
    True
    >>> game_over('banana', 'banana', SOLVE)
    True
    >>> game_over('banana', '^a^a^a', SOLVE)
    False
    """
    
    return puzzle == view or current_selection == QUIT


def bonus_letter(puzzle: str, view: str, letter: str) -> bool:
    """Return True if and only if the letter appears in the 
    puzzle but not in its view.
    
    >>> bonus_letter('banana', 'b^^^^^', 'a')
    True
    >>> bonus_letter('banana', 'b^^^^^', 'b')
    False
    >>> bonus_letter('banana', 'b^^^^^', 'k')
    False
    """
    
    return (letter in puzzle) and (not letter in view)


def update_letter_view(puzzle: str, view: str, index: int, 
                       letter_guessed: str)-> str:
    """Return a single character string representing the next 
    view of the character at the given index. If the character 
    at that index of the puzzle matches the letter_guessed, 
    then return that character. Otherwise, return the character 
    at that index of the view.  
        
    >>> update_letter_view('banana', 'b^^^^^', 2, 'n')
    'n'
    >>> update_letter_view('banana', 'b^^^^^', 1, 'b')
    '^'
    """
    
    char = puzzle[index]
    
    if char == letter_guessed:
        return char
    else:
        return view[index]


def calculate_score(current_score: int, occurrence: int,
                    letter_type: str) -> int:
    """ Return the new score by adding CONSONANT_POINTS per occurrence 
    of the letter to the current_score if the letter_type is CONSONANT, 
    or by deducting the VOWEL_PRICE from the current_score if the 
    letter_type is VOWEL.
    
    Precondition: letter_type == CONSONANT or letter_type == VOWEL
    
    >>> calculate_score(0, 2, CONSONANT)
    2
    >>> calculate_score(4, 2, VOWEL)
    3
    """
    
    if letter_type == CONSONANT:
        return current_score + CONSONANT_POINTS * occurrence
    elif letter_type == VOWEL:
        return current_score - VOWEL_PRICE

    
def next_player(current_player: str, last_letter_occur: int) -> str:
    """Return the next player. If and only
    if the number of occurrences in the puzzle of the letter last chosen by 
    the current_player last_letter_occur is greater than zero, the 
    current_player plays again.
    
    Precondition: current_player == PLAYER_ONE or 
    current_player == PLAYER_TWO
    
    >>> next_player(PLAYER_ONE, 2)
    'Player One'
    >>> next_player(PLAYER_ONE, 0)
    'Player Two'
    """
    
    if last_letter_occur > 0:
        return current_player
    else:
        if current_player == PLAYER_ONE:
            return PLAYER_TWO
        else:
            return PLAYER_ONE
            