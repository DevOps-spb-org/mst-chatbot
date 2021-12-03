from typing import List


class Quiz:
	type: str = 'quiz'
	
	def __init__(self, quiz_id, question, options, correct_option_id, owner_id):
	
		self.quiz_id: str = quiz_id
		self.question: str = question
		self.options: List[str] = [*options]
		self.correct_option_id: int = correct_option_id
		self.owner: int = owner_id
		self.winners: List[int] = []
		self.chat_id: int = 0
		self.message_id: int = 0
		
	