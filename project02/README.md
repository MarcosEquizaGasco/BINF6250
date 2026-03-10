# Introduction
This project is intended to read in a text file and use the contents to train a Markov model. It then can produce new text content based on the generated Markov model.

All functions written are found in `full_workflow_notebook.ipynb` along with reproducible implementations for demonstration.

The example scripts `generate_sonnet.py`, `generate_odyssey_fragment.py` and `generate_onefishtwofish.py` have built-in random number generation through `random.random()` and can quickly produce some example nonsense.

This project was done as an assignment for the course BINF6250 at Northeastern University.

# Pseudocode
----- 
```
--- Intended flow ---
1. Initialize constants for special tokens: ie. START="*S*", END="*E*", NL="*NL*".

2. Initialize an empty dictionary to store the Markov model counts, where:
	- keys are tuples of tokens (states)
	- values are dictionaries mapping next_token to integer count

3. Open and read "sonnets.txt".  
	If this fails, exit and raise an error.
	Convert the full text to lowercase -> "new_text".

4. Process "new_text" into a list of tokens -> [text_list] :
	If separator is unspecified, treat the entire text as one chunk.
		Otherwise, split the text by separator and store the results as chunks.
	
	Initialize [text_list] as a list containing a single `START` token.
	
	For each chunk:
		- Strip leading and trailing whitespace from chunk.  
		- Replace every single newline "\n" inside the chunk with NL (surrounded by spaces) so the newline becomes its own word.
		- Split the chunk on whitespace and append the resulting tokens to [text_list].  
	If this chunk is not the last chunk:
		- Append END and then START to [text_list]
	
	After all chunks are processed, append a final END token to [text_list].
	(This method keeps punctuation attached to words)

5. Build count model:
   Create an [expanded] text list:
	   For each token in [text_list]: 
	   If the token is START, append START (Markov order) times to [expanded].  
	   Otherwise, append the token once to [expanded].
    
    For each viable state - next word pair, update the nested dictionaries:
	    If the state is not a key in the outer dictionary, create it with a value of {}.
	    If next word is not in the inner dict for that state, initialize its count to 0.
	    Increment the transition count.

6. Generate a new token sequence based on learned transition probabilities:
	Initialize a reproducible random number generator.
	Initialize generated list as a list containing START repeated (order) times.
	Initialize counters for stopping conditions.
	
	Loop until a stopping condition is met or a hard token cap is reached:
		-Define current state as the last (order) words of the generated list.
		-Look up current_state in model-defining dictionary.
		-Sample one token according to the stored probabilities.
		-Append next token to generated list.
	
7. Convert the generated tokens back into readable text
	If the token is START, skip it.
	If the token is NL or END, append a newline character "\n" (optionally collapsing consecutive newlines) 
		and note that you are at the start of a line
	Otherwise:
		If you are not at the start of a line, append a space
		Append a token
		Mark that you are no longer at the start of a line
	Return text
	
____________________

--- Draft Pseudocode from pre-planning meetings -----

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

```

# Successes
Description of the team's learning points

We met and worked together to develop our algorithm. We had extremely productive discussions where we discussed multiple methods for solving each problem, trying to use forward thinking to make sure our methods would be compatible with higher order models and different types of input and output such as the format of sonnets. 

# Struggles
Description of the stumbling blocks the team experienced

Our group leader, Marcos, had a medical emergency during the weekend, when we had planned to meet to write the code for the project. Since he wasn't available, the other team members, Victoria and Linh, took ownership over that part. It helped that the team had met previously to map out the conceptual plan for the project, letting Marcos have a clear understanding of the project. After he came back, Victoria and Linh walked him through the codebase, explaining the implementation and describing some bits of syntax, which was very helpful. While this was a drawback for the project, it was fortunate that we had planned on meeting early on to discuss the conceptual plan and pseudocode to tackle this project.

# Personal Reflections
## Marcos Equiza Gasco
As mentioned above, I had a medical emergency and was out for the weekend and early in the week. Due to this, the other team members were very understanding and stepped up by taking responsibility over the code implementation. I am happy that we were able to meet before this happened, as that allowed me to still be part of the planning and conceptualization. We discussed the overall algorithm and separate helper functions that would be useful to implement it. Having this understanding allowed me to get up to speed after I came back from the hospital fairly easily. I think we worked well as a team, with everyone contributing to the execution of the plan. 

## Victoria Van Berlo
Designing the algorithm was the hardest part for me. Once we had the workings hashed out, most of the code was relatively straightforward to implement. Dictionaries prove a little tricky to use and get the correct syntax since they are made up of multiple data types put together. 

## Ngoc Linh Nguyen
This project emphasized the point that planning out the logic of the algorithm (eg. by drafting pseudocode) is the most important step. Once we had outlined what we wanted the code to do in a meeting and helped each other come to a better understanding of the algorithm, what was left was just syntax. Even if unexpected issues with how we set out to implement a step are discovered, having a clear idea of the purpose of that step makes it fairly simple to debug or even modify. I think playing around with the parameters helped me form some intuition about Markov order, and I also ended up learning a bit about random number generators.

# Generative AI Appendix
Generative AI was not used for this assignment.
