class Ticket:
    def __init__(self, staff_id, creator_name, email, issue_description, ticket_number):
        # Initialize ticket attributes
        self.ticket_number = ticket_number
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.email = email
        self.issue_description = issue_description
        self.response = "Not Yet Provided"
        self.status = "Open"

    def respond(self):
        # Prompt user for response and update ticket details
        print(self.issue_description)
        self.response = input("Your response:")

    def resolve_password_change(self):
        # Resolve password change issue
        new_password = self.generate_password()
        self.response = f"Password changed successfully. New password: {new_password}"
        print(self.response)
        self.status = "Closed"

    def reopen(self):
        # Reopen a ticket
        self.status = "Reopened"

    def generate_password(self):
        # Generate password based on staff ID and creator name
        return self.staff_id[:2] + self.creator_name[:3]

    def print_ticket(self):
        # Print ticket details
        print("Ticket Number:", self.ticket_number)
        print("Ticket Creator:", self.creator_name)
        print("Staff ID:", self.staff_id)
        print("Email Address:", self.email)
        print("Description:", self.issue_description)
        print("Response:", self.response)
        print("Ticket Status:", self.status)


class TicketingSystem:
    def __init__(self):
        # Initialize TicketingSystem attributes
        self.tickets = []
        self.ticket_count = 2000
        self.resolved_count = 0
        self.open_tickets = 0

    def create_ticket(self, staff_id, creator_name, email, issue_description):
        # Create a new ticket
        ticket = Ticket(staff_id, creator_name, email, issue_description, str(self.ticket_count))
        if 'password change' in issue_description.lower():
            ticket.resolve_password_change()
            self.resolved_count += 1
            self.open_tickets -= 1
        self.ticket_count += 1
        self.open_tickets += 1
        self.tickets.append(ticket)

    def resolve_ticket(self, ticket):
        # Resolve a ticket
        ticket.respond()
        self.resolved_count += 1
        self.open_tickets -= 1

    def reopen_ticket(self, ticket):
        # Reopen a ticket
        ticket.reopen()
        self.open_tickets += 1
        self.resolved_count -= 1

    def print_ticket(self, ticket_number):
        # Print ticket details
        for ticket in self.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.print_ticket()
                return
        print('Ticket does not exist')

    def ticket_stats(self):
        # Print ticket statistics
        print(f"Tickets Created: {len(self.tickets)}\nTickets Resolved: {self.resolved_count}\nOpen Tickets: {self.open_tickets}")


# Example Usage
ticketingSystem = TicketingSystem()

while True:
    choice = input('1. Create Ticket\n2. Resolve Ticket\n3. Reopen a ticket\n4. Statistics\n5. Display a ticket\n')
    if choice == '1':
        staff_id = input('Staff ID: ')
        creator_name = input('Creator name: ')
        email = input('Email: ')
        issue_description = input('Description: ')
        ticketingSystem.create_ticket(staff_id, creator_name, email, issue_description)
        feedback = input('Would you like to leave feedback? (y/n) ')
        if feedback.lower() == 'y':
            ticket = ticketingSystem.tickets[-1]
            ticket.respond()

    elif choice == '2':
        ticket_number = input("Ticket number to resolve: ")
        exists = False
        for ticket in ticketingSystem.tickets:
            if ticket.ticket_number == ticket_number:
                ticketingSystem.resolve_ticket(ticket)
                exists = True
                break
        if not exists:
            print("Ticket does not exist.")

    if choice == '3':
        ticket_number = input("Ticket number to reopen: ")
        exists = False
        for ticket in ticketingSystem.tickets:
            if ticket.ticket_number == ticket_number:
                ticketingSystem.reopen_ticket(ticket)
                exists = True
                break
        if not exists:
            print("Ticket does not exist.")

    if choice == '4':
        ticketingSystem.ticket_stats()

    if choice == '5':
        ticket_number = input('Ticket number to display: ')
        ticketingSystem.print_ticket(ticket_number)
