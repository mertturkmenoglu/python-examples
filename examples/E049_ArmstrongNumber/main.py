# Example 049: Armstrong number

def is_armstrong(num: int) -> bool:
    return True if sum(int(d) ** 3 for d in str(num)) == num else False


if __name__ == "__main__":
    print(is_armstrong(153))
    print(is_armstrong(407))
    print(is_armstrong(100))