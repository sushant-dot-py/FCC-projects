** start of main.py **

def square_root_bisection(number, tolerance=1e-7, maximum=50):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number

    low = 0
    high = max(1, number)

    root = None

    for _ in range(maximum):
        mid = (low + high) / 2
        square = mid * mid

        # correct convergence condition (important for small numbers like 0.001)
        if (high - low) / 2 <= tolerance:
            root = mid
            break

        if square < number:
            low = mid
        else:
            high = mid

    if root is None:
        print(f"Failed to converge within {maximum} iterations")
        return None

    print(f"The square root of {number} is approximately {root}")
    return root

** end of main.py **

