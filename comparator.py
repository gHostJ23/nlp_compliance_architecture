"""
comparator.py

Evaluates transcribed text strings against a dictionary of mandated legal disclaimers.
Utilizes fuzzy string matching to account for minor transcription errors or regional accents 
from the offline NLP engine.
"""

from rapidfuzz import fuzz

def evaluate_compliance_phrase(transcript: str, target_phrase: str, threshold: float = 85.0) -> bool:
    """
    Compares the transcribed audio text against the required compliance phrase.
    
    Args:
        transcript (str): The raw text output from the Vosk NLP model.
        target_phrase (str): The exact legal disclaimer required for QA compliance.
        threshold (float): The minimum similarity percentage required to pass.

    Returns:
        bool: True if the phrase meets the threshold, False otherwise.
    """
    
    if not transcript or not target_phrase:
        return False
        
    # Calculate the similarity ratio using RapidFuzz
    similarity_score = fuzz.partial_ratio(transcript.lower(), target_phrase.lower())
    
    if similarity_score >= threshold:
        return True
        
    return False

# Basic Unit Test for Console Verification
if __name__ == "__main__":
    required_disclaimer = "I am calling on a recorded line regarding your epic communication preferences."
    
    # Simulating a slightly flawed audio transcription
    mock_transcript = "I am calling on a recorded line regarding your communication preferences."
    
    passed = evaluate_compliance_phrase(mock_transcript, required_disclaimer)
    print(f"Compliance Check Passed: {passed}")
