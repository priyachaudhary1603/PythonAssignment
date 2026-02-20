import logging

logging.basicConfig(
    filename="list.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def second_largest(nums: list) -> int:
    """
    Find the second largest element in a list using a for loop.
    Parameters:
        nums (list): List of integers
    Returns:
        int: Second largest element in the list
    """
    logging.info("Finding the second largest element in the list")

    if len(nums) < 2:
        logging.error("List must contain at least two elements")
        raise ValueError("List must contain at least two elements")

    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num != largest and num > second_largest:
            second_largest = num

    logging.info(f"Second largest element found: {second_largest}")
    return second_largest

nums = [10, 5, 20, 8, 20]
result = second_largest(nums)

print("Second largest element:", result)