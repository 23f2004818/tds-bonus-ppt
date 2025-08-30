def parse_text_to_slides(text, guidance=""):
    """
    Simple heuristic split: each section separated by blank lines -> one slide.
    LLM can refine slide structure based on guidance.
    """
    sections = [s.strip() for s in text.split("\n\n") if s.strip()]
    slides = []

    for i, section in enumerate(sections, 1):
        lines = section.split("\n")
        title = lines[0][:60]  # First line = title
        content = "\n".join(lines[1:]) if len(lines) > 1 else ""
        slides.append({"title": title, "content": content})

    return slides
