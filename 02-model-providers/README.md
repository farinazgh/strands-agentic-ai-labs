# Lab 02 — Switching Model Providers

## Overview

Strands abstracts model providers behind a common interface,
allowing developers to switch models without redesigning the
agent harness.

## Key Takeaways

### Model Abstraction and Portability

- Model providers are abstracted behind a common interface.
- Switching providers requires minimal application code changes.
- Model portability does not guarantee behavioural consistency.
- Explicitly configure models rather than relying on SDK defaults.

### Model Selection

- Model selection is an architectural decision, not merely
  a configuration decision.
- Different models have different reasoning, planning and
  tool-calling capabilities.
- Select models based on task complexity, accuracy, cost
  and latency.

### Multi-Model Architecture

- Use specialized models for different responsibilities
  within a multi-agent system.
- Consider different models for generation and evaluation
  to reduce correlated bias.

### Local Models

- Local models offer privacy, offline execution and
  potentially lower inference costs.
- Reasoning and tool-calling capabilities may be weaker
  than those of hosted frontier models.

### Reliability and Evaluation

- Switching models can fundamentally change agent behaviour,
  not merely response quality.
- Reevaluate agent behaviour and reliability whenever
  the underlying model changes.

## Architectural Principle

> Model portability does not imply behavioural equivalence.
> Same harness, different model, potentially different behaviour.

## References

- [Strands — Switching Model Providers](https://strandsagents.com/docs/learning/switching-model-providers/)