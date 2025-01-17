# class User:
#     def __init__(self, user_id, username):
#         print("New user being created...")
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User("001", "Ander")
# print(user_1.username)
#
# # user_2 = User()
# # user_2.id = "002"
# # user_2.name = "angela"
# user_2 = User("002", "Angela")
# user_2.follower = 3
# print(user_2.id)
#
#
# user_1.follow(user_2)
# print(f"User_1 following: {user_1.following}")
# print(f"User_1 folowers: {user_1.followers}")
# print(f"User_2 following: {user_2.following}")
# print(f"User_2 folowers: {user_2.followers}")


from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

