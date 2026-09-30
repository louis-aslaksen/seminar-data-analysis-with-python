from bulls_and_cows import check_bulls_cows, check_input


#--------------Test: check_bulls_cows--------------

#Test 1, checks for 4 bulls
bulls, cows = check_bulls_cows(["1","2","3","4"],["1","2","3","4"])

assert bulls == 4
assert cows == 0

#Test 2, checks for 0 bulls and 0 cows
bulls, cows = check_bulls_cows(["1","2","3","4"],["5","6","7","8"])

assert bulls == 0
assert cows == 0

#Test 3, checks for 0 bulls and 1 cow
bulls, cows = check_bulls_cows(["1","2","3","4"],["4","5","6","7"])

assert bulls == 0
assert cows == 1

#Test 4, checks for 1 bulls, 1 cow and one same number but no cow becuase already used
bulls, cows = check_bulls_cows(["1","2","3","4"],["1","3","6","3"])

assert bulls == 1
assert cows == 1

#Test 6
bulls, cows = check_bulls_cows(["1","2","3","4"],["1","3","6","3"])

assert bulls == 1
assert cows == 1

#Test 6, checks for 1 bull against all digits same.
bulls, cows = check_bulls_cows(["1","2","3","4"],["1","1","1","1"])

assert bulls == 1
assert cows == 0

#--------------Test: check_input --------------

#Test 1, checks if correct input yiels True
assert check_input(["1","2","3","4"])

#Test 2, checks if non-integer input yiels False
assert not check_input(["1","a","3","4"])


#Test 3, checks if too long input yiels False
assert not check_input(["1","2","3","4","5"])

#Test 4, checks if too short input yiels False
assert not check_input(["1","2","3"])
