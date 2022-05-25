def bottle_song(n):
	# write your code here!
	num = n
	
	while n > 2:
		str = f"""
		{n} bottles of beer on the wall, {n} bottles of beer.
		Take one down and pass it around, {n-1} bottles of beer on the wall.
		{n-1} bottles of beer on the wall, {n-1} bottles of beer."""

		print(str)
		n = n - 1

	str = f"""
	\t2 bottles of beer on the wall, 2 bottles of beer.
	\tTake one down and pass it around, 1 bottle of beer on the wall.
	\t1 bottle of beer on the wall, 1 bottle of beer. 
	\n\t\tTake one down and pass it around, no more bottles of beer on the wall.
	\tNo more bottles of beer on the wall, no more bottles of beer.
	\tGo to the store and buy some more, {num} bottles of beer on the wall"""

	print(str)
	
print(bottle_song(9))
