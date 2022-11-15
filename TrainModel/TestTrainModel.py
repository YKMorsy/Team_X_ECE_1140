import unittest
from TrainModel.TrainModel import TrainModel

class TestTrainModel(unittest.TestCase):
    def test_generate_engine_failure(self):
        #Define a Train Model T (we don't need a handler for our single-train tests)
        T = TrainModel(handler = None, ID = 0)

        #Generate an engine failure
        T.generate_engine_failure()

        #Check if the engine has actually failed
        self.assertTrue(T.engine_failure)
    
    def test_generate_brake_failure(self):
        #Define a Train Model T (we don't need a handler for our single-train tests)
        T = TrainModel(handler = None, ID = 0)

        #Generate a brake failure
        T.generate_brake_failure()

        #Check if the brakes have actually failed
        self.assertTrue(T.brake_failure)

    def test_generate_signal_pickup_failure(self):
        #Define a Train Model T (we don't need a handler for our single-train tests)
        T = TrainModel(handler = None, ID = 0)

        #Generate a signal pickup failure
        T.generate_signal_pickup_failure()

        #Check if the signal pickup system has actually failed
        self.assertTrue(T.signal_failure)

    def test_engine_power_with_failure(self):
        #Define a Train Model T (we don't need a handler for our single-train tests)
        T = TrainModel(handler = None, ID = 0)

        #Generate an engine failure
        T.generate_engine_failure()

        #Attempt to set the engine power to 1000 Watts
        T.set_engine_power(1000)

        #Check that the engine power is at 0
        self.assertAlmostEqual(0, T.engine_power)

    def test_brake_with_failure(self):
        #Define a Train Model T (we don't need a handler for our single-train tests)
        T = TrainModel(handler = None, ID = 0)

        #Set the engine power high, and iterate forward for ~10 seconds or so
        T.set_engine_power(400000)
        T.update(1)
        T.update(1)
        T.update(1)
        T.update(1)
        T.update(1)
        T.update(1)
        T.update(1)
        T.update(1)
        T.update(1)
        T.update(1)
        T.set_engine_power(0)

        #Generate a brake failure, and trigger the e-brake
        T.generate_brake_failure()
        T.emergency_brake = True

        #Set the velocity before and after the update with the e-brake and brake failure
        v0 = T.velocity
        T.update(1)
        v1 = T.velocity

        #If the velocities differ by less than 90% of the brake deceleration, than the test is successful
        self.assertLess(v0-v1, 0.9*T.emergency_deceleration)

if __name__ == '__main__':
    unittest.main()