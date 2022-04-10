# Модуль "получения" данных для логирования.

def get_user_info(number_of_users):
    user_id = [i for i in range(1, number_of_users + 1)]
    user_info = {'id': user_id}
    user_info.update({'user_name':[f'user_name_{i}' for i in range(1, number_of_users)]})
    user_info.update({'user_surname': [f'user_surname_{i}' for i in range(1, number_of_users)]})
    user_info.update({'date_of_birth':[f'date_of_birth_{i}' for i in range(1, number_of_users)]})
    user_info.update({'phone_number': [f'phone_number_{i}' for i in range(1, number_of_users)]})
    
    return user_info
