import unittest
import evacsim.disaster
import evacsim.polygon

class TestDisaster(unittest.TestCase):
    """Tests functionality in the disaster module"""

    def test_add_data(self):
        """Tests the add_data function"""
        disaster = evacsim.disaster.Disaster('Alfred')
        self.assertEqual(len(disaster.data), 0)
        disaster.add_data(disaster.Data('04/21/2021-10:00:00', evacsim.polygon.Polygon([(42.750958, -73.675494), (42.723977, -73.664851), (42.724607, -73.696780)])))
        self.assertEqual(len(disaster.data), 1)
        disaster.add_data(disaster.Data('04/21/2021-10:10:00', evacsim.polygon.Polygon([(42.750958, -73.675494), (42.723977, -73.664851), (42.739238, -73.724234)])))
        self.assertEqual(len(disaster.data), 2)
