""" functions pertaining to hexagrams and trigrams """
import math
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
    min_radius = 12
    scale_by_number_of_hexagrams = 35
    radius = max(min_radius, 25 * (n / scale_by_number_of_hexagrams))  # trial and error for now
    return f"{radius:.1f}vmin"

def build_hexagram_circle_html(
        num: int, angle: float, radius_css: str, show_num: bool) -> Result[str, str]:
    """Build the HTML div for a single hexagram in circular layout."""
    result = get_hexagram_unicode(num)
    if result.is_error():
        return Error(f"Skipping hexagram {num}: {result.error}")

    char = result.ok
    inner_html = char
    if show_num:
        inner_html += f"<span class='num-label'>{num}</span>"

    html_div = (
        "<div class='hex-circle' style="
        f"'transform: rotate({angle}deg) translate({radius_css}) rotate(-{angle}deg);'>"
        f"{inner_html}</div>"
    )
    return Ok(html_div)

def build_hexagram_square_html(num: int, show_num: bool) -> Result[str, str]:
    """Build the HTML div for a single hexagram in square layout."""
    result = get_hexagram_unicode(num)
    if result.is_error():
        return Error(f"Skipping hexagram {num}: {result.error}")

    char = result.ok
    inner_html = char
    if show_num:
        inner_html += f"<span class='num-label'>{num}</span>"

    html_div = f"<div class='hex-square'>{inner_html}</div>"
    return Ok(html_div)

def build_css_common() -> str:
    """Build common CSS styles shared across all display types."""
    return """
body {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
}
.num-label {
  display: block;
  font-size: 0.8rem;
}
.center-char {
font-size: 2.5rem;
font-weight: bold;}
"""

def build_css_circle() -> str:
    """Build CSS styles for circle layout."""
    return """
.circle {
  position: relative;
  width: 80vmin;
  height: 80vmin;
  border-radius: 50%;
  margin: auto;
}
.hex-circle {
  position: absolute;
  left: 50%;
  top: 50%;
  transform-origin: 0 0;
  font-size: 2rem;
  text-align: center;
}
.circle .center-char {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}"""

def build_css_square() -> str:
    """Build CSS styles for square layout."""
    return """
.square-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: center;
}
.square-row {
  display: flex;
  gap: 10px;
  justify-content: center;
}
.hex-square {
  font-size: 2rem;
  text-align: center;
  padding: 10px;
  border-radius: 5px;
  min-width: 60px;
}
.square-container .center-char {
  margin-bottom: 20px;
}"""

def build_header(display_type: str = "circle") -> str:
    """Build the HTML header with CSS styles."""
    css_parts = [build_css_common()]

    if display_type == "square":
        css_parts.append("body { min-height: 100vh; padding: 20px; }")
        css_parts.append(build_css_square())
    elif display_type == "circle":
        css_parts.append("body { height: 100vh; }")
        css_parts.append(build_css_circle())
    elif display_type == "all":
        css_parts.append("body { height: 100vh; }")
        css_parts.append("""
.combined-container {
  position: relative;
  width: 90vmin;
  height: 90vmin;
}
.combined-container .circle {
  width: 100%;
  height: 100%;
}
.combined-container .square-container {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  gap: 5px;
  z-index: 10;
}
.combined-container .square-row {
  gap: 5px;
}
.combined-container .hex-square {
  font-size: 1.5rem;
  padding: 5px;
  background-color: rgba(255, 255, 255, 0.9);
  min-width: 45px;
}
.combined-container .center-char {
  font-size: 2rem;
  margin-bottom: 10px;
  background-color: rgba(255, 255, 255, 0.9);
  padding: 5px 10px;
}""")
        css_parts.append(build_css_circle())
        css_parts.append(build_css_square())

    css_style = "<style>" + "\n".join(css_parts) + "\n</style>"

    header_parts = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        "<meta charset='UTF-8'>",
        "<title>Hexagrams</title>",
        css_style,
        "</head><body>",
    ]
    return "\n".join(header_parts)

def build_circle_hexagrams(
    hex_numbers: Sequence[int],
    origin_string: str,
    show_num: bool
) -> Result[str, str]:
    """Build the circle div with hexagrams arranged around a center."""
    n = len(hex_numbers)
    if n == 0:
        return Error("No hexagrams to display.")
    radius_css = compute_radius(n)
    angle_step = 360 / n
    circle_parts = [
        "<div class='circle'>",
        f"<div class='center-char'>{origin_string}</div>",
    ]

    for i, num in enumerate(hex_numbers):
        angle = i * angle_step
        hex_div_res = build_hexagram_circle_html(num, angle, radius_css, show_num)
        if hex_div_res.is_error():
            return Error(hex_div_res.error)
        circle_parts.append(hex_div_res.ok)

    circle_parts.append("</div>")
    return Ok("\n".join(circle_parts))

def build_square_hexagrams(
    hex_numbers: Sequence[int],
    origin_string: str,
    show_num: bool
) -> Result[str, str]:
    """Build a square grid with hexagrams arranged in rows."""
    n = len(hex_numbers)
    if n == 0:
        return Error("No hexagrams to display.")

    # Calculate number of columns (square root, rounded up)
    cols = math.ceil(math.sqrt(n))

    square_parts = [
        "<div class='square-container'>",
        f"<div class='center-char'>{origin_string}</div>",
    ]

    # Process hexagrams in rows
    for row_start in range(0, n, cols):
        row_end = min(row_start + cols, n)
        row_hexagrams = hex_numbers[row_start:row_end]

        square_parts.append("<div class='square-row'>")
        for num in row_hexagrams:
            hex_div_res = build_hexagram_square_html(num, show_num)
            if hex_div_res.is_error():
                return Error(hex_div_res.error)
            square_parts.append(hex_div_res.ok)
        square_parts.append("</div>")

    square_parts.append("</div>")
    return Ok("\n".join(square_parts))

def build_footer() -> str:
    """Build the HTML footer."""
    return "</body></html>"

def build_html_page(
    hex_numbers: Sequence[int],
    show_num: bool,
    display_type: str = "circle"
) -> Result[str, str]:
    """Build the full HTML page as a string."""
    # for debugging
    center_square = "+"
    center_circle = "o"
    header = build_header(display_type)

    layout_parts = []

    # Wrap content for "all" display type
    if display_type == "all":
        layout_parts.append("<div class='combined-container'>")

    if display_type in ("square", "all"):
        square_res = build_square_hexagrams(hex_numbers, center_square, show_num)
        if square_res.is_error():
            return Error(square_res.error)
        layout_parts.append(square_res.ok)

    if display_type in ("circle", "all"):
        circle_res = build_circle_hexagrams(hex_numbers, center_circle, show_num)
        if circle_res.is_error():
            return Error(circle_res.error)
        layout_parts.append(circle_res.ok)

    if display_type == "all":
        layout_parts.append("</div>")

    footer = build_footer()

    html_parts = [header] + layout_parts + [footer]
    return Ok("\n".join(html_parts))

def generate_html(
    hex_numbers: Sequence[int],
    show_num: bool = False,
    output_file: str = "hexagrams.html",
    display_type: str = "circle"
) -> Result[None, str]:
    """Generate HTML file for hexagrams arranged in a circle, square, or both.

    Args:
        hex_numbers: Sequence of hexagram numbers (1-64)
        show_num: Whether to show hexagram numbers
        output_file: Output HTML filename
        display_type: "circle", "square", or "all" (both circle and square combined)
    """
    if not hex_numbers:
        return Error("No hexagram numbers provided.")

    if display_type not in ("circle", "square", "all"):
        estr = f"Invalid display_type '{display_type}'. Must be 'circle', 'square', or 'all'."
        return Error(estr)

    html_res = build_html_page(hex_numbers, show_num, display_type)
    if html_res.is_error():
        return Error(html_res.error)

    try:
        Path(output_file).write_text(html_res.ok, encoding="utf-8")
        return Ok(None)
    except OSError as e:
        return Error(f"Failed to write HTML file '{output_file}': {e}")
