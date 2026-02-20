import logging

logging.basicConfig(
    filename="missingnum.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def find_missing_number(nums: list, n: int) -> int:
    """
    Find the missing number in a list containing numbers from 1 to N.
    Parameters:
        nums (list): List containing numbers from 1 to N with one missing
        n (int): The value of N (maximum number)
    Returns:
        int: The missing number
    """
    logging.info("Finding the missing number from 1 to N")

    total_sum = 0
    for num in nums:
        total_sum += num

    expected_sum = n * (n + 1) // 2
    missing = expected_sum - total_sum

    logging.info(f"Missing number found: {missing}")
    return missing

nums = [1, 2, 4, 5, 6]
n = 6
result = find_missing_number(nums, n)

print("Missing number:", result)