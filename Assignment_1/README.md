## 2/10/22 ##

I put in a unit tester so that I could easily see where I go wrong with my implementations. It would be told clear that something was wrong because
of the stack trace for the unit test. I looked up the concepts of a* to start. My edits are going to be heavily commented.

I know that this what I'm about to say isn't about the assignment, but the netflix series "All of us are dead" is really good and I reccomend it.

## 2/18/22 ##

I really sat down to figure out how to implement a*. I have a version working for the first example puzzle, but when I use it for the second puzzle, it loops. I thought I did
away with looping. I also looked up the implementation of manhattan distance for my improved scoring method, but the looping kept happening. On the bright side, example 1 still worked with manhattan distance.

It is now almost 4am and I am tired. I might get help from one of my classmates, but I forget his name. When I learn it, I will add it here.

## 2/20/22 ##

I decided to try again with my first attempt commented out entirely. I added a check to make sure there was progress being made, keeping track of the lowest h_value twice and comparing them. If the previous h_value was lower than the new h_value, there was a loop happening and we can return with no solution. At least I think that is how we can tell if there is a solution or not. I tried example_1 again with this check in place and it does work there too. 

With the second attempt in place, I have arbitrary values for the initial values of lowest (h_value) and target_maximum (h_value), so hopefully this never has to run into a scenario where something is over 100,000 spots away from its goal. I fixed the comments on my second attempt to reflect what is actually happening.
