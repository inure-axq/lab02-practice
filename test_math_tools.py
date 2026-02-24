from math_tools import add, multiply, is_even, subtract, max_of_three, is_palindrome, find_min, remove_duplicates

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("test_add: ALL PASSED")

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0
    print("test_multiply: ALL PASSED")

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    print("test_is_even: ALL PASSED")

def test_subtract():
    assert subtract(5,2) == 3
    assert subtract(6,2) == 4
    assert subtract(4,3) == 1
    print("test_subtract: ALL PASSED")

def test_max_of_three():
    assert max_of_three(1,2,3) == 3
    assert max_of_three(-1,-3,-10) == -1
    assert max_of_three(5,9,11) == 11
    print("test_max_of_three: ALL PASSED")
    
def test_is_palindrome():
    assert is_palindrome("z") == True
    assert is_palindrome("") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("madam") == True
    assert is_palindrome("hi") == False
    assert is_palindrome("computer science") == False
    print("test_is_palindrome: ALL PASSED")
    
def test_find_min():
    assert find_min([5, 8, 12]) == 5
    assert find_min([3, -10, 49]) == -10
    assert find_min([-39, -20, -10]) == -39
    assert find_min([9, 24, 2]) == 2
    assert find_min([9]) == 9
    print("test_is_min: ALL PASSED")
    
def test_remove_duplicates():
    assert remove_duplicates([]) == []
    assert remove_duplicates([10, 20, 30]) == [10, 20, 30]
    assert remove_duplicates([1,"1"]) == [1, "1"]
    assert remove_duplicates([1, 2, 2, 5,3, 1, 1]) == [1, 2, 5, 3]
    assert remove_duplicates([1, "1", 2, "2", 1, "1"]) == [1, "1", 2, "2"]
    assert remove_duplicates(["x", "b", "x", "c", "b", "a"]) == ["x", "b", "c", "a"]
    print("test_remove_duplicates: ALL PASSED")
    
test_add()
test_multiply()
test_is_even()
test_subtract()
test_max_of_three()
test_is_palindrome()
test_find_min()
test_remove_duplicates()
print(" --- All tests passed ! ---")