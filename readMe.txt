Process:
-   At first I missunderstood the problem and thought there was a finite number of each stripe so my method was to order the stripe inputs by length and try slot in longest the first.
    I then realised this was the wrong understanding.
-   I then noticed that, the longer stripes were made up of smaller stripes so to reduce processes, made a list of th single stripes not represented as a single input.
    I thought that if i reduced the towel inputs to only single stripes and stripes made up of non single stripes it would speed up computation
-   I noticed that, espcially the if the first stripe was the colour of the non-single stripe input, it wasnt being complete. So i needed to figure out a method to try every input over very section of the desired towel.
-   This is there for applying the same function slightly changing bits of string/towel, the change being made if the previous towel input worked ... which is recurrsion
-   Knowing i had to use recurssion to apply the function to th output of the previous function, i then rebegan using my new technique.
-   I would try each towel input on the first bit of th desired towel, and if that towel input fit, remove it from the front of te desired towel and try the inputs for the remaining towel.
    I would repeat this until either all towel inputs had been tried : design cannot be made, or there was no stripes left in the desirted towel: the towel can be made.



Results:
    Example Input:
        number of complete towels: 6
        number of ways to complete: 16

    My Input:
        number of complete towels: 247
        number of ways to complete: 692596560138745

    SamDesk Input: 
        number of complete towels: 369
        number of ways to complete: 761826581538190

