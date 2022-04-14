from pywebcomponents import __version__, render_component


def test_version():
    assert __version__ == "0.1.0"


def test_render_component():
    assert (
        render_component("x-name", "<p><slot></slot></p>", "hello world!")
        == """
        <x-name>
            <template shadowroot="open">
                <p><slot></slot></p>
            </template>
            hello world!
        </x-name>
    """
    )
