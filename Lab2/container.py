import os.path
import re
import json


class ContainerUE:
    def __init__(self):
        self.container = set()

    # adding element(s).
    def add(self, elements):
        for element in elements:
            if element in self.container:
                print('Element {} is already in ur container!'.format(element))
            else:
                self.container.add(element)
                print('Element {} was successfully added to ur container'.format(element))

    # removing element(s).
    def remove(self, elements):
        for element in elements:
            self.container.discard(element)
            print('Element {} is no longer in ur container'.format(element))

    # find element(s).
    def find(self, elements):
        found = 0
        for element in elements:
            if element in self.container:
                print('Element {} found in ur container'.format(element))
                found += 1
        if found == 0:
            print('No such elements')

    # elements output.
    def list(self):
        for index, element in enumerate(self.container):
            print('{0}:\t{1}'.format(index, element))

    # searching elements according to a regex.
    def grep(self, pattern):
        found = 0
        for element in self.container:
            if re.match(pattern, str(element)):
                print("Found match with {} element".format(element))
                found += 1
        if found == 0:
            print('No such elements')

    # saving jsong-string to .txt file converting set to a list beforehand.
    def save(self, filename):
        with open(filename, 'w') as file:
            file.write(json.dumps(list(self.container)))
        print('The container was successfully saved to {}'.format(filename))

    # loading set from file.
    def load(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                self.container.update(set(json.load(file)))
        else:
            print('file {} does not exist!'.format(filename))

    # clearing set. Why not?
    def clear(self):
        self.container.clear()

