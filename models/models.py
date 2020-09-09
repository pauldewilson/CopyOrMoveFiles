import os, shutil


def user_chooses_copy_or_move(choice=None):
    if choice is None:
        choice = str(input("\nDo you want to (c)opy or (m)ove files: "))
        return user_chooses_copy_or_move(choice=choice)
    elif choice is not None:
        valid_choices = ['c', 'm']
        if choice.lower() not in valid_choices:
            print("\nJust type 'c' to indicate copy or 'm' to indicate move")
            return user_chooses_copy_or_move(choice=None)
        elif choice in valid_choices:
            return choice.lower()


def get_source_and_target_directories(copy_or_move='copy or move', source=None, target=None):
    # re-formatting from c or m for use in f string literals later on
    if copy_or_move == 'c':
        copy_or_move = 'copy'
    elif copy_or_move == 'm':
        copy_or_move = 'move'

    def check_dir_is_valid(path):
        if os.path.isdir(path) is False:
            print(f"{path} is not valid")
            return False
        elif os.path.isdir(path) is True:
            return path

    # get source dir and check if valid
    if source is None:
        # get dir choice
        source = input(fr'Paste directory you want to {copy_or_move} files from: ')
        return get_source_and_target_directories(copy_or_move=copy_or_move, source=source, target=None)
    # check source choice is valid if provided
    elif source is not None:
        is_choice_valid = check_dir_is_valid(path=source)
        if is_choice_valid is True:
            print("Valid directory found")
            # passing because moving onto getting target dir
            pass
        elif is_choice_valid is False:
            # if the choice was invalid then go back to getting the source
            print(f"\nThe choice {source} was not valid")
            return get_source_and_target_directories(copy_or_move=copy_or_move, source=None, target=None)

    if source is not None and target is None:
        target = input(fr'Paste directory you want to {copy_or_move} files to: ')
        return get_source_and_target_directories(copy_or_move=copy_or_move, source=source, target=target)
    elif source is not None and target is not None:
        is_choice_valid = check_dir_is_valid(path=target)
        if is_choice_valid is True:
            print("Valid directory found")
            # passing because both dirs are valid and just need to return both dirs
            pass
        elif is_choice_valid is False:
            # if the choice was invalid then go back to getting the target
            print(f"\nThe choice {source} was not valid")
            return get_source_and_target_directories(copy_or_move=copy_or_move, source=source, target=None)

    # if made it this far it's because both source and target are not none and are also valid
    print("\nSource and target directories are both valid.")
    if source == target:
        print("NOTE: Source and target directories are the same")
    return source, target


def action_all_files_or_specified(choice=None):
    if choice is None:
        choice = str(input("\nDo you want to move (a)ll files from the source directory or a specific (l)ist?"))
        return action_all_files_or_specified(choice=choice)
    elif choice is not None:
        valid_choices = ['a', 'l']
        if choice.lower() not in valid_choices:
            print("\nNot a valid choice, type 'a' for all or 'l' for list")
            return action_all_files_or_specified(choice=None)
        elif choice.lower() in valid_choices:
            return choice


def perform_move_or_copy(move_or_copy, src, tgt, list_of_files=None):
    # process list of files first if not None
    all_files_in_src_dir = [f for f in os.listdir(src)]
    if list_of_files is not None:
        if move_or_copy == 'm':
            for file in list_of_files:
                try:
                    shutil.move(src=src + '\\' + file, dst=tgt + '\\' + file)
                except:
                    print(f"File {file} not found, passing")
                    pass
        elif move_or_copy == 'c':
            for file in list_of_files:
                try:
                    shutil.copy2(src=src + '\\' + file, dst=tgt + '\\' + file)
                except:
                    print(f"File {file} not found, passing")
                    pass

    # if list_of_files is None then just copying/moving all in dir
    if list_of_files is None:
        for file in os.listdir(path=src):
            if move_or_copy == 'm':
                for file in os.listdir(src):
                    try:
                        shutil.move(src=src + '\\' + file, dst=tgt + '\\' + file)
                    except:
                        print(f"File {file} not found, passing")
                        pass
            elif move_or_copy == 'c':
                for file in os.listdir(src):
                    try:
                        shutil.copy2(src=src + '\\' + file, dst=tgt + '\\' + file)
                    except:
                        print(f"File {file} not found, passing")
                        pass
