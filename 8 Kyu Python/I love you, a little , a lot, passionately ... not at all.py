def how_much_i_love_you(nb_petals):
    output = nb_petals % 6
    match output:
        case 0:
            return "not at all"
        case 1:
            return "I love you"
        case 2:
            return "a little"
        case 3:
            return "a lot"
        case 4:
            return "passionately"
        case 5:
            return "madly"

