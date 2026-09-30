# EV Battery Management System
# EEE Mini Project - Python

class EVBatteryManagementSystem:

    def __init__(self, capacity_ah):
        self.capacity_ah = capacity_ah
        self.soc = 80.0

    def monitor(self, voltage, current, temperature):
        print("\n--- Battery Status ---")
        print(f"Voltage     : {voltage:.2f} V")
        print(f"Current     : {current:.2f} A")
        print(f"Temperature : {temperature:.2f} °C")
        print(f"SOC         : {self.soc:.1f} %")

        # Protection conditions
        if voltage > 420:
            print("WARNING: Over-Voltage!")
        elif voltage < 300:
            print("WARNING: Under-Voltage!")
        else:
            print("Voltage Status: Normal")

        if current > 100:
            print("WARNING: Over-Current!")
        else:
            print("Current Status: Normal")

        if temperature > 45:
            print("WARNING: High Temperature!")
        elif temperature < 0:
            print("WARNING: Low Temperature!")
        else:
            print("Temperature Status: Normal")

    def update_soc(self, current, time_hours):
        # SOC change using Ah
        charge_used = current * time_hours
        soc_change = (charge_used / self.capacity_ah) * 100

        self.soc -= soc_change

        if self.soc < 0:
            self.soc = 0

        if self.soc > 100:
            self.soc = 100

    def battery_status(self):
        if self.soc >= 80:
            return "Battery Level: High"
        elif self.soc >= 30:
            return "Battery Level: Medium"
        elif self.soc > 0:
            return "Battery Level: Low"
        else:
            return "Battery Empty"


# Main program
print("================================")
print(" EV BATTERY MANAGEMENT SYSTEM")
print("================================")

capacity = float(input("Enter battery capacity (Ah): "))
voltage = float(input("Enter battery voltage (V): "))
current = float(input("Enter battery current (A): "))
temperature = float(input("Enter battery temperature (°C): "))

bms = EVBatteryManagementSystem(capacity)

bms.monitor(voltage, current, temperature)

# Simulate 0.1 hour operation
bms.update_soc(current, 0.1)

print("\n--- Updated Battery Information ---")
print(f"SOC: {bms.soc:.2f} %")
print(bms.battery_status())
