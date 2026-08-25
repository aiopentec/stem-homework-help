---
title: Logistic Regression
layout: concept
subject: stats
topic: regression
description: >
  Logistic regression models outcomes such as probabilities or binary classes.
---

# Logistic Regression

Logistic regression predicts the probability of a binary outcome (e.g., yes/no, pass/fail) by applying the logistic (sigmoid) function to a linear combination of predictors, mapping any real number to a value between 0 and 1.

## What is logistic regression?

Logistic regression predicts the probability of a binary outcome (e.g., yes/no, pass/fail) by applying the logistic (sigmoid) function to a linear combination of predictors, mapping any real number to a value between 0 and 1.

## Basic formula

P(y=1|x) = 1 / (1 + e^−(β₀ + β₁x)), and the model is fit by maximizing the likelihood of the observed data rather than minimizing squared error.

## Example

Predicting whether a customer will churn based on their usage patterns — the model outputs a probability, which is then thresholded (commonly at 0.5) to make a yes/no prediction.

## Common mistakes

Interpreting coefficients as if they were linear-regression coefficients (they represent log-odds, not the outcome directly); using accuracy alone to evaluate imbalanced classification problems.

## Related concepts

- Linear Regression

## Questions about logistic regression

Per-concept question filtering isn't wired up yet — browse all worked
[Statistics problems](/stats/) in the meantime.
