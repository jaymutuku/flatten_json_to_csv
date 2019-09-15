from flatten_json_to_csv import flatten_json_to_csv


def test_fib() -> None:
    assert flatten_json_to_csv.fib(0) == 0
    assert flatten_json_to_csv.fib(1) == 1
    assert flatten_json_to_csv.fib(2) == 1
    assert flatten_json_to_csv.fib(3) == 2
    assert flatten_json_to_csv.fib(4) == 3
    assert flatten_json_to_csv.fib(5) == 5
    assert flatten_json_to_csv.fib(10) == 55
