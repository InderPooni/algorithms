def isUnique(s):
	s = s.strip()
	if len(s) == 0 or len(s) == 1:
		return True
	x = ''

	for c in s:
		if c in x:
			return False
		x += str(c)
	
	return True

def check_permutation(str1, str2):
	if len(str1) != len(str2):
		return False


	str1 = sorted(str1) # O(nlogn)
	str2 = sorted(str2)

	idx = 0

	while idx < len(str1):
		if str1[idx] != str2[idx]:
			return False
		
		idx += 1
	
	return True

#1.3 replace all spaces in a string with %20
def urlify(s):
	token = '%20'
	s = s.rstrip()
	s = s.lstrip()

	arr = s.split(' ')

	return token.join(arr)

# 1.4 check if a string is a permutation of a palidrome
def palindrome_permutation(s):
	# approach to be a palindrome: if len is even -> all characters need to have even count
	# if len is odd -> there can only be one character with odd len

	#replace all spaces and convert to lower case
	s = s.replace(' ' , '')
	s = s.lower()

	#set up dictionary with frequences
	st = set()

	for c in s:
		if c in st:
			st.remove(c)
		else:
			st.add(c)
		
	
	return st.__len__() <= 1

# TODO(Inder Pooni) 1.5 One Away: Given two string s & t check if they are one ( or zero ) edit(s) ( add , remove , replace ) away

def one_away(s , t):
	return False





if __name__ == "__main__":
	# sampleTest1 = 'cat'
	# sampleTest2 = 'attack'
	# sampleTest3 = '     '

	# perm1 = 'tej'
	# perm2 = 'etj'
	# perm3 = 'avc'

	print(palindrome_permutation('carerac'))
	# print(check_permutation(perm1, perm2))
	# print(check_permutation(perm1, perm3))

	# print(isUnique(sampleTest1))
	# print(isUnique(sampleTest2))
	# print(isUnique(sampleTest3))
