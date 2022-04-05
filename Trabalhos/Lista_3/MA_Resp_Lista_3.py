"""
Aluno: Marcos André de Moraes Galdino
Matrícula: 201810068311

"""

#Exercicio 3.2
    def penultimate(self):
        u = self.head
        while u.next is not None:
            penultimate = u.x
            u = u.next
        return penultimate

#Exercicio 3.4
    def reverse(self):
        i = 0
        lenght = self.size() - 1
        while i < (self.size() / 2):
            a = self.get(i)
            b = self.get(lenght - i)
            self.set(i, b)
            self.set(lenght - i, a)
            i += 1

        return 'Reversed'

#Exercicio 3.7
    def eh_palindromo(self):
        i = 0
        lenght = self.size() - 1
        a = True
        while i < (self.size() / 2):
            a = self.get(i)
            b = self.get(lenght - i)
            if a != b:
                i = self.size()
                a = False
            i += 1
        if a:
            return "É Palindromo"
        else:
            return "Não É Palindromo"
#Exercicio 3.8
    def rotate(self, r):
        mod = self.size()
        j = r % mod
        a = self.get(j)
        self.set(j, self.get(0))
        i = 1
        while i < self.size():
            b = a
            j = (j + r) % mod
            a = self.get(j)
            self.set(j, b)
            i += 1