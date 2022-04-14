__version__ = "0.1.0"


def render_component(name: str, shadow_root: str, slot_content: str):
    return f"""
        <{name}>
            <template shadowroot="open">
                {shadow_root}
            </template>
            {slot_content}
        </{name}>
    """
