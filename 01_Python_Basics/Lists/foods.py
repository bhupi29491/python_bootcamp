## Copying a List ##

# To copy a list, you can make a slice that includes the entire original list by omitting
# the first index and the second index ([:]).

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_favorite_cricketer = ['Sachin', 'Dhoni', 'Kohli']
my_friend_favorite_cricketer = my_favorite_cricketer[:]

my_favorite_cricketer.append('Yuvraj')
my_friend_favorite_cricketer.append('Rohit')

print("My Favorite players are:")
print(my_favorite_cricketer)

print("\nMy Favorite players are:")
print(my_friend_favorite_cricketer)