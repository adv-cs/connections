import random


def check_guess_correctness(guesses: list, board: dict) -> tuple:
    '''
    Checks if the guesses match a category in the board.

    Args:
        guesses: A list of words guessed by the player
        board: A dictionary mapping categories to lists of words

    Returns:
        A tuple containing:
        - A boolean indicating whether the guesses was correct (True) or incorrect (False)
        - The category name if all guesses are correct, "One Away" if one guess is incorrect,
        or None if no guesses are correct.
    '''
    pass


def validate_guess(guesses: list, board: dict) -> bool:
    '''
    Checks that the user has guessed 4 valid words from the board, with no duplicates.

    Args:
        guesses: A list of words guessed by the player
        board: A dictionary mapping categories to lists of words
    
    Returns:
        True if the guesses are valid, False otherwise.

    '''
    pass


def read_line(line: str) -> list:
    '''
    Reads and cleans a comma-separated line with a category name and its words/phrases

    Args:
        line: A string containing a category name and its words/phrases, separated by commas

    Returns:
        A list of cleaned values, with whitespace removed and all letters capitalized

    Example:
        >>> read_line("Fruits, apple, banana, cherry, orange")
        ['FRUITS', 'APPLE', 'BANANA', 'CHERRY', 'ORANGE']
        
    '''
    pass


def load_board(name: str) -> dict:
    '''
    Loads a Connections board from a comma-separated values file in the games/
    directory.

    The first value in each line must be the category name, and the
    subsequent values the words/phrases in that category.

    Args:
        name: The name of the game to load, corresponding to a file
        in the games/ directory.

    Returns:
        A dictionary mapping category names to lists of words/phrases in that
        category
    '''
    pass


def display_board(board: dict) -> None:
    '''
    Prints the board in random order, with four words per line separated by spaces.

    Args:
        board: A dictionary mapping categories to lists of words

    Returns:
        None

    Example:
        >>> display_board({
        ...     "FRUITS": ["APPLE", "BANANA", "CHERRY", "ORANGE"],
        ...     "ANIMALS": ["DOG", "CAT", "ELEPHANT", "LION"]
        ... })
        
      ELEPHANT                 ORANGE                   DOG                    BANANA       

       CHERRY                   LION                   APPLE                    CAT         
    '''
    pass


if __name__ == "__main__":
    '''
    Asks the user which game they want to play, then loads the board and
    allows the user to play Connections through standard input/output.

    The words remaining on the board should be displayed before each guess, and feedback
    should be given after.

    The game should end when the user has guessed all categories correctly or makes 4 mistakes, and
    final feedback should be given to the user.
    '''
    pass
