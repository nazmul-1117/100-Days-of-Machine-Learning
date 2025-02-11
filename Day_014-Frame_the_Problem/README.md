# Day_014-Frame of Problem
It's the first Steps of MLDLC

In artificial intelligence, the "frame problem" refers to the challenge of representing the effects of an action in a logical system without explicitly stating all the things that do not change as a result of that action, essentially requiring an AI to identify and focus on only relevant aspects of a situation while ignoring irrelevant details, similar to how humans use common sense to navigate the world; it's a major hurdle in designing intelligent systems that can reason about complex situations and make appropriate decisions based on changing environments. 

```
1. Business Problem
2. Types of Problem
3. Current data
4. Getting Data
5. Matrix to measure
6. Online vs Batch
7. Check Assumption

```


## Key points about the frame problem:
### Logic-based challenge:
The frame problem is particularly prominent when using formal logic to represent knowledge about an environment, as it becomes cumbersome to explicitly list all the aspects that remain unchanged when an action occurs. 

### Common sense issue:
Humans naturally understand that most things in a situation stay the same when performing an action, but for an AI, this requires explicit representation which can be computationally expensive. 

### Example scenario:
Imagine an AI tasked with navigating a room. When it moves to pick up a cup, it needs to know that the table, chairs, and other objects in the room remain in their positions unless explicitly interacted with, without having to explicitly state this in its reasoning process. 

## Approaches to addressing the frame problem:
### Default reasoning:
Using default assumptions about what typically remains unchanged in a situation, only updating information when there is specific evidence to the contrary. 

### Model-based reasoning:
Building a model of the environment where changes are explicitly represented, allowing the AI to reason about the consequences of actions within that model. 
### Focus on relevant aspects:
Developing techniques to identify and prioritize only the most relevant information in a given situation, reducing the need to consider every possible factor. 