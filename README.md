**Hangman_BiLSTM**

Player A guesses an n-letter word and tells player B about the number of alphabets the word has. PLayer B has to guess it in k guesses. 

Each time player B guesses a correct alphabet all the places where that alphabet occurs are revealed, else if the guess is wrong a life is subtracted.

example gameplay:

player A: 7 Leter word (word - running)

player B: guess: A  word: _ _ _ _ _ _ _  lives = 5

player B: guess: B  word: _ _ _ _ _ _ _  lives = 4

player B: guess: N  word: _ _ n n _ n _  lives = 4

player B: guess: R  word: r _ n n _ n _  lives = 4

Implementation:

two vectors state and guessed are initialised.

state vector --> embedding --> BiLSTM --> BiLSTM --> GlobalAveragePooling1D --> Dense Layer --> state_embedding

guessed vector --> embedding --> Dense Layer --> Dense Layer --> guessed_embedding

concat(state_embedding, guessed_embedding) --> Dense Layer --> Dense Layer --> next guess alphabet

