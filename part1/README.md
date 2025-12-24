# HBnB Evolution – Part 1

## Introduction
This document describes the technical design and architecture of the HBnB Evolution application.

## High-Level Architecture
The following diagram illustrates the layered architecture of the application, including the Presentation, Business Logic, and Persistence layers, and how they communicate using the Facade pattern.

![High-Level Package Diagram](package_diagram.png)

## Business Logic Layer
The class diagram below represents the core entities of the system: User, Place, Review, and Amenity, along with their relationships.

![Class Diagram](class_diagram.png)

## API Interaction Flow
The following sequence diagrams illustrate the interaction flow for key API calls:
- User Registration
- Place Creation
- Review Submission
- Fetching a list of places

![Sequence Diagrams](sequence_diagrams.png)
