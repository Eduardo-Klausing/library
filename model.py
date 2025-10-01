# model.py

class Book:
    REGULAR: int = 0
    NEW_RELEASE: int = 1
    CHILDREN: int = 2

    def __init__(self, title: str, price_code: int):
        # ATRIBUTOS RENOMEADOS (sem _)
        self.title = title
        self.price_code = price_code

    # MÉTODOS @property REMOVIDOS


class Rental:
    def __init__(self, book: Book, days_rented: int):
        # ATRIBUTOS RENOMEADOS (sem _)
        self.book = book
        self.days_rented = days_rented

    # MÉTODOS @property REMOVIDOS


class Client:
    def __init__(self, name: str):
        # ATRIBUTOS RENOMEADOS (sem _)
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        # ATRIBUTO RENOMEADO AQUI TAMBÉM
        self.rentals.append(rental)

    # MÉTODO @property REMOVIDO

    def statement(self) -> str:
        total_amount = 0
        frequent_renter_points = 0
        # O ACESSO a self.name já era assim, então não muda.
        result = f"Rental summary for {self.name}\n"
        
        # ATRIBUTO RENOMEADO AQUI (de _rentals para rentals)
        for rental in self.rentals:
            amount = 0
            
            # O acesso a rental.book.price_code não muda, pois
            # do ponto de vista do código "cliente", a sintaxe é a mesma.
            if rental.book.price_code == Book.REGULAR:
                amount += 2
                if rental.days_rented > 2:
                    amount += (rental.days_rented - 2) * 1.5
            elif rental.book.price_code == Book.NEW_RELEASE:
                amount += rental.days_rented * 3
            elif rental.book.price_code == Book.CHILDREN:
                amount += 1.5
                if rental.days_rented > 3:
                    amount += (rental.days_rented - 3) * 1.5

            frequent_renter_points += 1
            if rental.book.price_code == Book.NEW_RELEASE and rental.days_rented > 1:
                frequent_renter_points += 1

            result += f"- {rental.book.title}: {amount}\n"
            total_amount += amount
        
        result += f"Total: {total_amount}\n"
        result += f"Points: {frequent_renter_points}"
        return result