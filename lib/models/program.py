

class Program:
    def __init__(self, location, trainer, exercise, membership_type="Premium"):
        self.location = location # Needs to be a property
        self.trainer = trainer # Needs to be a property
        self.exercise = exercise # Needs to be a property
        self.membership_type = membership_type # Needs to be a property

    def display_info(self):
        location_info = f"Location: {self.location.name}"
        trainer_info = f"Trainer: {self.trainer.name}"
        exercise_info = f"Exercise: {self.exercise.name}"
        membership_info = f"Membership Type: {self.membership_type}"

        print(f"Premium Information:\n{location_info}\n{trainer_info}\n{exercise_info}\n{membership_info}")