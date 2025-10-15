# leet-suite

This package provides some tools to more easily test and develop solutions you write for leetcode problems. See below for example usage.

## Installing

You can install directly from PyPI using e.g.

```bash
uv add leet-suite
```

or

```bash
pip install leet-suite
```

or you can install locally from file using:

```bash
uv pip install -e <location_on_disk>
```

## Developing

This repo provides a devcontainer to easily develop the package. It assumes you have `uv` and `fish` installed on your host system. This cannot be made optional because these assumptions involve bind mounts.

Install the package locally (symlinked) within the `venv` created by `uv` using:

```bash
uv pip install -e .
```

### Pre-commit

We use `pre-commit` to run a few hooks to ensure code quality and stuff like that. Please use the devcontainer, all this is taken care for you if you do so.

### Running tests

We use `tox` for bothing running the tests as well as running `pre-commit`. Please run `tox` to run your tests.

## Contributing

Please see `CONTRIBUTING.md`.

## Issues

If you discover bugs or other issues, please create an issue with a stack trace and code to reproduce. We have no predefined format for issues, just make sure there is enough info to reproduce.

## Example usage

In your leet solution file:

In-place solutions:

```python
class Solution:

    def rotate(self, ...) -> ...:
        ...

if __name__ == "__main__":

    from leet.test_suite import Submission, Case
    cases = [
        Case(
            matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
            solution=[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]],
        ),
    ]

    sub = Submission(
        callable=Solution().rotate,
        cases=cases,
        inplace=True,
        throw=False,
        verbose=True
    )
    sub.run(inplace_arg="matrix")
```

Not in-place

```python
class Solution:

    def myPow(self, ...) -> ...:
        ...

if __name__ == "__main__":

    from leet.test_suite import Submission, Case
    # from leet.test_suite.comparators import nested_list_comparator

    cases = [
        Case(x=2.00000, n=10, solution=1024.00000).disable_from_here(), # disable this case and all following ones ...
        Case(x=2.10000, n=3, solution=9.26100).enable() # enable this one,
        Case(x=2.00000, n=-2, solution=0.25).enable_from_here(), # enabled from here (including this case)
        Case(x=8.66731, n=4, solution=5643.35434, enabled=False), # and disabled using arg
    ]

    sub = Submission(
        callable=Solution().myPow,
        cases=cases,
        inplace=False,
        throw=False,
        verbose=True
    )
    sub.run(comparator=lambda x, y: round(x, 3) == round(y, 3))
```

Nested-list comparison

```python
class Solution:

    def groupAnagrams(self, ...) -> ...:
        ...

if __name__ == "__main__":

    from leet.test_suite import Submission, Case
    from leet.test_suite.comparators import nested_list_comparator

    cases = [
        Case(
            strs=["eat", "tea", "tan", "ate", "nat", "bat"],
            solution=[["bat"], ["nat","tan"], ["ate","eat","tea"]],
        ).disable(), # Disable a case
        Case(
            strs=["","b"],
            solution=[["b"], [""]],
        )
    ]

    sub = Submission(
        callable=Solution().groupAnagrams,
        cases=cases,
        inplace=False,
        throw=False,
        verbose=True
    )
    sub.run(comparator=nested_list_comparator)
```
