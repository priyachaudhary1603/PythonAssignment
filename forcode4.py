import logging

logging.basicConfig(
    filename="sort.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_sorted_ascending(nums: list) -> bool:
    """
    Check whether a list is sorted in ascending order using a for loop.
    Parameters:
        nums (list): List of numbers
    Returns:
        bool: True if the list is sorted in ascending order, False otherwise
    """
    logging.info("Checking if the list is sorted in ascending order")

    if len(nums) < 2:
        logging.info("List has fewer than 2 elements, considered sorted")
        return True

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            logging.warning(
                f"List is not sorted: {nums[i]} > {nums[i + 1]} at index {i}"
            )
            return False

    logging.info("List is sorted in ascending order")
    return True

nums = [1, 2, 3, 4, 5]
result = is_sorted_ascending(nums)

print("Is the list sorted in ascending order?", result)