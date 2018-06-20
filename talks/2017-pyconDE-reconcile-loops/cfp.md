## Don't fire-and-forget celery tasks, use reconcile loops.

25 Minutes + 5 Minute Q&A

keywords: celery, django, rest, ops


### Elevator pitch
500 calls to AWS when my user clicks this button. Ok, that's slow, let's put it in a celery task.

If it fails, how many times should I retry?

Ok, I have these celery AsyncResults, now what?

What if the user clicks the button again, before execution finishes?

There must be a better way!


## Description

The talk will present a pattern of handling asynchronous behavior, using the
open source project Zinc (https://github.com/presslabs/zinc) as a case study.

The talk will be structured in 4 parts:

1. presenting the problem
2. a summary of common solutions and their shortcomings
3. how reconcile loops can be used to solve the problem
4. solution review, potential downsides and possible improvements


1. The problem: we're building a REST API, to automate some parts of our
infrastructure, and some operations take so much time it's not possible to
perform them in the regular request/response cycle.

2. A common solution would be to extract the slow parts into a celery task and
call that asynchronously. We'll explore some of the potential error states our
system might end up in.

3. We'll introduce the idea of reconcile loops, and refactor our system to use
them.

4. We'll review our solution, consider how it addressed the downsides of the
previous one, and explore the trade-offs and other potential applications.


## Bio:
