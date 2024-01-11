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
The code: 
takes takes a 27x1 vector which represents the word to be guessed and passes it through a word embedding to prokect it to a higher dimensional plane
takes the guessed alphabet 





