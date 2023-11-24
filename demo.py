from env import Hangman
from network import NNAgent, Network

policy_network = Network()
policy_network.load_weights('policy.h5') #input p
player = NNAgent(policy_network)
player.eval() #setting to evaluation state so the agent will not memorize play history.

player.reset_guessed()

import random
max_lives = 6
score = 0
with open("/Users/ashutoshganguly/Desktop/personal/ml_work/hangman/hangman_try5/test_words.txt", "r") as f:
    testing_word_list = [line.strip() for line in f.readlines()]

random.shuffle(training_word_list)
testing_word_list = testing_word_list[:1000] if len(testing_word_list) > 1000 else testing_word_list
print(len(training_word_list))

for word in training_word_list:
    env = Hangman([word] , max_lives = 6, verbose = True)
    done = False
    state = env.reset()
    final_score = 0
    while not done :
        guess = player.select_action(state)
        print('Guessing', guess)
        state, _ , done , _= env.step(guess)
    if state == word:
        score += 1
    player.reset_guessed()

print(score/len(training_word_list))






