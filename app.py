from models.models import (user_chooses_copy_or_move,
                           get_source_and_target_directories,
                           action_all_files_or_specified,
                           perform_move_or_copy)

# asks the user whether wants to copy or move the files
copy_or_move_choice = user_chooses_copy_or_move()

# returns tuple of directories: (src, tgt)
src_and_tgt_dirs = get_source_and_target_directories(copy_or_move=copy_or_move_choice)

# asks whether to action on all files in the dir or just specific files
all_or_list = action_all_files_or_specified()

if all_or_list == 'l':
    # TODO: Implement checks on the txt file, kind of the point of the whole thing.
    # TODO: Clean this up, it looks dreadful
    print(f"\nDue to time constraints, it was not coded in to ensure the list_of_files.txt file exists or is populated")
    print("If it's not present, since you selected 'l' it will not throw an error to you but it will just do nothing")
    print(f"If it's not there then create list_of_files.txt where app.py exists"
          f" and populate it with target filenames on each row, such as")
    for n in range(3):
        print(f"target_filename_{n}.extension")

    print("\n!Make sure you have included the file extensions!")
    list_of_files = []
    with open('list_of_files.txt', 'r') as txtfile:
        for line in txtfile.readlines():
            list_of_files.append(line.replace('\n', ''))
    print(f"Files in text file are: {list_of_files}")
    perform_move_or_copy(move_or_copy=copy_or_move_choice,
                         src=src_and_tgt_dirs[0],
                         tgt=src_and_tgt_dirs[1],
                         list_of_files=list_of_files)
elif all_or_list == 'a':
    # re-formatting from c or m for use in f string literals later on
    if copy_or_move_choice == 'c':
        print_choice = 'copy'
    elif copy_or_move_choice == 'm':
        print_choice = 'move'
    print(f"{print_choice}ing all files from source to target directory")
    perform_move_or_copy(move_or_copy=copy_or_move_choice,
                         src=src_and_tgt_dirs[0],
                         tgt=src_and_tgt_dirs[1],
                         list_of_files=None)
