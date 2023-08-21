entail_prompt_v1=f"""Please classify the provided (Premise, Hypothesis) according to the definition.

% Definition of classification：
Entailment: the hypothesis is a sentence with a similar meaning as the premise. 
Contradiction: the hypothesis is a sentence with a contradictory meaning. 
Neutral: the hypothesis is a sentence with mostly the same lexical items as the premise but a different meaning.

% Here are three examples:
"Premise":"Einstein's theory of relativity revolutionized physics and our understanding of space-time. [Einstein, 1905] "
"Hypothesis":Einstein developed the theory of relativity.",
"Classification":"Entailment"

"Premise":"[Passage about history of baseball] [Passage about rules of chess]"
"Hypothesis":"Soccer is the most popular sport in the world."
"Classification":"Neutral"

"Premise":"[Passage saying Einstein was a biologist]"
"Hypothesis":"Einstein was a physicist."
"Classification":"Contradiction"

% 请基于以上定义与例子，判断以下分类：
"Premise":{{Premise}}
"Hypothesis":{{Hypothesis}}
"""


entail_prompt_v2=f"""Please classify the provided (Premise, Hypothesis) according to the definition.

% Definition of classification：
1: the hypothesis is a sentence with a similar meaning as the premise. 
0: the hypothesis is a sentence with a contradictory meaning. 
0.5: the hypothesis is a sentence with mostly the same lexical items as the premise but a different meaning.

% Here are three examples:
"Premise":"Einstein's theory of relativity revolutionized physics and our understanding of space-time. [Einstein, 1905] "
"Hypothesis":Einstein developed the theory of relativity.",
"Classification":1

"Premise":"[Passage about history of baseball] [Passage about rules of chess]"
"Hypothesis":"Soccer is the most popular sport in the world."
"Classification":0

"Premise":"[Passage saying Einstein was a biologist]"
"Hypothesis":"Einstein was a physicist."
"Classification":0.5

% 请基于以上定义与例子，判断以下分类：
"Premise":{{Premise}}
"Hypothesis":{{Hypothesis}}
"""