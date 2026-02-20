import logging

logging.basicConfig(
    filename="reverse.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def reverse_string(s: str) -> str:
    """
    Reverse a string using only a for loop (no slicing).
    Parameters:
        s (str): Input string
    Returns:
        str: Reversed string
    """
    logging.info("Reversing the string using only a for loop (no slicing)")

    reversed_str = ""

    for ch in s:
        reversed_str = ch + reversed_str   # prepend each character

    logging.info(f"Reversed string created: {reversed_str}")
    return reversed_str

s = "python"
result = reverse_string(s)

print("Reversed string:", result)