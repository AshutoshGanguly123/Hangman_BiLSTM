# from collections import Counter
# import ast
# import matplotlib.pyplot as plt
# import numpy as np

# # Initialize counters
# length_correct_counter = Counter()
# length_incorrect_counter = Counter()

# # Load data from the file
# with open('/Users/ashutoshganguly/Desktop/personal/ml_work/hangman/hangman_try5/HangmanKeras/words_guessed_3_to_10.txt', 'r') as f:
#     lines = f.readlines()

# # Parse and accumulate data
# for line in lines:
#     entry, correct = line.split(", ")
#     entry = ast.literal_eval(entry)
#     word = entry['ans']
#     word_length = len(word)
#     correct = int(correct)
#     counter = length_correct_counter if correct else length_incorrect_counter
#     counter[word_length] += 1

# # Prepare data for plotting
# lengths_correct = sorted(length_correct_counter.keys())
# freq_correct_length = [length_correct_counter[length] for length in lengths_correct]

# lengths_incorrect = sorted(length_incorrect_counter.keys())
# freq_incorrect_length = [length_incorrect_counter[length] for length in lengths_incorrect]

# # Plot
# plt.figure(figsize=(12, 6))

# # Separate positions for correct and incorrect to avoid overlap
# x_correct = np.array(lengths_correct) - 0.2
# x_incorrect = np.array(lengths_incorrect) + 0.2

# plt.bar(x_correct, freq_correct_length, width=0.4, alpha=0.6, label='Correct Guesses', color='b')
# plt.bar(x_incorrect, freq_incorrect_length, width=0.4, alpha=0.6, label='Incorrect Guesses', color='r')

# plt.xlabel('Word Length')
# plt.ylabel('Frequency')
# plt.title('Word Length vs Bot Guesses')
# plt.legend()
# plt.xticks(np.union1d(x_correct, x_incorrect).astype(int))
# plt.show()



from collections import Counter
import ast
import matplotlib.pyplot as plt
import numpy as np

# Initialize counters
length_correct_counter = Counter()
length_incorrect_counter = Counter()

# Load data from the file
with open('/Users/ashutoshganguly/Desktop/personal/ml_work/hangman/hangman_try5/HangmanKeras/words_guessed_policies_26.txt', 'r') as f:
    lines = f.readlines()

# Parse and accumulate data
for line in lines:
    entry, correct = line.split(", ")
    entry = ast.literal_eval(entry)
    word = entry['ans']
    word_length = len(word)
    correct = int(correct)
    counter = length_correct_counter if correct else length_incorrect_counter
    counter[word_length] += 1

# Prepare data for plotting
lengths = sorted(set(length_correct_counter.keys()).union(set(length_incorrect_counter.keys())))
freq_correct_length = [length_correct_counter.get(length, 0) for length in lengths]
freq_incorrect_length = [length_incorrect_counter.get(length, 0) for length in lengths]
ratios = [c / (c + i) if c + i > 0 else 0 for c, i in zip(freq_correct_length, freq_incorrect_length)]

# Plot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Bar plots for frequencies
ax1.bar(np.array(lengths) - 0.2, freq_correct_length, width=0.4, alpha=0.6, label='Correct Guesses', color='b')
ax1.bar(np.array(lengths) + 0.2, freq_incorrect_length, width=0.4, alpha=0.6, label='Incorrect Guesses', color='r')

# Make the y-axis label and tick labels match the line color.
ax1.set_xlabel('Word Length')
ax1.set_ylabel('Frequency', color='black')
for tl in ax1.get_yticklabels():
    tl.set_color('black')

# Twin axes for ratios
ax2 = ax1.twinx()
ax2.plot(lengths, ratios, 'g-', label='Correct/Total Ratio')
ax2.set_ylabel('Ratio', color='green')
for tl in ax2.get_yticklabels():
    tl.set_color('green')

# Legends and grid
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.grid(True)

plt.title('Word Length vs Bot Guesses and Correct/Total Ratio')
plt.show()

