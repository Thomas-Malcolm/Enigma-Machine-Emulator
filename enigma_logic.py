"""Enigma Machine logic (machine object)

To be implemented:
    - Compatibility for 4/5 rotors
    - Switching rotors around

To be checked:
    - plugboard functionality
"""

from rotor_class import Rotor, Reflector

class EnigmaMachine():
    """Enigma machine template"""

    def __init__(self, rotor1, rotor2, rotor3, reflector, rotor4 = None, rotor5 = None):
        """Constructor

        Parameters
            rotor1 (str): Identifying name of left most rotor
            rotor2 (str): Identifying name of middle rotor
            rotor3 (str): Identifying name of right rotor
            reflector (str): Identifying name of the reflector
            rotor4 (str): Identifying name of the 4th rotor, if in use
            rotor5 (str): Identifying name of the 5th rotor, if in use
        """

        self._rotor_l = Rotor(rotor1)
        self._rotor_m = Rotor(rotor2)
        self._rotor_r = Rotor(rotor3)

        if rotor4 != None:
            self._rotor_4 = Rotor(rotor4)
        if rotor5 != None:
            self._rotor_5 = Rotor(rotor5)

        self._reflector = Reflector(reflector)

        self._plugboard = {}
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self._plugboard[letter] = letter

    def get_reflector(self):
        """(str) The name of the reflector"""
        return self._reflector.get_rotor_name()

    def get_left_rotor(self):
        """(str) The name of the left rotor"""
        return self._rotor_l.get_rotor_name()

    def get_middle_rotor(self):
        """(str) The name of the middle rotor"""
        return self._rotor_m.get_rotor_name()

    def get_right_rotor(self):
        """(str) The name of the right rotor"""
        return self._rotor_r.get_rotor_name()

    def get_left_rotor_pos(self):
        """(str) Returns currently viewable letter/setting for left rotor"""
        return self._rotor_l.current_viewable()

    def get_middle_rotor_pos(self):
        """(str) Returns currently viewable letter/setting for middle rotor"""
        return self._rotor_m.current_viewable()

    def get_right_rotor_pos(self):
        """(str) Returns currently viewable letter/setting for right rotor"""
        return self._rotor_r.current_viewable()

    def set_plugboard_pair(self, letter1, letter2):
        """Set two letters to be plugboard pairs

        Parameters
            letter1 (str): The first letter of the new pair
            letter2 (str): The second letter of the new pair
        """

        if letter1 != self._plugboard[letter1]:
            self.reset_pair(self._plugboard[letter1])
        if letter2 != self._plugboard[letter2]:
            self.reset_pair(self._plugboard[letter2])


        self._plugboard[letter1] = letter2
        self._plugboard[letter2] = letter1

    def reset_pair(self, letter):
        """Resets letter pairs based on single letter input"""
        current_pairing = self._plugboard[letter]
        self._plugboard[letter] = letter
        self._plugboard[current_pairing] = current_pairing

    def full_encode(self, input):
        """Encodes/Decodes a letter through the entire process

        Parameters
            input (str): The user's letter input

        Returns
            str: The encoded/decoded letter [stage_9]

        Stages:
            stage_1: The initial pass through the Stecker/Plugboard
            stage_2: Rotate the rotors by relative amounts & first pass through rotor3 (rotor_r)
            stage_3: First pass through rotor2 (rotor_m)
            stage_4: First pass through rotor1 (rotor_l)
            stage_5: The reflector
            stage_6: Second pass through rotor1 (rotor_l)
            stage_7: Second pass through rotor2 (rotor_m)
            stage_8: Second pass through rotor3 (rotor_r)
            stage_9: Final pass through the Stecker/Plugboard
        """

        # Stage 1
        stage_1 = self._plugboard[input]

        # Stage 2
        self._rotor_r.rotate_rotor_value()

        if self._rotor_r.does_next_rotate():
            self._rotor_m.rotate_rotor_value()

            if self._rotor_m.does_next_rotate():
                self._rotor_l.rotate_rotor_value()

        stage_2 = self._rotor_r.encipher_letter(stage_1, 0)

        # Stage 3
        stage_3 = self._rotor_m.encipher_letter(stage_2, 0)

        # Stage 4
        stage_4 = self._rotor_l.encipher_letter(stage_3, 0)

        # Stage 5
        stage_5 = self._reflector.encipher_letter(stage_4, 2)

        # Stage 6
        stage_6 = self._rotor_l.encipher_letter(stage_5, 1)

        # Stage 7
        stage_7 = self._rotor_m.encipher_letter(stage_6, 1)

        # Stage 8
        stage_8 = self._rotor_r.encipher_letter(stage_7, 1)

        # Stage 9
        stage_9 = self._plugboard[stage_8]

        return stage_9

    def rotate_n_times(self, n):
        """Rotate rotor_r n times"""
        i = 0

        while i < n:
            self._rotor_r.rotate_rotor_value()

            if self._rotor_r.does_next_rotate():
                self._rotor_m.rotate_rotor_value()

                if self._rotor_m.does_next_rotate():
                    self._rotor_l.rotate_rotor_value()
            i += 1

    def set_left_rotor_pos(self, position):
        """Sets left rotor position to input"""
        print(type(self._rotor_l))
        if type(position) == str:
            self._rotor_l.set_position(position)
        else:
            raise ValueError("Position argument must be a letter (str)")
    def set_middle_rotor_pos(self, position):
        """Sets middle rotor position to input"""
        if type(position) == str:
            self._rotor_m.set_position(position)
        else:
            raise ValueError("Position argument must be a letter (str)")

    def set_right_rotor_pos(self, position):
        """Sets right rotor position to input"""
        if type(position) == str:
            self._rotor_r.set_position(position)
        else:
            raise ValueError("Position argument must be a letter (str)")


    def set_rotor_positions(self, left_rotor_pos='A', middle_rotor_pos='A',
                            right_rotor_pos='A'):
        """Sets the position of each rotor at the same time

        Parameters
            left_rotor_pos (str): The position the left rotor will be set to (Default = 'A')
            middle_rotor_pos (str): The position the middle rotor will be set to (Default = 'A')
            right_rotor_pos (str): The position the right rotor will be set to (Default = 'A')

        Condition
            All inputs must be a single letter from English alphabet
        """
        if type(left_rotor_pos) == str:
            self._rotor_l.set_position(left_rotor_pos)
        else:
            raise ValueError("Position argument must be a letter (str)")

        if type(middle_rotor_pos) == str:
            self._rotor_m.set_position(middle_rotor_pos)
        else:
            raise ValueError("Position argument must be a letter (str)")

        if type(right_rotor_pos) == str:
            self._rotor_r.set_position(right_rotor_pos)
        else:
            raise ValueError("Position argument must be a letter (str)")

    def set_left_rotor(self, rotor_name):
        """Changes left rotor"""
        self._rotor_l = Rotor(rotor_name)

    def set_middle_rotor(self, rotor_name):
        """Changes middle rotor"""
        self._rotor_m = Rotor(rotor_name)

    def set_right_rotor(self, rotor_name):
        """Changes right rotor"""
        self._rotor_r = Rotor(rotor_name)

    def set_reflector(self, reflector_name):
        """Changes reflector rotor"""
        self._reflector = Reflector(reflector_name)

    def reset_rotors(self):
        """Resets all rotors to default values"""

        self._rotor_l.reset_to_default()
        self._rotor_m.reset_to_default()
        self._rotor_r.reset_to_default()

        self._reflector.reset_to_default()


def main():
    """Used for testing the machine's functionality
        - Only run from this file""" 
    x = EnigmaMachine('I', 'II', 'III', 'UKW-B')

    print(x.full_encode('H'))
    print(x.full_encode('U'))
    print(x.full_encode('B'))
    print(x.full_encode('N'))
    print(x.full_encode('E'))
    print(x.full_encode('Q'))

if __name__ == "__main__":
    main()
