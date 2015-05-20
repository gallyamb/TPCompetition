class Brainfuck(object):
    def __init__(self, code=None):
        self.translator = {
            '>': self.to_right,
            '<': self.to_left,
            '|': self.reset_pointer,

            ',': self.read_to_cell,
            '.': self.print_cell,
            '=': self.assign_prev,
            '0': self.reset_cell,
            '!': self.copy_to_variable,
            '?': self.copy_from_variable,
            '*': self.multiply,
            '/': self.divide,
            '+': self.increment,
            '-': self.decrement,

            '^': self.print_variable,
            '$': self.assign_index
        }

        self.brackets = {
            '[': ']',
            '(': ')'
        }

        self.special_translator = {
            ']': self.while_cycle,
            ')': self.if_statement
        }

        self.variable = -1
        self.pointer = 0
        self.memory = [0 for i in range(30000)]

        if code is not None:
            self.execute(code)

    def to_right(self):
        self.pointer = (self.pointer + 1) % 30000

    def to_left(self):          
        self.pointer = (self.pointer + 29999) % 30000

    def reset_pointer(self):
        self.pointer = 0

    def read_to_cell(self):         
        self.memory[self.pointer] = int(input()) % 256

    def print_cell(self):           
        print(self.memory[self.pointer])

    def assign_prev(self):
        self.to_left()
        item = self.memory[self.pointer]
        self.to_right()
        self.memory[self.pointer] = item

    def reset_cell(self):           
        self.memory[self.pointer] = 0

    def copy_to_variable(self):         
        self.variable = self.memory[self.pointer]

    def copy_from_variable(self):    
        self.memory[self.pointer] = self.variable % 256

    def multiply(self):         
        self.to_left()
        item = self.memory[self.pointer]
        self.to_right()
        self.memory[self.pointer] = (self.memory[self.pointer] * item) % 256

    def divide(self):
        self.to_left()
        item = self.memory[self.pointer]
        self.to_right()
        self.memory[self.pointer] = int(self.memory[self.pointer] / item)

    def increment(self):
        self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256

    def decrement(self):
        self.memory[self.pointer] = (self.memory[self.pointer] + 255) % 256

    def print_variable(self):    
        print(self.variable)

    def assign_index(self):    
        self.variable = self.pointer

    def while_cycle(self, code):            
        while self.memory[self.pointer]:
            self.execute(code)

    def if_statement(self, code):           
        if self.memory[self.pointer]:
            self.execute(code)

    def execute(self, code):
        index_diff = 0
        for i in range(len(code)):
            index = i + index_diff
            if index >= len(code):
                break
            command = code[index]
            if command not in self.translator:
                extracted_code, new_index_diff = self.extract_code(code[index:])
                index_diff += new_index_diff
                index = i + index_diff
                self.special_translator[code[index]](extracted_code)
            else:
                self.translator[command]()

    def extract_code(self, code):
        bracket = code[0]
        result = ''
        count = 1
        index = 1
        while count:
            if code[index] == self.brackets[bracket]:
                count -= 1
            if code[index] == bracket:
                count += 1
            result += code[index]
            index += 1
        return result[:-1], index - 1

code = input()
bf = Brainfuck()
bf.execute(code)