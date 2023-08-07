import pytest


import temperature_converter

class TestConverter:

    def test_fahrenheit_to_celsius(self):
        # Test freezing temperature
        assert temperature_converter.f_to_c(32) == 0
        # Test boiling temperature
        assert temperature_converter.f_to_c(212) == 100
        # Test float
        assert temperature_converter.f_to_c(31.0) == pytest.approx(-0.5555555555)
        # Test errors
        with pytest.raises(TypeError):
            temperature_converter.f_to_c("freezing")
    
    def test_celsius_to_farenheit(self):
        # Test freezing temperature
        assert temperature_converter.c_to_f(0) == 32
        # Test boiling temperature
        assert temperature_converter.c_to_f(100) == 212
        # Test float
        assert temperature_converter.c_to_f(-0.5555555555) == pytest.approx(31.0)
        # Test errors
        pytest.raises(TypeError, temperature_converter.c_to_f, "freezing")
        # another way to make the raises() function raise the TypeError with 
        # the argument "freezing":
        # with pytest.raises(TypeError):
        #     temperature_converter.c_to_f("freezing")

pytest.main()