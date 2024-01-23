class Member:
    def __init__(self, first_name, last_name, membership_type="Basic"):
        self.first_name = first_name # Needs to be property
        self.last_name = last_name
        self.membership_type = membership_type # Needs to be property
        # self.classes_attended = [] 

    def upgrade_membership(self):
        if self.membership_type == "Basic":
            self.membership_type = "Premium"
            print(f"{self.name}'s membership upgraded to Premium.")

    def attend_class(self, exercise):
        self.classes_attended.append(exercise)
        print(f"{self.name} attended {exercise.name} class.")

    def display_info(self):
        membership_info = f"Membership Type: {self.membership_type}"
        classes_info = f"Classes Attended: {', '.join([exercise.name for exercise in self.classes_attended])}"

        print(f"Member Name: {self.name}\n{membership_info}\n{classes_info}")

# Members
basic_member = Member("Jeffery")
premium_member = Member("Katie", membership_type="Premium")
