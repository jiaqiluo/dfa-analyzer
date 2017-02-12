# CS311 Program #1
# Jiaqi Luo

import json

DESCRIPTION = "description"
ALL_STATES = "all_states"
ALPHABET = "alphabet"
START_STATE = "start_state"
FINAL_STATE = "final_states"
TRANSITION_TABLE = "transition"
TEST = "test_strings"

class DFA_Analyzer:

    def __init__(self):
        self.description = None
        self.states = None
        self.alphabet = None
        self.start_state = None
        self.final_states = None
        self.transitions = None
        self.test_strings = None

    def read_dfa(self, file_name):
        try:
            f = open(file_name)
            source = json.load(f)
            self.description = source[DESCRIPTION]
            self.states = source[ALL_STATES]
            self.alphabet = source[ALPHABET]
            self.start_state = source[START_STATE]
            self.final_states = source[FINAL_STATE]
            self.transitions = source[TRANSITION_TABLE]
            self.test_strings = source[TEST]
            f.close()
            return("Open file successfully, start testing")
        except IOError:
            return("\n*** the file does not exist\n")

    def process_a_string(self, string):
        current_state = self.start_state
        print ("\n-------- Test --------\n-Description: " + self.description + "\n-Testing String: " + string)
        print("-Process:")
        for char in string:
            if char not in self.alphabet:
                return("*** Invalid Alphabet: " + char + " is not an element of the alphabet.")
            if current_state not in self.states:
                return ("*** Invalid state: " + current_state + " is not a state in the DFA.")
            new_state = self.transitions[current_state][char]
            print ("  transition( " + current_state + ", " + char + " ) --> " + new_state)
            current_state = new_state
        if current_state in self.final_states:
            return("-Result: Accepted\n")
        else:
            return("-Result: Recjected\n")

    def test_dfa(self, file_name):
       print(self.read_dfa(file_name))
       if(self.test_strings):
           for string in self.test_strings:
                print(self.process_a_string(string))

    def test_user_string(self):
        string = input("enter the string you want to test:")
        print(self.process_a_string(str(string)))

if __name__ == "__main__":
    sample = DFA_Analyzer()
    sample.test_dfa("test2.json")
    sample.test_user_string()
