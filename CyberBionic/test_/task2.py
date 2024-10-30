import pytest
import unittest


def body_mass(weight: int, height: int):
    """
    Calculate body mass index (BMI) based on weight and height.
    """

    if not isinstance(weight, int) or not isinstance(height, int):
        raise ValueError("Both weight and height must be integers.")
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive integers.")

    bmi = weight / (height / 100) ** 2
    return round(bmi, 3)


print(body_mass(88, 195))

assert body_mass(70, 195)
assert body_mass(50, 166)
assert body_mass(120, 178)

"""PYTEST"""


def test_valid_values():
    assert body_mass(70, 195) == 18.409
    assert body_mass(50, 166) == 18.145
    assert body_mass(120, 178) == 37.874


def test_zero_values():
    with pytest.raises(ValueError):
        body_mass(0, 195)
    with pytest.raises(ValueError):
        body_mass(70, 0)


def test_negative_values():
    with pytest.raises(ValueError):
        body_mass(-70, 195)
    with pytest.raises(ValueError):
        body_mass(70, -195)


def test_not_numeric_value():
    with pytest.raises(ValueError):
        body_mass("seven", 195)
    with pytest.raises(ValueError):
        body_mass(70, "nineteen-five")


"""UNITTEST"""


class TestBodyMass(unittest.TestCase):
    def test_valid_values(self):
        self.assertAlmostEqual(body_mass(70, 195), 18.409)
        self.assertAlmostEqual(body_mass(50, 166), 18.145)

    def test_zero_values(self):
        self.assertRaises(ValueError, body_mass, 0, 195)
        self.assertRaises(ValueError, body_mass, 70, 0)

    def test_negative_values(self):
        self.assertRaises(ValueError, body_mass, -70, 195)
        self.assertRaises(ValueError, body_mass, 70, -195)

    def test_not_numeric_value(self):
        self.assertRaises(ValueError, body_mass, "seven", 195)
        self.assertRaises(ValueError, body_mass, 70, "nineteen-five")


if __name__ == "__main__":
    unittest.main()
