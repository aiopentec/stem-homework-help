---
title: Entropy
layout: concept
subject: stats
topic: probability
description: >
  Entropy measures uncertainty or information associated with a probability distribution.
---

# Entropy

Entropy quantifies how unpredictable a random variable is — a distribution concentrated on one outcome has low entropy, while a uniform distribution over many outcomes has high entropy.

## What is entropy?

Entropy quantifies how unpredictable a random variable is — a distribution concentrated on one outcome has low entropy, while a uniform distribution over many outcomes has high entropy.

## Basic formula

For a discrete random variable X with outcomes x₁...xₙ, Shannon entropy is H(X) = −Σ p(xᵢ) log₂ p(xᵢ), measured in bits.

## Example

A fair coin flip has entropy of 1 bit (maximum uncertainty for two outcomes); a coin that always lands heads has entropy of 0 (no uncertainty at all).

## Common mistakes

Confusing entropy with variance (they measure different things — variance measures spread of values, entropy measures unpredictability of outcomes); forgetting entropy depends on the log base used (bits vs. nats).

## Related concepts

- Probability

## Questions about entropy

Per-concept question filtering isn't wired up yet — browse all worked
[Statistics problems](/stats/) in the meantime.
