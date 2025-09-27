""" functions pertaining to hexagrams and trigrams """
from pathlib import Path
from typing import Sequence
from expression import Error, Ok, Result

# reminder for error string type
errstr = str # pylint: disable=invalid-name

def get_hexagram_unicode(hexagram_number: int) -> Result[str, errstr]:
    """ Get the Unicode character for a given hexagram number (1-64) """
    if 1 <= hexagram_number <= 64:
        return Ok(chr(0x4DC0 + hexagram_number - 1))
    else:
        return Error("Hexagram number must be between 1 and 64")

def compute_radius(n: int) -> str:
    """Compute the circle radius as vmin based on number of hexagrams."""
    min_radius = 10
    scale_by_number_of_hexagrams = 40
    radius = max(min_radius, 25 * (n / scale_by_number_of_hexagrams))  # trial and error for now
    return f"{radius:.1f}vmin"

def build_hex_html(num: int, angle: float, radius_css: str, show_num: bool) -> Result[str, str]:
    """Build the HTML div for a single hexagram number by calling get_hexagram_unicode."""
    result = get_hexagram_unicode(num)
    if result.is_error():
        return Error(f"Skipping hexagram {num}: {result.error}")

    char = result.ok
    inner_html = char
    if show_num:
        inner_html += f"<span class='num-label'>{num}</span>"

    html_div = (
        "<div class='hex' style="
        f"'transform: rotate({angle}deg) translate({radius_css}) rotate(-{angle}deg);'>"
        f"{inner_html}</div>"
    )
    return Ok(html_div)

def build_html_page(
    hex_numbers: Sequence[int],
    radius_css: str,
    center_string: str,
    show_num: bool
) -> Result[str, str]:
    """Build the full HTML page as a string, calling get_hexagram_unicode for each number."""
    n = len(hex_numbers)
    if n == 0:
        return Error("No hexagrams to display.")

    angle_step = 360 / n
    css_style = """
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
"""
    html_parts = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "<meta charset='UTF-8'>",
        "<title>Hexagrams Circle</title>",
        f"{css_style}",
        "</head><body>",
        "<div class='circle'>",
        f"<div class='center-char'>{center_string}</div>",
    ]

    for i, num in enumerate(hex_numbers):
        angle = i * angle_step
        hex_div_res = build_hex_html(num, angle, radius_css, show_num)
        if hex_div_res.is_error():
            return Error(hex_div_res.error)
        html_parts.append(hex_div_res.ok)

    html_parts.append("</div></body></html>")
    return Ok("\n".join(html_parts))


def generate_html(
    hex_numbers: Sequence[int],
    center_string: str = "+",
    show_num: bool = False,
    output_file: str = "hexagrams.html"
) -> Result[None, str]:
    """Generate HTML file for hexagrams arranged in a circle."""
    if not hex_numbers:
        return Error("No hexagram numbers provided.")

    radius_css = compute_radius(len(hex_numbers))
    html_res = build_html_page(hex_numbers, radius_css, center_string, show_num)
    if html_res.is_error():
        return Error(html_res.error)

    try:
        Path(output_file).write_text(html_res.ok, encoding="utf-8")
        return Ok(None)
    except OSError as e:
        return Error(f"Failed to write HTML file '{output_file}': {e}")
