def key_with_value(dic, value):
    '''
        Returns the key associated with the passed-in value.
        WARNING: Behavior is undefined if there's more than one key that has the passed-in value.
    '''
    return [k for k,v in dic.items() if v == value][0]


def key_with_value_case_insensitive(dic, value):
    '''
        Returns the key associated with the passed-in value.
        WARNING: Behavior is undefined if there's more than one key that has the passed-in value.
        WARNING: The value being looked for and all the items in the passed-in dictionary must be strings.
    '''
    return [k for k,v in dic.items() if v.lower() == value.lower()][0]
