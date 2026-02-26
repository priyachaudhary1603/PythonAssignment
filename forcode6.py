import logging

logging.basicConfig(
    filename="duplicate.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def remove_duplicates(nums: list) -> list:
    """
    Remove duplicate elements from a list while preserving order.
    Parameters:
        nums (list): Input list
    Returns:
        list: List without duplicates (original order preserved)
    """
    logging.info("Removing duplicate elements from the list while preserving order")

    unique_list = []
    seen = set()

    for num in nums:
        if num not in seen:
            unique_list.append(num)
            seen.add(num)

    logging.info(f"List after removing duplicates: {unique_list}")
    return unique_list

nums = [1, 2, 3, 2, 4, 1, 5, 3]
result = remove_duplicates(nums)

print("List after removing duplicates:", result)