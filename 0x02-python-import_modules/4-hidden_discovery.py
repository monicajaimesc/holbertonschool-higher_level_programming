#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # interaction in each word of the list
    for i in dir(hidden_4):
        if "__" in i:
            continue
        else:
            print(i)
