# control.py

class PDController:
    def __init__(self, kp=0.15, kd=0.6):
        self.kp = kp
        self.kd = kd
        self.previous_error = 0.0

    def compute_control(self, reference: float, observation: float) -> float:
        # Calculate the current error
        error = reference - observation
        # Calculate the derivative of the error
        derivative = error - self.previous_error
        # Compute the control action using the PD formula
        control_action = self.kp * error + self.kd * derivative
        # Update the previous error for the next time step
        self.previous_error = error
        return control_action
