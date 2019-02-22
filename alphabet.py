import os

class Alphabet:
    alpha = ['a','b','c','d','e','f','g','h','i','j','k',
            'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    def latin(self):
        return self.alpha

    def __len__(self):
        return len(self.alpha)

    def write_to_file(self, name):

        file = open(name,'w')
        file.write(self.latin)
        file.close()
        '''
        with open(name, 'w') as file:
            file.write(self.latin)
        '''
        return

    def read_from_file(self,name):

        file = open(name,'r')
        for line in file:
            print(line)
        file.close()
        '''
        with open(name, 'r') as file:
            file.write(self.latin)
            for line in file:
                print(line)
        '''

        return


if __name__ == "__main__":
    latin = Alphabet().latin()

    # for letter in latin:
    #     print(letter)
    #
    # i=0
    # while i < len(latin):
    #     print(latin[i])
    #     i+=1
    print(len(latin))
