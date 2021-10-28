def output_info(name: str = 'Иван', surname: str = 'Иванов', data: str = '01.01.1987', city: str = 'Матала',
                email: str = 'example@gmail.com', mobile: str = '0123456789') -> None:
    print(f"Имя: {name}\nФамилия: {surname}\nГод рождения: {data}\nГород проживания: {city}\nЭлекторнная почта: {email}"
          f"\nМобильный телефон: {mobile}")
