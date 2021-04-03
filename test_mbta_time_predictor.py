import unittest
import mbta_time_predictor



class TestPredictor(unittest.TestCase):
    def test_no_stops_entered(self):
        """
        should issue an error if no stops/nothing is entered
        """

        self.assertEqual(mbta_time_predictor.time_predictor('',''), "An Error has occured, Please check the stop names.")

    def test_stop1_invalid(self):
        pass

    def test_stop2_invalid(self):
        pass
    
    def test_stop1_stop2_invalid(self):
        pass

    def test_stop1_stop2_not_on_same_route(self):
        pass
    
    def test_time_predicted_success(self):
        self.assertEqual(mbta_time_predictor.time_predictor('Cleveland Circle','North station'), "An Error has occured, Please check the stop names.")

        pass
    




if __name__ == '__main__':
    unittest.main()