import logging

logging.basicConfig(
    filename="vowel.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def count_vowels(s: str) -> int:
    """
    Count the number of vowels in a given string.
    Parameters:
        s (str): Input string
    Returns:
        int: Total number of vowels in the string.
    """
    logging.info("Counting vowels in the string")
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1

    logging.info(f"Vowel count calculated: {count}")
    return count

s = "programming"
result = count_vowels(s)
print("Vowel count:", result)