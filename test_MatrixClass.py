from MatrixClass import MyMatrix
def test_repr(): 
    a = MyMatrix([[1, 2, 5], [3, 4, 6]])
    assert a.__repr__() ==' 1 2 5\n 3 4 6\n'

def test_size():
    a = MyMatrix([[1, 2, 5], [3, 4, 6]])
    assert a.size() == (2, 3)
    a = MyMatrix([[], []])
    assert a.size() == (2, 0)
    a = MyMatrix([])
    assert a.size() == (0, 0)

def test_flip_left_right():
    a = MyMatrix([[1, 2, 5], [3, 4, 6]])
    a.flip_left_right()
    assert (a.matrix == [[5, 2, 1], [6, 4, 3]]) 
  
def test_flip_up_down():
    a = MyMatrix([[1, 2, 5], [3, 4, 6]])
    a.flip_up_down()
    assert a.matrix == [[3, 4, 6], [1, 2, 5]]

def test_flipped_left_right():
    a=MyMatrix([[1,3,4],[5,7,2]])
    assert(a.flipped_left_right().get_data() == [[4,3,1],[2,7,5]])
    assert(a.get_data() == [[1,3,4],[5,7,2]])
    
def test_flipped_up_down():
    a=MyMatrix([[1,3,4],[5,7,2]])
    assert(a.flipped_up_down().get_data() == [[5,7,2],[1,3,4]])
    assert(a.get_data() == [[1,3,4],[5,7,2]])
    
def test_transpose():
    a = MyMatrix([[1, 2, 5], [3, 4, 6]])
    a.transpose()
    assert (a.matrix == [[1, 3], [2, 4], [5, 6]]) 

def test_transposed():
    a=MyMatrix([[1,3,4],[5,7,2]])
    assert(a.transposed().get_data() == [[1,5],[3,7],[4,2]])
    assert(a.get_data() == [[1,3,4],[5,7,2]])
    a=MyMatrix([[1,3],[5,7],[9,0]])
    assert(a.transposed().get_data() == [[1, 5, 9],[3, 7, 0]]) 
    assert(a.get_data() == [[1,3],[5,7],[9,0]])
    ### ссылка на колаб на всякий случай:https://colab.research.google.com/drive/1oybdehXVVnK4PWNWMhzPQiy9Qaipoq9y#scrollTo=E5gQw82B-UNR###
