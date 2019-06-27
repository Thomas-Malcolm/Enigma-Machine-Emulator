"""Individual rotor logic and functionality (core rotors and Umkehrwalze)"""

ENIGMA_ROTORS = {}
LETTER_VALUES = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,
                 'X':23,'Y':24,'Z':25}

with open('rotors.txt') as file:
    for line in file:
        no_spaces = line.strip()
        rotor_name, __ , info = no_spaces.partition(':')
        letter_order_str, __ , turnover_pos = info.partition(",")

        letter_order_dict = []
        for letter in letter_order_str.strip():
            letter_order_dict.append(letter)

        ENIGMA_ROTORS[rotor_name.strip()] = (letter_order_dict, turnover_pos)


class Rotor():
    """Class for individual rotor functionality"""

    def __init__(self, rotor_name):
        """Constructor

        Parameter
            rotor_name (str): The name of the rotor
        """
        self._rotor_name = rotor_name
        try:
            self._letter_order = ENIGMA_ROTORS[rotor_name][0]

            self._inverse_order = {}

            for i, letter in enumerate(self._letter_order):
                self._inverse_order[letter] = ENIGMA_ROTORS['ETW'][0][i]
        except:
            raise ValueError("Rotor given not identified")

        self._turnover_key_unadjusted = ENIGMA_ROTORS[rotor_name][1].strip()
        if self._turnover_key_unadjusted != '':
            self._turnover_index = (LETTER_VALUES[self._turnover_key_unadjusted] + 1) % 25   # Added modulo 25
            self._turnover_key = ENIGMA_ROTORS['ETW'][0][self._turnover_index]

        self._rotation_count = 0

        self._viewable_letter = ENIGMA_ROTORS['ETW'][0][0]

    def current_viewable(self):
        """(str) Returns the current letter in the viewport"""
        return self._viewable_letter

    def get_rotor_name(self):
        """(str) Returns rotor's name"""
        return self._rotor_name

    def rotate_rotor_value(self):
        """Rotates rotor by one letter

        Return
            (bool): True iff complete cycle rotated, else False"""

        self._letter_order.append(self._letter_order.pop(0))

        self._rotation_count += 1

        self._rotation_count = self._rotation_count % 26

        self._viewable_letter = ENIGMA_ROTORS['ETW'][0][self._rotation_count]

        self.update_inverse_order()

    def does_next_rotate(self):
        """(bool) Returns true iff the rotor next to this one should rotate next iteration"""

        if self._viewable_letter == self._turnover_key:
            return True
        else:
            return False

    def encipher_letter(self, input, version=None):
        """(str) Returns the coded letter

        Parameters
            input (str): The letter to be enccodered
            version (int): 0 if letter passing through first time, 1 if letter passing second, 2 if reflector"""

        if version == 0:
            input_index_value = LETTER_VALUES[input.upper()]
            unadjusted_converted_letter = self._letter_order[input_index_value]
            converted_index_value = (LETTER_VALUES[unadjusted_converted_letter] - self._rotation_count) % 26
            converted_letter = ENIGMA_ROTORS['ETW'][0][converted_index_value]

        elif version == 1:
            input_index_value = (LETTER_VALUES[input.upper()] + self._rotation_count) % 26
            converted_index = ENIGMA_ROTORS['ETW'][0][input_index_value]
            converted_letter = self._inverse_order[converted_index]

        elif version == 2:
            input_index_value = LETTER_VALUES[input.upper()]
            converted_letter = self._letter_order[input_index_value]

        elif version == None:
            pass

        return converted_letter

    def reset_to_default(self):
        """Resets the rotor to the initial 'A' setting"""

        # At some point the ENIGMA_ROTORS constant is modified - reinstantiating is quick fix
        # Think it has something to do with python splicing/list mutability
        ENIGMA_ROTORS={}
        with open('rotors.txt') as file:
            for line in file:
                no_spaces = line.strip()
                rotor_name, __, info = no_spaces.partition(':')
                letter_order_str, __, turnover_pos = info.partition(",")

                letter_order_dict = []
                for letter in letter_order_str.strip():
                    letter_order_dict.append(letter)

                ENIGMA_ROTORS[rotor_name.strip()] = (letter_order_dict, turnover_pos)

        self._letter_order = ENIGMA_ROTORS[self._rotor_name][0]

        self._rotation_count = 0
        self._viewable_letter = ENIGMA_ROTORS['ETW'][0][self._rotation_count]

        self._inverse_order = {}

        for i, letter in enumerate(self._letter_order):
            self._inverse_order[letter] = ENIGMA_ROTORS['ETW'][0][i]

    def update_inverse_order(self):
        """Updates the inverse order"""
        self._inverse_order = {}

        for i, letter in enumerate(self._letter_order):
            self._inverse_order[letter] = ENIGMA_ROTORS['ETW'][0][i]

    def set_position(self, viewable_letter):
        """Sets the position of the rotor to a letter

        Parameter
            viewable_letter (str): The letter that will be viewable after being set"""
        self._letter_order = ENIGMA_ROTORS[self._rotor_name][0]

        self._viewable_letter = viewable_letter
        self._rotation_count = LETTER_VALUES[self._viewable_letter]

        i=0
        while i < self._rotation_count:
            self._letter_order.append(self._letter_order.pop(0))
            i+=1

        self.update_inverse_order()

class Reflector(Rotor):
    """Special type of rotor that does not move"""

    def rotate_rotor_value(self):
        """Reflector generally doesn't rotate"""

        raise NotImplementedError("Reflector doesn't rotate")

def main():
    s=[]
    for x in ENIGMA_ROTORS:
        s.append(x)
    print(s)

if __name__ == "__main__":
    main()





