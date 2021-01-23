"""
Date:Jan. 22 2021
Author:Andrew Lin
Description: An S-Expression Calculator that performs the add and multiply
operator on natural numbers.
"""
import sys

def get_parsed_list(string):
    """
    get_parsed_list(string) Consumes a string and returns the string
        in a parsed list
    Examples:
        "(add 5 5)" -> ["(", "add", "5", "5", ")" ]
    :param string: Str
    :return: list[Str]
    """
    splitted_string = string.split()
    final_parsed_list = []
    # If there is a ")" or "(" append to final_parsed_list seperating
    # the word and ")" or "("
    for element in splitted_string:
        if (")" in element):
            final_parsed_list.append(element[0:-1])
            final_parsed_list.append(")")
        elif ("(" in element):
            final_parsed_list.append("(")
            final_parsed_list.append(element[1:])
        else:
            final_parsed_list.append(element)
    return final_parsed_list

def first_cut_off(parsed_list):
    """
    first_cut_off(parsed_list) Given a parsed list return the first cutoff
    Example:
        ["(", "add", "5", "6", ")" ] -> "5"

    :param parsed_list: list[Str]
    :return: Str
    """
    cut_list = parsed_list.copy()
    cut_list = cut_list[2:-1]
    # If the first element is not "(", return the first element
    if (cut_list[0] != "("):
      return convert_string(cut_list)
    else:
      count = 0
      first_tree_list = []
    # The code checks each element of the list and appends to
    # a new list.  It uses count as a stack to consider the
    # number of brackets for when to stop appending.
      for element in cut_list:
        if (element == "("):
          count += 1
          first_tree_list.append(element)
        elif (element == ")"):
          count -= 1
          if (count == 0):
            first_tree_list.append(element)
            break
          else:
            first_tree_list.append(element)
        else:
          first_tree_list.append(element)
      return convert_string(first_tree_list)

def rest_cut_off(parsed_list):
    """
    rest_cut_off(parsed_list) Given a parsed list return the rest cutoff
    Example:
        ["(", "add", "5", "6", ")" ] -> "6"

    :param parsed_list: list[Str]
    :return: Str
    """
    rest_list = parsed_list.copy()
    rest_list = rest_list[2:-1]
    # If the first element is not "(", return everything after that element
    if (rest_list[0] != "("):
        rest_list = rest_list[1:]
        return convert_string(rest_list)
    else:
    # The code checks each element of the list and appends to
    # a new list.  It uses count as a stack to consider the
    # number of brackets.
      count = 0
      for index in range(0, len(rest_list)):
        if (rest_list[index] == "("):
          count += 1
        elif (rest_list[index] == ")"):
          count -= 1
          if (count == 0):
            rest_list = rest_list[index+1:]
            break
      return convert_string(rest_list)

def convert_string(parsed_list):
    """
    convert_string(parsed_list) Consumes a list of string and produces a string
    Examples:
        ["(", "add", "(", "multiply" ,"2", "3", ")", "8", ")"] -> "(add (multiple 2 3) 8)"
    :param parsed_list: list[Str]
    :return: Str
    """
    # if the list doesn't start with "(" then return
    # the first part element of the list
    if (parsed_list[0] != "(" ):
        return parsed_list[0]
    else:
        count = 0
        final_list = []
    # The code checks each element of the list and appends to
    # a new list.  It uses count as a stack to consider the
    # number of brackets and when to add spaces between lists.
        for index in range(0, len(parsed_list)):
            if (parsed_list[index] == "("):
                count += 1
                final_list.append(parsed_list[index])
            elif (count > 0):
                count -= 1
                final_list.append(parsed_list[index])
                final_list.append(" ")
            elif (parsed_list[index] == ")"):
                del final_list[-1]
                final_list.append(parsed_list[index])
                final_list.append(" ")
            else:
                final_list.append(parsed_list[index])
                final_list.append(" ")
        del final_list[-1]
        return "".join(final_list)

def calc(string_input):
    """
    calc(string_input) Consumes an S-Expression string and produces the expression evaluated.
    :param string_input: Str
    :return: Nat
    """
    if (string_input.isdigit() == True):
        return int(string_input)
    else:
        if (get_parsed_list(string_input)[1] == "add"):
          return (calc(first_cut_off(get_parsed_list(string_input))) +
                  calc(rest_cut_off(get_parsed_list(string_input))))
        elif (get_parsed_list(string_input)[1] == "multiply"):
          return (calc(first_cut_off(get_parsed_list(string_input))) *
                  calc(rest_cut_off(get_parsed_list(string_input))))

def main():
    s = sys.argv[1]
    print(calc(s))

main()