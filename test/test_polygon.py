import unittest
import evacsim.polygon

class TestPolygon(unittest.TestCase):
    """Tests the functionality in the polygon module"""

    def test_contains(self):
        """Tests the contains function"""
        poly = evacsim.polygon.Polygon([(42.750958, -73.675494), (42.723977, -73.664851), (42.724607, -73.696780)])
        self.assertTrue(poly.contains(42.730322, -73.680254))
        self.assertFalse(poly.contains(42.719554, -73.746986))

    def test_reverse(self):
        """Tests the reverse_lat_lng function"""
        poly = evacsim.polygon.Polygon([(42.750958, -73.675494), (42.723977, -73.664851), (42.724607, -73.696780)])
        points = poly.points
        reversed_points = poly.reverse_lat_lng()
        for i in range(len(points)):
            self.assertEqual(points[i][0], reversed_points[i][1])
            self.assertEqual(points[i][1], reversed_points[i][0])
