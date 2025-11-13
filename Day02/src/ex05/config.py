num_of_steps = 3

report_template = """We have made {observations} observations from tossing a coin: {tails} of them were tails and {heads} of them were heads. The probabilities are {head_proc:.2f}% and {tail_proc:.2f}%, respectively. Our forecast is that in the next {num_of_steps} observations we will have: {pred_heads} tail and {pred_tails} heads."""

LOG_FILE = "analytics.log"
LOG_FORMAT = "%(asctime)s %(message)s"

TELEGRAM_CHAT_ID = "340199175"
TELEGRAM_API_URL = "8087944996:AAEO_iAdAMwVP0Q1nV1urX5KQsN9ld8c6DE"