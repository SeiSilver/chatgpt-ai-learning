# Prompting Principles

---

## Principle 1: Write clear and specific instructions

### Tactic 1:

- Use delimiters to clearly indicate distinct parts of the input
- Delimiters can be anything like: ```, """, < >, <tag> </tag>, :

### Tactic 2:

- Ask for a structured output such as HTML, JSON

### Tactic 3:

Ask the model to check whether conditions are satisfied
Check assumptions required to do the task

### Tactic 4: "Few-shot" prompting

- Give successful examples of completing tasks
- Then ask model to perform the task

---

## Principle 2: Give the model time to “think”

### Tactic 1:

- Specify the steps required to complete a task

### Tactic 2:

- Instruct the model to work out its own solution before rushing to a conclusion

---

## Limitation

### Hallucination:

- Makes statements that sound reasonable but are not true

### Reducing hallucinations:

- First find relevant information
- Then answer the question
- Based on the relevant information.