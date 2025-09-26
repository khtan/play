""" lib/core.py containing basic core helper functions """
import os
import json
from pathlib import Path
from typing import Sequence, TypeVar
from expression import Error, Ok, Result
from common.core_classes import IChingConfig

HaveAddOperator = TypeVar('HaveAddOperator', int, float, str, bytes)
# reminder for error string type
errstr = str # pylint: disable=invalid-name
T1 = HaveAddOperator
def greet(name: str) -> str:
    """ Returns a greeting message """
    return f"Hello, {name}"

def add(a: T1, b: T1) -> T1:
    """ Returns the + of two values """
    return a + b
# region sf functions
def view_file(file_path: str) -> None:
    """ Brings up Windows default app on the file_path """
    try:
        os.startfile(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except (IOError, OSError) as e:
        print(f"IOError or OSError on {file_path}: {e}")
    except Exception as e: # pylint: disable=W0718
        print(f"An unexpected error occurred: {e}")

def load_json(file_path: str) -> Result[IChingConfig, str]:
    """ Loads a JSON file """
    if not os.path.exists(file_path):
        return Error(f"File {file_path} not found")

    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            json_str = json.dumps(data)
            config: IChingConfig = json.loads(json_str, object_hook=IChingConfig) # type: ignore
            return Ok(config)
        except json.JSONDecodeError as e:
            return Error(f"Failed to parse JSON from {file_path}: {e}")
        # Break broad-except for FP style
        except Exception as e: # pylint: disable=broad-except
            return Error(f"Unexpected error occurred while loading {file_path}: {e}")
# endregion sf functions
# region sc functions
def get_hexagram_unicode(hexagram_number: int) -> Result[str, errstr]:
    """ Get the Unicode character for a given hexagram number (1-64) """
    if 1 <= hexagram_number <= 64:
        return Ok(chr(0x4DC0 + hexagram_number - 1))
    else:
        return Error("Hexagram number must be between 1 and 64")

def get_trigram_unicode(trigram_number: int) -> Result[str, errstr]:
    """ Get the Unicode character for a given trigram number (1-8) """
    if 0 <= trigram_number <= 7:
        return Ok(chr(0x2630 - trigram_number + 7))
    else:
        return Error("Trigram number must be between 0 and 7")

def generate_html(
    hex_numbers: Sequence[int],
    center_string: str = "+",
    show_num: bool = False,
    output_file: str = "hexagrams.html"
) -> Result[None, str]:
    """
    Generate an HTML file displaying given hexagram numbers as Unicode characters
    arranged evenly around a circle, with a center character.

    Args:
        hex_numbers: List of hexagram numbers (integers).
        center_string: Character to display at the center.
        show_num: Whether to display hexagram numbers under characters.
        output_file: Path to the HTML file to generate.

    Returns:
        Result[None, str]: Ok(None) on success, Error(str) on failure.
    """
    hex_chars = []
    for n in hex_numbers:
        result = get_hexagram_unicode(n)
        if result.is_error():
            return Error(f"Skipping hexagram {n}: {result.error}")
        hex_chars.append((n, result.ok))  # store number + char

    n = len(hex_chars)
    if n == 0:
        return Error("No valid hexagrams to display.")

    angle_step = 360 / n
    # Dynamically adjust radius: 25vmin for n=10, proportional otherwise
    radius = 25 * (n / 40)
    radius_css = f"{radius:.1f}vmin"

    html_parts = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "<meta charset='UTF-8'>",
        "<title>Hexagrams Circle</title>",
        """
<style>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}
.circle {
  position: relative;
  width: 80vmin;
  height: 80vmin;
  border-radius: 50%;
  margin: auto;
}
.hex {
  position: absolute;
  left: 50%;
  top: 50%;
  transform-origin: 0 0;
  font-size: 2rem;
  text-align: center;
}
.center-char {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  font-size: 2.5rem;
  font-weight: bold;
}
.num-label {
  display: block;
  font-size: 0.8rem;
}
</style>
""",
        "</head><body>",
        "<div class='circle'>",
        f"<div class='center-char'>{center_string}</div>",
    ]

    for i, (num, char) in enumerate(hex_chars):
        angle = i * angle_step
        inner_html = char
        if show_num:
            inner_html += f"<span class='num-label'>{num}</span>"

        html_parts.append(
            (
                "<div class='hex' style="
                f"'transform: rotate({angle}deg) translate({radius_css}) rotate(-{angle}deg);'>"
                f"{inner_html}</div>"
            )
        )

    html_parts.extend(["</div></body></html>"])

    try:
        Path(output_file).write_text("\n".join(html_parts), encoding="utf-8")
        return Ok(None)
    except OSError as e:
        return Error(f"Failed to write HTML file '{output_file}': {e}")

# endregion sc functions
