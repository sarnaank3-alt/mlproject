import unittest
from app.backend.token_tracking.tracker import TokenTracker

class TestTokenTracking(unittest.TestCase):

    def setUp(self):
        self.token_tracker = TokenTracker()

    def test_initial_token_count(self):
        self.assertEqual(self.token_tracker.get_token_count(), 0)

    def test_add_tokens(self):
        self.token_tracker.add_tokens(10)
        self.assertEqual(self.token_tracker.get_token_count(), 10)

    def test_reset_tokens(self):
        self.token_tracker.add_tokens(5)
        self.token_tracker.reset_tokens()
        self.assertEqual(self.token_tracker.get_token_count(), 0)

    def test_token_limit_exceeded(self):
        self.token_tracker.set_token_limit(15)
        self.token_tracker.add_tokens(10)
        self.token_tracker.add_tokens(6)  # This should exceed the limit
        self.assertEqual(self.token_tracker.get_token_count(), 16)  # Should still count but indicate limit exceeded

    def test_get_cost_estimate(self):
        self.token_tracker.add_tokens(20)
        cost = self.token_tracker.get_cost_estimate()
        self.assertEqual(cost, 20 * 0.0001)  # Assuming cost per token is 0.0001

if __name__ == '__main__':
    unittest.main()