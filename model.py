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
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def get_charge(self, rental: Rental) -> float:
        """
        Calcula o valor de um aluguel específico.
        Este é o método extraído.
        """
        amount = 0
        
        # Lógica de cálculo do valor movida para cá
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
        
        return amount

    def statement(self) -> str:
        total_amount = 0
        frequent_renter_points = 0
        result = f"Rental summary for {self.name}\n"
        
        for rental in self.rentals:
            # O bloco 'if/elif/else' foi substituído por esta chamada de método
            amount = self.get_charge(rental)

            # add frequent renter points
            frequent_renter_points += 1
            if rental.book.price_code == Book.NEW_RELEASE and rental.days_rented > 1:
                frequent_renter_points += 1

            # show each rental result
            result += f"- {rental.book.title}: {amount}\n"
            total_amount += amount
        
        # show total result
        result += f"Total: {total_amount}\n"
        result += f"Points: {frequent_renter_points}"
        return result
