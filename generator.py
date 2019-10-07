from random import randint

def next_number(total_so_far, numbers_remaining, set_length):
    """
    Generates the next elemental effect number on a random mech. This assumes the
    average value across all stats is 3 out of 5 and returns an integer between 1 and
    5 inclusive that won't make the mean of 3 impossible
    """
    # if the set number is less than halfway through the set, any value 1-5 is allowed
    if numbers_remaining > (set_length/2):
        return randint(1,5)
    # if not, set minimum and maximum to make sure the mean is 3 at the end
    target_number = (3 * set_length) - total_so_far
    min_value = max(target_number-(5*(numbers_remaining-1)) ,1)
    max_value = min(target_number-(1*(numbers_remaining-1)) ,5)
    return randint(min_value,max_value)

def total(iterabable):
    """
    Calculates the total of all items in an interable. Returns 0 if empty
    """
    if len(iterable) == 0:
        return 0
    else:
        total = 0
        index = 0
        for item in iterable:
            total += iterable[index]
            index += 1
        return total

def make_random_mech_stats(number_of_profiles, number_of_attributes=4):
    """
    Accepts an integer for the desired number of random mech stats and
    returns a list that size of tuple profiles (of default length 4). The tuples 
    contain a value of 1 to 5 inclusive
    """
    mech_array = []
    for profile in range(0,number_of_profiles):
        new_profile = []
        for attribute in range(0,number_of_attributes):
            new_profile.append(next_number(
                total(new_profile),
                number_of_attributes - len(new_profile),
                number_of_attributes
                ))
    return mech_array[]

print(make_random_mech_stats(5))

