def draw_text(text, text_font, text_col, surface, coordinates):
    """
    Draw the text.
    :param text: text to draw
    :param text_font: font of the text
    :param text_col: color of the text
    :param surface: surface to draw
    :param coordinates: coordinates to draw
    """
    txt = text_font.render(text, True, text_col)
    text_rect = txt.get_rect(center=coordinates)
    surface.blit(txt, text_rect)
