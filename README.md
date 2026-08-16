# Real-Time NLP Compliance Dashboard: Architecture & Logic Stubs

## 1. Executive Summary
Within the Aetna Lifestyle and Condition Coaching program, Member Engagement Associates must deliver legally mandated disclaimers to patients prior to enrollment. Navigating complex visual scripts while managing live patient conversations causes cognitive overload, leading directly to human error and lowered Quality Assurance (QA) audit scores. 

This repository serves as the Technical Design Document and initial logic build for a localized, voice-activated compliance tool. The objective is to introduce a real-time Natural Language Processing (NLP) dashboard that actively listens to the associate and visually confirms when mandatory phrases are spoken.

## 2. Architectural Constraints
To adhere to strict enterprise security protocols and HIPAA regulations, this application enforces the following:
* **Zero Cloud Processing:** The application will not interface with external cloud APIs. 
* **Localized Execution:** All speech-to-text processing is handled entirely offline using the open-source Vosk NLP library.
* **Mock Validation:** To prevent the accidental capture of live Protected Health Information (PHI), initial testing utilizes fabricated `.wav` audio files. 

## 3. System Data Flow
The pipeline isolates the audio ingestion, the string-matching logic, and the visual UI into distinct modular systems.

```mermaid
graph TD
    A[Mock Audio .wav] --> B[Audio Ingestion Engine]
    B --> C[Vosk Offline NLP Model]
    C --> D[Transcribed Text String]
    D --> E{Fuzzy String Comparator}
    E -->|Similarity >= 85%| F[Tkinter GUI: Status Green]
    E -->|Similarity < 85%| G[Tkinter GUI: Status Red]
