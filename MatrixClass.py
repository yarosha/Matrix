class MyMatrix:
    def __init__(self, data: list):
        """
        Create matrix of given data.
        Example of data:
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
        ]
        Return TypeError if data is not list.
        """
        if isinstance(data, list) == False:
            raise TypeError
        elif isinstance(data, list) == True:
            self.matrix = copy.deepcopy(data)
            
            if len(self.matrix) != 0:
                for i in range(len(self.matrix)-1):
                    if len(self.matrix[i]) != len(self.matrix[i+1]):
                        raise TypeError('The length of strings is diffrent')
       

    def __repr__(self) -> str:
        """
        Return visual presentation of matrix.
        Example:
          1  20   3   4
          5   6 100   8
        Hint: use '\n' for line break
        """
        if len(self.matrix) == 0:
            self.a = ''
            return self.a
        else:
            yara = ''
            gap = ' '
            counter = 0
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    if len(str(self.matrix[i][j] )) > counter:
                        counter = len(str(self.matrix[i][j]))

            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    yara += ((counter - len(str(self.matrix[i][j])) + 1) * gap) + str(self.matrix[i][j])
                yara += '\n'
            return yara

    def size(self) -> tuple:
        """
        Return tuple(height, width) for matrix.
        Example: (2, 4)
        """
        if len(self.matrix) != 0:
            self.tuple1 = (len(self.matrix), len(self.matrix[0]))
        else:
            self.tuple1 = (0, 0)
        return(self.tuple1)

    def flip_up_down(self):
        """
        E.g. modify
        1, 2, 3, 4   to   5, 6, 7, 8
        5, 6, 7, 8        1, 2, 3, 4
        """
        if len(self.matrix) == 0:
            raise TypeError('matrix is empty')
        else:
            for i in range(len(self.matrix)//2):
                self.matrix[i], self.matrix[len(self.matrix) - i-1] = self.matrix[len(self.matrix) - i-1], self.matrix[i]
   
  

    def flip_left_right(self):
        """
        E.g. modify
        1, 2, 3, 4   to   4, 3, 2, 1
        5, 6, 7, 8        8, 7, 6, 5
        """
        if len(self.matrix) == 0:
            raise TypeError('matrix is empty')
        else:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0]) //2):
                    self.matrix[i][j], self.matrix[i][len(self.matrix[i])-j-1] = self.matrix[i][len(self.matrix[i])-j-1], self.matrix[i][j]

       
     

    # методы flip_ ИЗМЕНЯЮТ матрицу
    # методы flipped_ по сути делают то же самое,
    # но возвращают изменённую КОПИЮ матрицы
    def flipped_up_down(self):
        if len(self.matrix) != 0:
            a = MyMatrix(self.matrix)
            a.flip_up_down()
            return a

        else:
            raise TypeError('matrix is empty')
            
    def flipped_left_right(self):
        if len(self.matrix) != 0:
           a = MyMatrix(self.matrix)
           a.flip_left_right()
           return a
        else:
            raise TypeError('matrix is empty')

    def transpose(self):
        """
        E.g. modify
                          1, 5
        1, 2, 3, 4   to   2, 6
        5, 6, 7, 8        3, 7
                          4, 8
        """
        if len(self.matrix) != 0:
            v = [[0 for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix[0])):
                for j in range(len(self.matrix)):
                    v[i][j]=self.matrix[j][i]
            self.matrix = v
        else:
            raise  TypeError

    def transposed(self):
        """
        Return transposed copy of MyMatrix.
        """
        if len(self.matrix) != 0:
            a = MyMatrix(self.matrix)
            a.transpose()
            return a
        else:
            raise TypeError
         
    def get_data(self):
        return copy.deepcopy(self.matrix)
        
      
