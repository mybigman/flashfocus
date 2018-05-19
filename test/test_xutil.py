"""Testsuite for flashfocus.xutil."""
from pytest import approx
from xpybutil.ewmh import get_wm_window_opacity

from flashfocus.xutil import *


def test_get_wm_class(window):
    assert get_wm_class(window) == ("window1", "Window1")


def test_create_message_window():
    window = create_message_window()
    set_opacity(window, 0.8)


def test_set_opacity(window):
    set_opacity(window, 0.5)
    assert get_wm_window_opacity(window).reply() == approx(0.5)
