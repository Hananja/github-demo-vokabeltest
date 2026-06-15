from dataclasses import dataclass


@dataclass
class QuizResult:
    total: int
    correct: int

    @property
    def wrong(self):
        return self.total - self.correct

    @property
    def percentage(self):
        if self.total == 0:
            return 0
        return round((self.correct / self.total) * 100)


def normalize_answer(text: str) -> str:
    return text.strip().lower()


def is_correct(user_answer: str, expected_answer: str) -> bool:
    return normalize_answer(user_answer) == normalize_answer(expected_answer)


def evaluate_answers(answer_pairs):
    total = len(answer_pairs)
    correct = sum(1 for user_answer, expected_answer in answer_pairs if is_correct(user_answer, expected_answer))
    return QuizResult(total=total, correct=correct)


def run_quiz(entries):
    print("\nQuiz startet. Bitte Übersetzungen eingeben.\n")
    given_answers = []
    correct = 0
    wrong = 0

    for item in entries:
        user_answer = input(f"{item['question']}: ")
        given_answers.append((user_answer, item['answer']))

        if is_correct(user_answer, item['answer']):
            correct += 1
        else:
            wrong += 1

        print(f"Aktueller Punktestand: {correct} richtig, {wrong} falsch")

    result = evaluate_answers(given_answers)
    print("\nErgebnis")
    print("-" * 20)
    print(f"Richtig: {result.correct} von {result.total}")
    print(f"Falsch : {result.wrong}")
    print(f"Quote  : {result.percentage} %")


def ask_yes_no(prompt):
    input(f"\n{prompt}")
