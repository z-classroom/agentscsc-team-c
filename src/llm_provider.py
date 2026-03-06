import os
import random

class MockLLM:
    """
    A mock language model used for testing.
    Returns simple structured responses without requiring an API key.
    """

    def generate(self, messages):
        """
        Simulate a response based on the last user message.
        """

        user_message = ""

        for m in reversed(messages):
            if m["role"] == "user":
                user_message = m["content"]
                break

        responses = [
            "Your argument is generally clear, but you may want to strengthen the supporting explanation.",
            "The paragraph introduces an interesting idea, but the thesis could be stated more explicitly.",
            "Your writing is concise and readable. Consider adding an example to strengthen the argument.",
            "The structure is logical, though some sentences could be clarified to improve flow."
        ]

        feedback = random.choice(responses)

        return f"""
Clarity Assessment
{feedback}

Strengths
- The topic is introduced clearly
- The writing is concise

Areas for Improvement
- The central claim could be more explicit
- Additional supporting detail may help strengthen the argument

Suggested Improvements
- Consider stating your thesis more directly
- Provide an example to support your claim

Clarity Rating
7/10
"""

