import importlib.util
from pathlib import Path
import tempfile
import unittest
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ExerciseTests(unittest.TestCase):
    def test_transposition_roundtrip_multiline_unicode_and_line_endings(self):
        module = load('Transposition.py')
        for text in ['', 'x', 'odd', 'even', 'Ankara Türkiye 😀']:
            self.assertEqual(module.untranspose(module.transpose(text)), text)
        with tempfile.TemporaryDirectory() as tmp:
            paths = [Path(tmp) / name for name in ('original', 'encoded', 'decoded')]
            paths[0].write_bytes('first\r\n\r\nTürkiye\nlast'.encode())
            module.transform_file(paths[0], paths[1])
            module.transform_file(paths[1], paths[2], decode=True)
            self.assertEqual(paths[0].read_bytes(), paths[2].read_bytes())

    def test_tram_start_destinations_are_valid_and_distinct(self):
        module = load('Amusement Park Tram.py')
        for lots in range(2, 12):
            for _ in range(100):
                start, dest = module.randstart(lots)
                self.assertNotEqual(start, dest)
                self.assertIn(start, range(lots))
                self.assertIn(dest, range(lots))
        tram = module.Tram(0, {0: module.ParkingLot(0), 1: module.ParkingLot(1)})
        travellers = [module.Tourist(1, 0), module.Tourist(1, 0)]
        tram.tourists = travellers.copy()
        tram.get_off()
        self.assertEqual(tram.tourists, [])
        self.assertTrue(all(t.arrived for t in travellers))

    def test_sentiment_uses_whole_words_and_standard_deviation(self):
        module = load('Sentiment Analysis.py')
        self.assertEqual(module.findscore(['4 good goodness GOOD', '0 bad'], 'good'), [4, 4])
        self.assertEqual(module.standard_deviation([0, 4]), 2)
        self.assertEqual(module.process_list(['unknown'], ['4 good'])[0][1], 0)

    def test_image_filters_accept_grayscale_and_rgba_images(self):
        module = load('Image Filters.py')
        with tempfile.TemporaryDirectory() as tmp:
            source, target = Path(tmp)/'input.png', Path(tmp)/'output.png'
            Image.new('RGBA', (2, 2), (100, 50, 200, 255)).save(source)
            module.vintage_look(source, target)
            with Image.open(target) as image:
                self.assertEqual(image.getpixel((0, 0)), (100, 50, 100))
            Image.new('L', (2, 2), 127).save(source)
            module.grayscale_look(source, target)
            with Image.open(target) as image:
                self.assertEqual(image.getpixel((0, 0)), (127, 127, 127))

    def test_exercises_are_import_safe(self):
        for name in ('LostLuggage.py', 'SliceProgram.py', 'Stocks.py'):
            load(name)


if __name__ == '__main__':
    unittest.main()
