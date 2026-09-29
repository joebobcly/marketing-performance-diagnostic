# Marketing Performance Diagnostic

A minimal Python project for diagnosing changes in marketing performance across campaigns and channels. The goal is to compare a previous period against the current period, identify likely performance changes, and surface actionable insights without adding unnecessary framework overhead.

## Purpose

This project is intended to help analyze campaign-level performance data such as spend, revenue, and leads across two reporting periods. The first version focuses on the project skeleton and sample data so future diagnostic logic can be added in a clean, testable way.

## Initial Architecture

- `data/` contains sample CSV files for campaign performance inputs.
- `src/` is reserved for application code and future analysis modules.
- `tests/` is intentionally left empty for future automated checks.
- `.gitignore` keeps the repository clean for Python development.
- `requirements.txt` tracks the minimal dependencies required for data work.

## Current State

This repository is intentionally minimal and does not yet implement the analysis logic. It provides a ready-to-use project structure for building the marketing diagnostic workflow, including a realistic sample dataset for campaign comparisons.
