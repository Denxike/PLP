def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
  else:
    return price
try:
    original_price_input = input("Enter the original price of the item: ")
    original_price = float(original_price_input)

    discount_percent_input = input("Enter the discount percentage: ")
    discount_percentage = float(discount_percent_input)

    final_price = calculate_discount(original_price, discount_percentage)

    if final_price != original_price:
        print(f"A discount of {discount_percentage}% was applied.")
        print(f"The final price after discount is: {final_price:.2f}")
    else:
        print(f"No discount was applied (discount was less than 20%).")
        print(f"The original price was: {original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter valid numbers for price and discount percentage.")
except Exception as e:
    print(f"An error occurred: {e}")

