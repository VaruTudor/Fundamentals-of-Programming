from nonUI3_4 import *

def test_remove():
    assert remove([1,2,3],2,[]) == ([1,2],[[1,2,3]])
    assert remove([1,2,3,5,7],2,[]) == ([1,2,5,7],[[1,2,3,5,7]])

def test_remove_from():
    assert remove_from([4,3,2,1,4,5,3,2],3,5,[]) == ([4,3,2,3,2],[[4,3,2,1,4,5,3,2]])

def test_add():
    assert add_number([4,3,2,1,4,5,3,2],3,[]) == ([4,3,2,1,4,5,3,2,3],[[4,3,2,1,4,5,3,2]])

def test_insert():
    assert insert_number([1,3,4,5],3,3,[]) == ([1,3,4,3,5],[[1,3,4,5]])

def test_check_word():
    assert check_word('abcde')==True
    assert check_word('abcde22')==False
    assert check_word('abcde>')==False

def test_check_sign():
    assert check_sign('>')==True

def test_convert_to_number():
    assert convert_to_number('3asd23') == [3,23]
    assert convert_to_number('3asd-23') == [3,-23]
    assert convert_to_number('3-5i') == [3,-5]
    assert convert_to_number('35k') == [35]
    assert convert_to_number('35') == 35
    assert convert_to_number('3-50i') == [3,-50]

def test_find():
    assert find([4,7,9,11,4,2],4) == [0,4]

def test_replace():
    assert replace([2,6,8,11,4,6],6,15,[]) == ([2,15,8,11,4,15],[[2,6,8,11,4,6]])

def test_modulo():
    assert modulo([3,4]) == 5

def test_filter_real():
    assert filter_real([[1,2],[2,4],[3,0],[5,1],[2,0],[3,1]],[])  == ([[3,0],[2,0]] , [[[1,2],[2,4],[3,0],[5,1],[2,0],[3,1]]])

def test_filter_modulo():
    assert filter_modulo([[1,2],[2,4],[3,0],[5,1],[2,0],[3,1]],3,">",[]) == ([[2,4],[5,1],[3,1]] , [[[1,2],[2,4],[3,0],[5,1],[2,0],[3,1]]])
    assert filter_modulo([[1,2],[2,4],[3,0],[5,1],[2,0],[3,1]],3,"=",[]) == ([[3,0]] , [[[1,2],[2,4],[3,0],[5,1],[2,0],[3,1]]])

def test_sum_from():
    assert sum_from([[5,3],[3,4],[2,0],[3,4],[5,0],[2,6],[1,15]],2,6) == (13,25)
    assert sum_from([[5,3],[3,4],[2,0],[3,4],[5,0],[2,6],[1,15]],1,5) == (15,14)

def test_product_from():
    assert product_from([[5,3],[3,4],[2,0],[3,4],[5,0],[2,6],[1,15]],2,4) == (30,40)
    assert product_from([[5,3],[3,4],[2,0],[3,4],[5,0],[2,6],[1,15]],0,1) == (3,29)

def test():
    test_remove()
    test_remove_from()
    test_add()
    test_insert()
    test_check_word()
    test_convert_to_number()
    test_find()
    test_replace()
    test_check_sign()
    test_filter_real()
    test_filter_modulo()
    test_sum_from()
    test_product_from()
    
test()