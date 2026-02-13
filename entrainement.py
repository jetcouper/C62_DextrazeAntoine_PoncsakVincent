#Quant tu lis le texte et créer les deux structures
import numpy as np

class entrainement:
    def __init__(self,texte):
        #word_list = ["apple", "banana", "cherry", "date"]
        #num_columns = 10 # Example: specify the desired number of columns

        # Define the shape of the 2D array using the length of the word list
        # Shape format is (rows, columns)
        self.array_shape = (len(texte), len(texte))

        # Create the 2D array of zeros with integer data type
        zero_matrix = np.zeros(self.array_shape, dtype=int)

        print(zero_matrix)