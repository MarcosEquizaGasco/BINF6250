# Introduction
This project is intended to read in a text file and use the contents to train a Markov model. It then can produce new text content based on the generated Markov model.

# Pseudocode
----- 

build_markov_model(markov_model, new_text): 

Use helper function to convert new_text to lower case and make a list text_list (accounting for start and end states. E.g.: 
    New_text = 'one two’ 
    2. Text_list = [*S*’, ‘one’, ‘two’, *E*]
While len(text_list) > 1: 
    For each current_word, next_word, in text_list[0:1]: 
    Check markov_model[current_word] exists 
        If not, markov_model[current_word] = {} 
	Check markov_model[current_word][next_word] exists 
    	If not, markov_model[current_word][next_word] = 0 
	Update markov_model[current][next_word] += 1 
	Delete text_list[0] 
Return markov_model 

-------- 

tokenize(new_text): 

Convert new_text to lower case and make a list text_list (accounting for start and end states. E.g.: 
    New_text = 'one two’ 
    Text_list = [*S*’, ‘one’, ‘two’, *E*] 
New_text.lower().split(‘ ‘) 
Add ‘*S*’ to start of list, ‘*E*’ to the end of list 

----- 

def get_next_word(current_word, markov_model_normalized, seed=42): 

''' 
Function to randomly move a valid next state given a markov model and a current state (word) 
Args: current_word (tuple): a word that exists in our model 
markov_model_normalized (dict of dicts): a dictionary of word (next_word:probability) 
Returns: next_word (str): a randomly selected next word based on transition probabilies 

Pseudocode: 

Access markov_model_normalized[current_word] 
	Get all keys, get all values 
Use np.random.choice(keys, 1, values) to get new_word 
Return new_word 

----- 

def generate_random_text(markov_model, seed=42, order=1): 

''' 
Function to generate text given a markov model 
Args: markov_model (dict of dicts): a dictionary of word:(next_word:frequency pairs) 
Returns: sentence (str): a randomly generated sequence given the model 

Pseudocode: 

Call helper function to create new dictionary with normalized probabilities 
Initialize generate_list with [‘*S*’] (add k *S* from k-th order
While '*E*’ is not in generate_list: 
	Take last word (or k-words) to generate new word 
	append get_next_word(tuple(generate_list[-order:]), markov_model_normalized) 
Convert generate_list to text as sentence 
Return sentence 

# Successes
Description of the team's learning points

We met and worked together to develop our algorithm. We had extremely productive discussions where we discussed multiple methods for solving each problem, trying to use forward thinking to make sure our methods would be compatible with higher order models and different types of input and output such as the format of sonnets. 

# Struggles
Description of the stumbling blocks the team experienced

# Personal Reflections
## Marcos Equiza Gasco
Group leader's reflection on the project

## Victoria Van Berlo
Designing the algorithm was the hardest part for me. Once we had the workings hashed out, most of the code was relatively straightforward to implement. Dictionaries prove a little tricky to use and get the correct syntax since they are made up of multiple data types put together. 

## Ngoc Linh Nguyen
Other members' reflections on the project

# Generative AI Appendix
Generative AI was not used for this assignment.
