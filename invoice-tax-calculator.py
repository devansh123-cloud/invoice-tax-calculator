from typing import Dict, List #Type hints using dictionaary

#Function to calculate gst
def calculate_tax(subtotal: float) -> float:
    return round(subtotal** 0.18, 2)

#function to display invoice summary
def display_invoice(items: Dict[str, float]) -> None:
    print("\n========== Invoice ==========")
    
 # ✅ Use enumerate to number each item while looping through dictionary
    for idx, (item, price) in enumerate(items.items(), start=1):
        print(f"Item {idx}: {item:<10} - ₹{price}")  # `:<10` = left-align with padding
  #Calculate subtotal and tax
        subtotal = sum(items.values())
        gst = calculate_tax(subtotal)
        total = gst + subtotal
        
    # ✅ Merge data using dictionary | operator (Chapter 12)
    bill_summary = {"Subtotal": subtotal, "GST (18%)": gst, "Total": total}
    
    print()
    # ✅ Loop to print summary section
    for key, value in bill_summary.items():
        print(f"{key}: ₹{value:.2f}")  # .2f formats value to 2 decimal places
    
    print("============================")
# ✅ Function to collect item names and prices using walrus + error handling

def get_items() -> Dict[str, float]:
    items = {}
    while (item := input("Enter item name (or press Enter to finish): ")) != "":
        try:
            price = float(input(f"Enter price for {item}: ₹"))  # ✅ Try converting input to float
        except ValueError:
            print("❌ Invalid price. Please enter a number.")  # ✅ Catch non-numeric input
        else:
            items[item] = price  # ✅ If successful, store item and price
        finally:
            print("---")  # ✅ Always runs, even if input fails (clean UX)
    return items  # ✅ Return the dictionary of items

if __name__ == "__main__":
    print("🧾 Welcome to Invoice Generator")
    items = get_items()  # ✅ Get the user input
    if items:
        display_invoice(items)  # ✅ Show invoice if there are items
    else:
        print("No items entered. Invoice not generated.")  # 
        
    