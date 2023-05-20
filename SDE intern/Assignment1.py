def current_index_member_next(old_queue, new_queue, current_index):
    new_index = 0
    old_index = 0
    while old_index != current_index and new_index < len(new_queue) and old_index < len(old_queue):
        if old_index == current_index:
            break
        if old_queue[old_index] == new_queue[new_index]:
            old_index += 1
            new_index += 1
        else:
            old_index += 1
    return new_index

# Main function
def main():
    old_queue = ['A', 'B', 'C', 'D', 'E', 'F', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'A', 'B', 'A']
    new_queue = ['B', 'C', 'E', 'F', 'B', 'C', 'B', 'C', 'B']
    current_index = 7
    
    print("The members of the old Queue are:", end=" ")
    for member in old_queue:
        print(member, end=" ")
    print()
    
    print("The members of the new Queue are:", end=" ")
    for member in new_queue:
        print(member, end=" ")
    print()
    
    current_index_member = old_queue[current_index - 1]
    new_index = current_index_member_next(old_queue, new_queue, current_index - 1)
    print("The new current Index member is:", new_index + 1)

# Execute the main function
if __name__ == "__main__":
    main()
