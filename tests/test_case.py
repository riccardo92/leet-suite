from typing import Any

import pytest

from leet.test_suite import Case


@pytest.mark.parametrize(
    (
        "enabled",
        "disabled_from_here",
        "enabled_from_here",
        "kwargs",
        "expected_exception",
    ),
    [
        (True, False, False, {}, ValueError),
    ],
)
def test_case_throws(
    enabled: bool,
    disabled_from_here: bool,
    enabled_from_here: bool,
    kwargs: dict,
    expected_exception: Any,
):
    with pytest.raises(expected_exception):
        Case(
            enabled=enabled,
            disabled_from_here=disabled_from_here,
            enabled_from_here=enabled_from_here,
            **kwargs,
        )
