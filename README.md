**Hangman_BiLSTM**
Overview
Hangman_BiLSTM is an advanced implementation of the classic word-guessing game, Hangman, utilizing a Bidirectional Long Short-Term Memory (BiLSTM) model. In this game, one player thinks of a word, and the other player has a limited number of attempts (lives) to guess the word by suggesting letters.

Gameplay
The gameplay of Hangman_BiLSTM follows the traditional Hangman rules with a slight twist. The player is given a fixed number of lives (default n=6) to guess a hidden word by suggesting letters. For each incorrect guess, a life is lost. The game ends when the player either guesses the word correctly or runs out of lives.

Example Gameplay
The hidden word is chosen, and its length is revealed to the player.
The player guesses a letter.
If the letter is in the word, it is revealed in its correct position(s).
If the letter is not in the word, the player loses a life.
Steps 2-4 are repeated until the player either guesses the word correctly or loses all lives.

