"""Model for aircraft Flights"""

class Flight:
	"""A Flight with particular passenger aircraft."""

	def __init__(self, number, aircraft):
		if not number[:2].isalpha():
			raise ValueError("No Airline code in '{}'".format(number))
		if not number[:2].isupper():
			raise ValueError("Invalid Airline code in '{}'".format(number))
		if not (number[2:].isdigit() and int(number[2:]) <=999 ):
			raise ValueError("Invalid route number '{}'".format(number))

		self._number = number
		self._aircraft = aircraft

		rows, seats = self._aircraft.seating_plan()
		self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

	def number(self):
		return self._number

	def airline(self):
		return self._number[:2]

	def aircraft(self):
		return self._aircraft.model()

	def _parse_seat(self, seat):
		"""Parse a seat designator into valid orw adn letter
		Args:
			seat: A seat designator such as 12F
		Teturns:
			a tuple containing integer adn string from row and seat
		"""
		row_numbers, seat_letters = self._aircraft.seating_plan()

		letter = seat[-1]
		if letter not in seat_letters:
			raise ValueError("Invalid Seat letter {}".format(letter))

		row_text = seat[:-1]
		try:
			row = int(row_text)
		except ValueError:
			raise ValueError("Invalid seat row {}".format(row_text))

		if row not in row_numbers:
			raise ValueError("Invalid row number {}".format(row))

		return row, letter

	def allocate_seats(self, seat, passenger):
		"""Allocate a seat to a passenger
		Args:
			seat: Seat designator such as 12C or 14F
			passenger: name of the passenger
		Raises:
			ValueError is seat is unavailable
		"""
		row, letter = self._parse_seat(seat)

		if self._seating[row][letter] is not None:
			raise ValueError("Seat {} is Occupied".format(seat))

		self._seating[row][letter] = passenger
		
	def relocate_passenger(self, from_seat, to_seat):
		"""Relocate a passenger to a diff seat
		Args:
			from_seat: existing seat designator
			to_seat: new seat designator
		"""
		from_row, form_letter = self._parse_seat(from_seat)
		if self._seating[from_row][form_letter] is None:
			raise ValueError("No passenger to relocate in seat {}".format(from_seat))

		to_row, to_letter = self._parse_seat(to_seat)
		if self._seating[to_row][to_letter] is not None:
			raise ValueError("Seat {} already occupied.".format(to_seat))

		self._seating[to_row][to_letter] = self._seating[from_row][form_letter]
		self._seating[from_row][form_letter] = None

	def num_available_seats(self):
		return sum(sum(1 for s in row.values() if s is None)
			       for row in self._seating
			       if row is not None)

	def make_boarding_cards(self, card_printer):
		for passenger, seat in sorted(self._passenger_seats()):
			card_printer(passenger, seat, self.number(), self.aircraft())

	def _passenger_seats(self):
		"""An iterable series of passenger seating allocations."""
		row_numbers, seat_letters = self._aircraft.seating_plan()
		for row in row_numbers:
			for letter in seat_letters:
				passenger = self._seating[row][letter]
				if passenger is not None:
					yield(passenger, "{}{}".format(row, letter))

# Class to model diff kinds of aircrafts.
#--------------------------------#
#Base Class
class Aircraft:
	#__init__ is called by the constructor.
	def __init__(self, registration):
		self._registration = registration

	def registration(self):
		return self._registration


#Derived Classes
class AirbusA319(Aircraft):
	
    def model(self):
	    return "Airbus A319"

    def seating_plan(self):
	    return range(1, 23), "ABCDEF"
    
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class Boeing777(Aircraft):

	def model(self):
		return "Boeing 777"

	def seating_plan(self):
		return range(1,56), "ABCDEFGHJK"
        
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


#----------------------------#

def make_flights():
	f = Flight("BA378", AirbusA319("G-EUPT"))
	f.allocate_seats('12A','Ashwini Singh')
	f.allocate_seats('15F','Abheesta Vemuru')
	f.allocate_seats('15E','Abinash Beuria')
	f.allocate_seats('1C','Aditya Mohan Singh')
	f.allocate_seats('1D','Anusri Radha')
	
	g = Flight("AF72", Boeing777("F-GSPS"))
	g.allocate_seats('55K','Ashutosh Singh')
	g.allocate_seats('33G','Aparajita Priya')
	g.allocate_seats('4B','Aman Sinha')
	g.allocate_seats('4A','Abhiram H Kumar')

	return f, g


def console_card_printer(passenger, seat, flight_number, aircraft):
	output = "| NAME: {0}"		\
	         " FLIGHT: {1}"	\
	         " SEAT: {2}"		\
	         " AIRCRAFT: {3}"	\
	         "|".format(passenger, flight_number, seat, aircraft)

	banner = '+' + '-' * (len(output) - 2) + '+'
	border = '|' + ' ' * (len(output) - 2) + '|'
	lines = [banner, border, output, border, banner]
	card = '\n'.join(lines)

	print(card)
	print()
