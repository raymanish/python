class Ticket:
    ticket_count = 0
    resolved_count = 0

    def _init_(self, number, name, staff_id, email, problem, response="", status="Open"):
        Ticket.ticket_count += 1
        self.number = number
        self.name = name
        self.staff_id = staff_id
        self.email = email
        self.problem = problem
        self.response = None
        self.status = "Open"

    def respond(self, response):
        self.response = response

    def resolve(self):
        self.status = "Resolved"
        Ticket.resolved_count += 1

    def change_password(self, new_password):
        # Simulate password change process
        self.response = f"Password changed successfully. New password: {new_password}"
        self.status = "Closed"
        return self.response

class TicketingSystem:
    def _init_(self):
        self.tickets = []
        self.closed_tickets_count = 0
    def create_ticket(self, name, staff_id, email, problem):
        number:int = len(self.tickets) + 1
        ticket = Ticket(number, name, staff_id, email, problem)
        self.tickets.append(ticket)
        return ticket

    def process_password_change_request(self, ticket, new_password):
        if ticket.status == "Open":
            ticket.change_password(new_password)
            self.closed_tickets_count += 1
            return "Password change request processed successfully."
        else:
            return "Ticket is already closed."



    def print_tickets(self):
        for ticket in self.tickets:
            print(f"Ticket Number: {ticket.number}")
            print(f"Name: {ticket.name}")
            print(f"Staff ID: {ticket.staff_id}")
            print(f"Email: {ticket.email}")
            print(f"Problem: {ticket.problem}")
            print(f"Response: {ticket.response}")
            print(f"Status: {ticket.status}")
            print()

    def get_ticket_statistics(self):
        open_tickets = Ticket.ticket_count - Ticket.resolved_count
        closed_tickets = Ticket.resolved_count
        return {
            "Total Tickets Created": Ticket.ticket_count,
            "Total Tickets Resolved": Ticket.resolved_count,
            "Total Open Tickets": open_tickets,

        }


# Example usage
ticketing_system = TicketingSystem()

# Create tickets
ticket1 = ticketing_system.create_ticket("John Doe", "12345", "john@example.com", "Printer not working")
ticket2 = ticketing_system.create_ticket("Jane Smith", "67890", "jane@example.com", "Can't access network drive")
ticket3 = ticketing_system.create_ticket("Bob Brown", "STF003", "bob@example.com", "Software installation issue")
# Responding to tickets
ticket1.respond("Please check the printer connections.")
ticket2.respond("Try restarting your computer and then accessing the drive again.")

# Process password change request for a ticketing staff
response = ticketing_system.process_password_change_request(ticket1, "newpassword123")
print(response)

# Resolving tickets
ticket1.resolve()
ticket2.resolve()

# Print tickets
ticketing_system.print_tickets()

# Get ticket statistics
statistics = TicketingSystem.get_ticket_statistics()
print("Ticket Statistics:")
for key, value in statistics.items():
    print(f"{key}: {value}")