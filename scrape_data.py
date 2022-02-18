import logging
import csv
from typing import List
from dataclasses import asdict
from json import dump
from analysis.src.python.data_collection.hyperskill.hyperskill_client import HyperskillClient
from analysis.src.python.data_collection.hyperskill.api.submissions import Submission, Feedback


PORT = 8000

STEPS_IDS = [8443, 7323, 9480, 6818]

SUBMISSIONS_CSV_PATH = "./data/submissions.csv"
FEEDBACKS_JSON_PATH = "./data/submissions_feedbacks.json"

STEPS_CSV_PATH = "./data/steps.csv"

SUBMISSIONS_FIELDS_NAMES = ["id", "step", "status", "time", "lang", "code"]
STEPS_FIELDS_NAMES = ["id", "seconds_to_complete", "solved_by", "success_rate"]


def download_submissions(client: HyperskillClient, steps_ids: List[int],
                         subm_csv_path: str, feedbacks_json_path: str):
    submissions = client.get_submissions(step_ids=steps_ids)
    feedbacks = {}

    with open(subm_csv_path, "w") as submissions_file, \
            open(feedbacks_json_path, "w") as feedbacks_file:
        writer = csv.writer(submissions_file, lineterminator="\n")
        writer.writerow(SUBMISSIONS_FIELDS_NAMES)
        for submission in submissions:
            writer.writerow([
                submission.id, submission.step, submission.status,
                submission.time, submission.reply.language,
                submission.reply.code
            ])
            feedbacks[submission.id] = asdict(submission.feedback) \
                if isinstance(submission.feedback, Feedback) \
                else submission.feedback
        dump(feedbacks, feedbacks_file, ensure_ascii=False, indent=2)

    logging.info(
        f"Written {len(submissions)} submission(s) into {subm_csv_path}")
    logging.info(
        f"Written {len(submissions)} feedback(s) into {feedbacks_json_path}")


def download_steps(client: HyperskillClient, steps_ids: List[int],
                   csv_path: str):
    steps = client.get_steps(ids=steps_ids)

    with open(csv_path, "w") as csv_file:
        writer = csv.writer(csv_file, lineterminator="\n")
        writer.writerow(STEPS_FIELDS_NAMES)
        for step in steps:
            writer.writerow([
                step.id, step.seconds_to_complete, step.solved_by,
                step.success_rate
            ])
    logging.info(
        f"Written {len(steps)} step(s) into {csv_path}")


logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    client = HyperskillClient(PORT)

    download_submissions(client, STEPS_IDS,
                         SUBMISSIONS_CSV_PATH, FEEDBACKS_JSON_PATH)
    download_steps(client, STEPS_IDS, STEPS_CSV_PATH)
