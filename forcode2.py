import logging

logging.basicConfig(
    filename="bank.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def char_frequency(s: str) -> dict:
    """
    Count the frequency of each character in a given string.
    Parameters:
        s (str): Input string
    Returns:
        dict: Dictionary with character frequencies.
    """
    logging.info("Counting frequency of each character in the string")
    
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    logging.info(f"Character frequency calculated: {freq}")
    return freq

s = "programming"
result = char_frequency(s)

print("Character Frequency:")
for ch, count in result.items():
    print(ch, ":", count)