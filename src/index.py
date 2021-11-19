from src.data.delete_data import DataDeleter


# This method is not ready to be used yet (can only delete data currently)
if __name__ == '__main__':
    """
    This method is going to be the so called CLI to setup project
    Leaving the input fields empty is also counted as a yes
    """
    answer_choice = "( Y / N )"

    # deleting data
    while True:
        print(f"Do you wish to delete all the previous data? {answer_choice}")
        delete = input().lower()
        if delete == "y" or "":
            DataDeleter.clean_data()
            break
        elif delete == "n":
            break

    # writing urls into json
    # downloading raw data
    # processing nordpool data
