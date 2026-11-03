def simple_interest(p, r, t):
    # p = principal, r = yearly rate (%), t = years
    return p * r * t / 100


def compound_interest(p, r, t):
    # interest compounded once a year
    amount = p * (1 + r / 100) ** t
    return amount - p


def calculate_emi(p, r, months):
    # r = yearly rate (%), months = loan duration in months
    monthly_rate = r / 12 / 100
    if monthly_rate == 0:
        return p / months
    factor = (1 + monthly_rate) ** months
    return p * monthly_rate * factor / (factor - 1)


def main():
    while True:
        print("\n--- Debt Calculator ---")
        print("1. Simple Interest")
        print("2. Compound Interest")
        print("3. EMI")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "4":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3"):
            print("Invalid choice, try again.")
            continue

        p = float(input("Principal amount: "))
        r = float(input("Yearly interest rate (%): "))

        if choice == "1":
            t = float(input("Time (years): "))
            si = simple_interest(p, r, t)
            print(f"Interest: {si:.2f}")
            print(f"Total amount: {p + si:.2f}")
        elif choice == "2":
            t = float(input("Time (years): "))
            ci = compound_interest(p, r, t)
            print(f"Interest: {ci:.2f}")
            print(f"Total amount: {p + ci:.2f}")
        else:
            months = int(input("Loan duration (months): "))
            emi = calculate_emi(p, r, months)
            print(f"Monthly EMI: {emi:.2f}")
            print(f"Total payment: {emi * months:.2f}")
            print(f"Total interest: {emi * months - p:.2f}")


main() 
