def draw_text(text, text_font, text_col, surface, coordinates):
    txt = text_font.render(text, True, text_col)
    text_rect = txt.get_rect(center=coordinates)
    surface.blit(txt, text_rect)