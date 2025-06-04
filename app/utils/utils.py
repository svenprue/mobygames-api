import re
from typing import Optional, Union


def zip_lists_into_dict(list_keys: list, list_values: list) -> dict:
    """
    Create a dictionary by pairing elements from two lists.

    Args:
        list_keys (list): List of keys.
        list_values (list): List of values.

    Returns:
        dict: A dictionary created by pairing elements from the input lists.
    """
    return {k: v for k, v in zip(list_keys, list_values)}


def extract_from_url(mobygames_url: Optional[str], element: str = "id") -> Optional[str]:
    """
    Extract a specific element from a MobyGames URL using regular expressions.

    Args:
        mobygames_url (str): The MobyGames URL from which to extract the element.
        element (str, optional): The element to extract (e.g., 'id', 'game_id', 'company_id').

    Returns:
        Optional[str]: The extracted element value or None if not found.
    """
    if not mobygames_url:
        return None

    # MobyGames URL patterns
    patterns = {
        'game_id': r'/game/(?P<game_id>\d+)',
        'company_id': r'/company/(?P<company_id>\d+)',
        'developer_id': r'/developer/(?P<developer_id>\d+)',
        'person_id': r'/person/(?P<person_id>\d+)',
        'group_id': r'/group/(?P<group_id>\d+)',
        'critic_id': r'/critic/(?P<critic_id>\d+)',
        'platform_id': r'/platform/(?P<platform_id>\d+)',
    }

    for pattern_name, pattern in patterns.items():
        if element in pattern_name:
            try:
                match = re.search(pattern, trim(mobygames_url))
                if match:
                    return match.groupdict().get(element)
            except (TypeError, AttributeError):
                continue
    return None


def trim(text: Union[list, str]) -> str:
    """
    Trim and clean up text by removing leading and trailing whitespace and special characters.

    Args:
        text (Union[list, str]): The text or list of text to be trimmed.

    Returns:
        str: The trimmed and cleaned text.
    """
    if isinstance(text, list):
        text = "".join(text)

    return text.strip().replace("\xa0", "")


def safe_regex(text: Optional[Union[str, list]], regex, group: str) -> Optional[str]:
    """
    Safely apply a regular expression and extract a specific group from the matched text.

    Args:
        text (Optional[str]): The text to apply the regular expression to.
        regex: The regular expression pattern.
        group (str): The name of the group to extract.

    Returns:
        Optional[str]: The extracted group value or None if not found or if the input is not a string.
    """
    if not isinstance(text, (str, list)) or not text:
        return None

    try:
        groups = re.search(regex, trim(text)).groupdict()
        return groups.get(group)
    except AttributeError:
        return None


def remove_str(text: Optional[str], strings_to_remove: Union[str, list]) -> Optional[str]:
    """
    Remove specified strings from a text and return the cleaned text.

    Args:
        text (Optional[str]): The text to remove strings from.
        strings_to_remove (Union[str, list]): A string or list of strings to remove.

    Returns:
        Optional[str]: The cleaned text with specified strings removed or None if not found or if
            the input is not a string.
    """
    if not isinstance(text, str):
        return None

    strings_to_remove = list(strings_to_remove)

    for string in strings_to_remove:
        text = text.replace(string, "")

    return trim(text)


def safe_split(text: Optional[str], delimiter: str) -> Optional[list]:
    """
    Split a text using a delimiter and return a list of cleaned, trimmed values.

    Args:
        text (Optional[str]): The text to split.
        delimiter (str): The delimiter used for splitting.

    Returns:
        Optional[list]: A list of split and cleaned values or None if the input is not a string.
    """
    if not isinstance(text, str):
        return None

    return [trim(t) for t in text.split(delimiter)]


def to_camel_case(headers: list) -> list:
    """
    Convert a list of headers to camelCase format.

    Args:
        headers (list): A list of headers in snake_case or space-separated format.

    Returns:
        list: A list of headers in camelCase format.
    """
    camel_case_headers = ["".join(word.capitalize() for word in header.split()) for header in headers]
    camel_case_headers = [header[0].lower() + header[1:] for header in camel_case_headers]

    return [header for header in camel_case_headers]