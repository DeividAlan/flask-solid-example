class Process:
    # Wrong method
    def handle(self, username: str, password: str) -> None:
        if isinstance(username, str) and isinstance(password, str):
            print('Access data base ...')
            print('Check user existence ...')
            print('User registration completed successfully...')
        else:
            raise Exception('Invalid data')
    
    # Right method
    def handle(self, username: str, password: str) -> None:
        if self.__verify_input_data(username, password):
            self.__verify_input_in_database(username)
            self.__insert_new_user(username, password)
        else:
            self.__raise_error('Invalid data')

    def __verify_input_data(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str)

    def __verify_input_in_database(self, username: str) -> None:
        print('Access data base ...')
        print('Check user existence ...')

    def __insert_new_user(self, username: str, password: str) -> None:
        print('User registration completed successfully ...')

    def __raise_error(self, message: str) -> Exception:
        raise Exception(message)