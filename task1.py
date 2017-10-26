# Program to sort alphabetically the words form a string provided by the user
import sys


def is_valid_node(node):
    if len(node) > 0:
        return True

    return False


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    return False


def main():
    sys.stdout.write("Please input word(s):")
    sys.stdout.flush()

    for line in sys.stdin:
        print("Input:")
        print(line)

        # breakdown the string into a list of nodes
        nodes = line.split()

        words = []
        nums = []
        node_types = [] # 0 : string, 1 : number

        for node in nodes:
            node = node.strip()
            if is_valid_node(node):
                if is_number(node):
                    node_types.append(1)
                    nums.append(node)
                else:
                    node_types.append(0)
                    words.append(node)

        # sort the list
        words.sort()
        nums.sort()

        # display the sorted nodes
        print("Output:")
        pos_word = 0
        pos_num = 0
        for type in node_types:
            if type == 0:
                sys.stdout.write(words[pos_word] + " ")
                pos_word += 1
            elif type == 1:
                sys.stdout.write(nums[pos_num] + " ")
                pos_num += 1
        print();

        sys.stdout.write("Please input word(s):")
        sys.stdout.flush()


main()
